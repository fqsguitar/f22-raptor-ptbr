# F-22 Raptor PT-BR

Patch de traducao de textos do NovaLogic F-22 Raptor para portugues do Brasil, sem acentos ou cedilha dentro dos arquivos do jogo.

A versao 1.0 cobre os 2.219 campos identificados nas 12 tabelas RTXT ativas do PFF analisado: campanhas, briefings, radio escrito, objetivos, menus, HUD e ajuda. Foram alterados 1.836 campos; os restantes incluem nomes proprios, siglas, numeros e campos vazios. Tambem ha avisos traduzidos do executavel.

## Instalacao facil no Windows — sem instalar Python

1. Tenha o jogo instalado e feche-o.
2. Abra **[Releases](https://github.com/fqsguitar/f22-raptor-ptbr/releases)** e baixe `F22-Raptor-PTBR-Windows.zip` quando estiver disponivel.
3. Extraia o ZIP em qualquer pasta.
4. Execute **Instalar.cmd** e informe onde estao `Raptor.pff` e `Raptor.exe` (exemplo: `G:\Jogos\F-22 Raptor`).
5. Aguarde a verificacao de hashes, criacao do backup e aplicacao da traducao.

**Nao precisa ter Python instalado.** O `Traduzir_F22.exe` vem incluido no pacote para Windows.

O instalador nao aplica o patch a arquivos de versoes desconhecidas. Uma segunda execucao reconhece o jogo ja traduzido. Os backups ficam na pasta `.ptbr_backups` dentro da instalacao do jogo.

**Ainda nao apareceu ZIP em Releases?** O mantenedor pode abrir [Actions: Windows portatil](https://github.com/fqsguitar/f22-raptor-ptbr/actions/workflows/windows.yml), clicar em **Run workflow** e baixar o artefato `F22-Raptor-PTBR-Windows` quando terminar. Ao criar uma tag `v*`, o workflow tambem publica o ZIP em Releases.

## Uso avancado (opcional, com Python)

Para desenvolvedores que quiserem executar o codigo diretamente, Python 3.8+:

```powershell
python aplicar.py "G:\Jogos\F-22 Raptor"
python aplicar.py "G:\Jogos\F-22 Raptor" --simular
python aplicar.py "G:\Jogos\F-22 Raptor" --restaurar
python aplicar.py "G:\Jogos\F-22 Raptor" --limpar-temporarios
```

Esses comandos tambem funcionam com o executavel portatil substituindo `python aplicar.py` por `Traduzir_F22.exe`.

A limpeza opcional remove apenas nomes listados em `temporarios.json` quando o conteudo confere com o hash registrado, depois de arquivar e verificar. Nao remove arquivos desconhecidos. Os arquivos temporarios arquivados nao sao restaurados por `--restaurar`.

## Compatibilidade e seguranca

O `Raptor.pff` possui 113.493.525 bytes. As variantes aceitas sao identificadas por hashes exatos em `patch.json`; nome e tamanho nao bastam. O patch preserva tamanhos de arquivo, offsets e marcadores de controle; os dados originais do jogo que nao precisam ser traduzidos permanecem inalterados.

Veja [RELATORIO.md](RELATORIO.md) e [PENDENCIAS.md](PENDENCIAS.md) para o alcance dos testes e as limitacoes de verificacao visual.

`traducoes.json` registra textos traduzidos, offsets e capacidades. `patch.json` contem deltas e hashes, sem distribuir o jogo completo.

## Distribuicao

Este repositorio nao inclui o jogo completo, executavel original, PFF original, saves ou bibliotecas. Tenha sua propria instalacao. A presenca em sites de abandonware nao comprova licenca de redistribuicao.

A licenca MIT em [LICENSE](LICENSE) cobre as ferramentas originais deste projeto, nao os direitos sobre o jogo. Veja [NOTICE.md](NOTICE.md).
