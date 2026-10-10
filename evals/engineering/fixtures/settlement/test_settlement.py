import tempfile
import unittest
from pathlib import Path
from provider import Provider
from settlement import Settlement

class SettlementTest(unittest.TestCase):
    def test_repeat(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            provider = Provider(root / 'provider.db')
            service = Settlement(root / 'service.db', provider)
            first = service.settle('settlement-S3', 3500)
            self.assertEqual(first, service.settle('settlement-S3', 3500))
            service.close()
            provider.close()
