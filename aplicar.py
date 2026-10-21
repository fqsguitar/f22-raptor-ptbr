#!/usr/bin/env python3
"""Aplica somente o delta PT-BR em arquivos locais com hashes conhecidos."""
import argparse, base64, hashlib, json, os, shutil, tempfile, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def digest(data):
    return hashlib.sha256(data).hexdigest()

def load(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8-sig'))

def atomic_write(path, data):
    handle, temporary = tempfile.mkstemp(prefix='ptbr_', suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(handle, 'wb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)

def checked_backup(path, data, directory):
    backup = directory / (path.name + '.' + digest(data) + '.bak')
    if backup.exists():
        if digest(backup.read_bytes()) != digest(data):
            raise ValueError('Backup existente invalido: ' + backup.name)
    else:
        atomic_write(backup, data)
    if digest(backup.read_bytes()) != digest(data):
        raise ValueError('Falha na verificacao do backup')
    return backup.name

def apply(game, specification, simulate=False):
    plans = []
    for item in specification['files']:
        path = game / item['name']
        original = path.read_bytes()
        initial = digest(original)
        if initial == item['result_sha256']:
            print(item['name'] + ': ja traduzido.')
            continue
        variant = item['bases'].get(initial)
        if variant is None or len(original) != item['size']:
            raise ValueError(item['name'] + ': versao desconhecida. Nenhum arquivo alterado.')
        result = bytearray(original)
        last_end = 0
        for change in variant['changes']:
            offset, length = change['offset'], change['length']
            replacement = base64.b64decode(change['data'], validate=True)
            if offset < last_end or offset < 0 or offset + length > len(original):
                raise ValueError('Intervalo de patch invalido')
            if len(replacement) != length or digest(original[offset:offset+length]) != change['before_sha256']:
                raise ValueError('Conteudo divergente no intervalo')
            result[offset:offset+length] = replacement
            last_end = offset + length
        if len(result) != len(original) or digest(result) != item['result_sha256']:
            raise ValueError('Validacao do resultado falhou')
        plans.append((path, original, bytes(result), item))
    if simulate:
        print('Validacao concluida: ' + str(len(plans)) + ' arquivos prontos; nenhuma gravacao.')
        return
    if not plans:
        print('Traducao ja instalada.')
        return
    backup_dir = game / '.ptbr_backups'
    backup_dir.mkdir(exist_ok=True)
    state_path = backup_dir / 'instalacao.json'
    previous_state = json.loads(state_path.read_text()) if state_path.exists() else {'files': {}}
    state = {'version': specification['version'], 'files': dict(previous_state['files'])}
    for path, original, result, item in plans:
        backup_name = checked_backup(path, original, backup_dir)
        state['files'][path.name] = {'backup': backup_name, 'before_sha256': digest(original), 'after_sha256': digest(result)}
    written = []
    try:
        for path, original, result, item in plans:
            if digest(path.read_bytes()) != digest(original):
                raise ValueError('Arquivo alterado durante a instalacao: ' + path.name)
            atomic_write(path, result)
            written.append((path, original))
            if digest(path.read_bytes()) != item['result_sha256']:
                raise ValueError('Falha na leitura apos gravacao')
        atomic_write(state_path, json.dumps(state, indent=2).encode())
    except BaseException:
        for path, original in reversed(written):
            atomic_write(path, original)
        raise
    print('Traducao instalada. Backup verificado em ' + str(backup_dir))

def restore(game):
    directory = game / '.ptbr_backups'
    state = json.loads((directory / 'instalacao.json').read_text())
    plans = []
    for name, item in state['files'].items():
        if name not in ('Raptor.pff', 'Raptor.exe') or Path(item['backup']).name != item['backup']:
            raise ValueError('Registro de restauracao invalido')
        path = game / name
        original = path.read_bytes()
        if digest(original) == item['before_sha256']:
            continue
        if digest(original) != item['after_sha256']:
            raise ValueError(name + ': foi modificado depois da instalacao; restauracao cancelada.')
        backup = (directory / item['backup']).read_bytes()
        if digest(backup) != item['before_sha256']:
            raise ValueError('Backup divergente')
        plans.append((path, original, backup))
    written = []
    try:
        for path, original, backup in plans:
            atomic_write(path, backup)
            written.append((path, original))
    except BaseException:
        for path, original in reversed(written):
            atomic_write(path, original)
        raise
    print('Arquivos anteriores restaurados; backups preservados.')

def cleanup(game):
    selected = []
    for item in load('temporarios.json'):
        name = item['name']
        if Path(name).name != name or not name.startswith('f22_') or Path(name).suffix.lower() not in ('.py', '.csv', '.txt'):
            raise ValueError('Nome nao permitido no inventario')
        path = game / name
        if path.is_file() and digest(path.read_bytes()) == item['sha256']:
            selected.append((path, item))
    if not selected:
        print('Nenhum temporario conhecido para limpar.')
        return
    backup_dir = game / '.ptbr_backups'
    backup_dir.mkdir(exist_ok=True)
    signature = digest(json.dumps([i for p, i in selected], sort_keys=True).encode())[:16]
    archive = backup_dir / ('temporarios-' + signature + '.zip')
    if not archive.exists():
        with zipfile.ZipFile(archive, 'x', zipfile.ZIP_DEFLATED) as stream:
            for path, item in selected:
                stream.write(path, path.name)
    with zipfile.ZipFile(archive) as stream:
        if stream.testzip() is not None:
            raise ValueError('Backup de temporarios corrompido')
        for path, item in selected:
            if digest(stream.read(path.name)) != item['sha256']:
                raise ValueError('Temporario diverge do backup')
    removed = 0
    for path, item in selected:
        if digest(path.read_bytes()) == item['sha256']:
            path.unlink()
            removed += 1
    print(str(removed) + ' temporarios arquivados e removidos; arquivos desconhecidos preservados.')

def main():
    parser = argparse.ArgumentParser(description='Traducao PT-BR F-22 Raptor. Feche o jogo antes de aplicar.')
    parser.add_argument('pasta', type=Path, help='Pasta que contem Raptor.pff e Raptor.exe')
    parser.add_argument('--simular', action='store_true')
    parser.add_argument('--restaurar', action='store_true')
    parser.add_argument('--limpar-temporarios', action='store_true')
    args = parser.parse_args()
    if args.restaurar and (args.simular or args.limpar_temporarios):
        parser.error('Use --restaurar sozinho.')
    if args.restaurar:
        restore(args.pasta.resolve())
    else:
        apply(args.pasta.resolve(), load('patch.json'), args.simular)
        if args.limpar_temporarios and not args.simular:
            cleanup(args.pasta.resolve())

if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        raise SystemExit('ERRO: ' + str(error))
