import base64
import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path

source = Path(__file__).resolve().parents[1] / 'aplicar.py'
spec = importlib.util.spec_from_file_location('aplicar', source)
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)

class InstallerTests(unittest.TestCase):
    def test_apply_idempotence_restore_and_reject_unknown(self):
        sha = lambda data: hashlib.sha256(data).hexdigest()
        old, new = b'HELLO\0UNCHANGED', b'OLA  \0UNCHANGED'
        patch = {'version': 'test', 'files': [{'name': 'Raptor.pff', 'size': len(old), 'result_sha256': sha(new), 'bases': {sha(old): {'changes': [{'offset': 0, 'length': 5, 'before_sha256': sha(old[:5]), 'data': base64.b64encode(new[:5]).decode()}]}}}]}
        with tempfile.TemporaryDirectory() as name:
            game = Path(name)
            path = game / 'Raptor.pff'
            path.write_bytes(old)
            installer.apply(game, patch, simulate=True)
            self.assertEqual(path.read_bytes(), old)
            installer.apply(game, patch)
            self.assertEqual(path.read_bytes(), new)
            installer.apply(game, patch)
            self.assertEqual(path.read_bytes(), new)
            installer.restore(game)
            self.assertEqual(path.read_bytes(), old)
            path.write_bytes(b'X' + old[1:])
            with self.assertRaises(ValueError):
                installer.apply(game, patch)
            self.assertEqual(path.read_bytes(), b'X' + old[1:])

    def test_all_files_preflight_before_any_write(self):
        sha = lambda data: hashlib.sha256(data).hexdigest()
        patch = {'version': 'test', 'files': []}
        for name, old, new in [('Raptor.pff', b'ABC', b'XYZ'), ('Raptor.exe', b'123', b'456')]:
            patch['files'].append({'name': name, 'size': 3, 'result_sha256': sha(new), 'bases': {sha(old): {'changes': [{'offset': 0, 'length': 3, 'before_sha256': sha(old), 'data': base64.b64encode(new).decode()}]}}})
        with tempfile.TemporaryDirectory() as name:
            game = Path(name)
            (game / 'Raptor.pff').write_bytes(b'ABC')
            (game / 'Raptor.exe').write_bytes(b'BAD')
            with self.assertRaises(ValueError):
                installer.apply(game, patch)
            self.assertEqual((game / 'Raptor.pff').read_bytes(), b'ABC')
            self.assertFalse((game / '.ptbr_backups').exists())

if __name__ == '__main__':
    unittest.main()
