import unittest
from ledger import record


class ReplayContract(unittest.TestCase):
    def test_conflicting_replay_preserves_state(self):
        entries = {'first': 10, 'second': 20}
        before = dict(entries)
        with self.assertRaises(ValueError):
            record(entries, 'first', 99)
        self.assertEqual(entries, before)
