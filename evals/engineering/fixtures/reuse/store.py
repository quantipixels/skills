import sqlite3
from states import AccountState

class Store:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self.db.execute("CREATE TABLE IF NOT EXISTS accounts (id TEXT PRIMARY KEY, state TEXT NOT NULL, cents INTEGER NOT NULL, suspended INTEGER NOT NULL DEFAULT 0)")
    def add(self, key, cents):
        self.db.execute("INSERT INTO accounts VALUES (?, ?, ?, 0)", (key, AccountState.OPEN.value, cents))
        self.db.commit()
    def get(self, key):
        row = self.db.execute("SELECT * FROM accounts WHERE id=?", (key,)).fetchone()
        if row is None: raise KeyError(key)
        return row
    def suspend(self, key, value):
        self.get(key)
        self.db.execute("UPDATE accounts SET suspended=? WHERE id=?", (int(value), key))
        self.db.commit()
    def eligible(self):
        return self.db.execute("SELECT * FROM accounts WHERE state=? AND suspended=0", (AccountState.OPEN.value,)).fetchall()
    def close(self): self.db.close()
