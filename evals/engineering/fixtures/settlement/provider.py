import sqlite3

class LostReply(TimeoutError):
    pass

class Provider:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.db.execute("CREATE TABLE IF NOT EXISTS transfers (id INTEGER PRIMARY KEY, request_key TEXT UNIQUE NOT NULL, cents INTEGER NOT NULL)")
        self.drop_next_reply = False

    def transfer(self, request_key, cents):
        prior = self.db.execute("SELECT id, cents FROM transfers WHERE request_key = ?", (request_key,)).fetchone()
        if prior:
            if prior[1] != cents:
                raise ValueError('request key reused with different amount')
            return prior[0]
        cur = self.db.execute("INSERT INTO transfers(request_key, cents) VALUES (?, ?)", (request_key, cents))
        self.db.commit()
        if self.drop_next_reply:
            self.drop_next_reply = False
            raise LostReply('reply lost')
        return cur.lastrowid

    def close(self):
        self.db.close()
