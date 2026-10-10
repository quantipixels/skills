import tempfile
import unittest
from pathlib import Path
from store import Store
from collections_service import Collections
from api import dispatch
from admin import set_collection_hold

class AccountsTest(unittest.TestCase):
    def test_existing_admin_hold(self):
        with tempfile.TemporaryDirectory() as root:
            store = Store(Path(root)/"db")
            try:
                store.add("a", 1250)
                service = Collections(store)
                set_collection_hold(service, "a", True)
                self.assertEqual([], store.eligible())
                self.assertEqual({"id":"a", "status":"Open", "cents":1250}, dispatch(service, "show", "a"))
            finally: store.close()
