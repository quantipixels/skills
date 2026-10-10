import sqlite3
from uuid import uuid4

class Settlement:
    def __init__(self, path, provider):
        self.db = sqlite3.connect(path)
        self.db.execute("CREATE TABLE IF NOT EXISTS completed (settlement_id TEXT PRIMARY KEY, cents INTEGER NOT NULL, transfer_id INTEGER NOT NULL)")
        self.provider = provider

    def settle(self, settlement_id, cents):
        prior = self.db.execute("SELECT transfer_id FROM completed WHERE settlement_id = ?", (settlement_id,)).fetchone()
        if prior:
            return prior[0]
        transfer_id = self.provider.transfer(str(uuid4()), cents)
        self.db.execute("INSERT INTO completed VALUES (?, ?, ?)", (settlement_id, cents, transfer_id))
        self.db.commit()
        return transfer_id

    def close(self):
        self.db.close()
