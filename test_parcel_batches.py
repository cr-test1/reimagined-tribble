import unittest

from parcel_batches import dispatch_batches


class DispatchBatchesTest(unittest.TestCase):
    def test_empty_dispatch(self):
        self.assertEqual(dispatch_batches(0, 12), 0)

    def test_partial_final_batch(self):
        self.assertEqual(dispatch_batches(25, 12), 3)

    def test_full_final_batch(self):
        self.assertEqual(dispatch_batches(24, 12), 2)
