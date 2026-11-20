import unittest

from file_kinds import count_file_kinds


class FileKindsTest(unittest.TestCase):
    def test_combines_case_variants_and_preserves_extensionless_files(self):
        paths = ["src/app.py", "tools/report.PY", "bin/run", ".gitignore", "docs/guide.md"]
        self.assertEqual(count_file_kinds(paths), {"(no extension)": 2, ".md": 1, ".py": 2})

    def test_empty_change(self):
        self.assertEqual(count_file_kinds([]), {})
