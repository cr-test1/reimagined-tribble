import unittest

from parcel_racks import racks_needed


class ParcelRackTests(unittest.TestCase):
    def test_counts_full_and_partial_racks(self):
        self.assertEqual(racks_needed(0), 0)
        self.assertEqual(racks_needed(8), 1)
        self.assertEqual(racks_needed(9), 2)

    def test_rejects_negative_counts(self):
        with self.assertRaises(ValueError):
            racks_needed(-1)
