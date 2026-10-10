import sqlite3
import tempfile
import unittest
from pathlib import Path

from migration import migrate


class MigrationTest(unittest.TestCase):
    def test_empty_version_one_database_migrates_and_reopens(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "empty.db"
            with sqlite3.connect(path) as database:
                database.executescript(
                    "CREATE TABLE accounts (id INTEGER PRIMARY KEY, login TEXT UNIQUE NOT NULL, display_name TEXT NOT NULL);"
                    "CREATE TABLE projects (id INTEGER PRIMARY KEY, slug TEXT UNIQUE NOT NULL);"
                    "CREATE TABLE project_members (project_id INTEGER NOT NULL, account_id INTEGER NOT NULL, role TEXT NOT NULL, PRIMARY KEY(project_id, account_id));"
                    "PRAGMA user_version = 1;"
                )
            migrate(path)
            migrate(path)
            with sqlite3.connect(path) as database:
                self.assertEqual(2, database.execute("PRAGMA user_version").fetchone()[0])
                self.assertEqual([], database.execute("SELECT * FROM project_members").fetchall())
