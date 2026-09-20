import unittest
from batching import chunks

class ChunksTest(unittest.TestCase):
    def test_exact_batches(self):
        self.assertEqual([[1, 2], [3, 4]], chunks([1, 2, 3, 4], 2))

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            chunks([1], 0)
