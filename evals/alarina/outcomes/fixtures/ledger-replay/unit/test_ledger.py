import unittest
from ledger import record


class LedgerTest(unittest.TestCase):
    def test_distinct_events(self):
        entries = {}
        self.assertEqual(record(entries, 'first', 10), 10)
        self.assertEqual(record(entries, 'second', 20), 30)

    def test_exact_replay(self):
        entries = {'first': 10}
        self.assertEqual(record(entries, 'first', 10), 10)
        self.assertEqual(entries, {'first': 10})
