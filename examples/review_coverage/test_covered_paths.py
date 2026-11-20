import unittest

from covered_paths import uncovered_paths


class CoverageTest(unittest.TestCase):
    def test_only_changed_paths_without_review_evidence_are_returned(self):
        self.assertEqual(
            uncovered_paths(["b.py", "a.py", "a.py"], ["b.py", "old.py"]),
            ["a.py"],
        )
