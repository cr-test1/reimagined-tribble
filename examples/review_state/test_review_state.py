import unittest

from review_state import review_state


class ReviewStateTest(unittest.TestCase):
    def test_completed_reviews_follow_the_head(self):
        self.assertEqual(review_state("abc", "completed", "abc"), "current")
        self.assertEqual(review_state("def", "completed", "abc"), "stale")

    def test_incomplete_observations_remain_unknown(self):
        self.assertEqual(review_state("abc", "reviewing", "abc"), "unknown")
        self.assertEqual(review_state("abc", "completed", None), "unknown")
