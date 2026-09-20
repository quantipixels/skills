import sqlite3


def migrate(path):
    database = sqlite3.connect(path)
    try:
        version = database.execute("PRAGMA user_version").fetchone()[0]
        if version == 2:
            return
        if version != 1:
            raise ValueError(f"unsupported schema version: {version}")
        members = database.execute(
            "SELECT project_id, role FROM project_members ORDER BY project_id, account_id"
        ).fetchall()
        logins = [row[0] for row in database.execute("SELECT login FROM accounts ORDER BY login")]
        database.execute("ALTER TABLE project_members RENAME TO project_members_legacy")
        database.execute(
            "CREATE TABLE project_members ("
            "project_id INTEGER NOT NULL REFERENCES projects(id), "
            "account_login TEXT NOT NULL REFERENCES accounts(login), "
            "role TEXT NOT NULL, PRIMARY KEY (project_id, account_login))"
        )
        for (project_id, role), login in zip(members, logins):
            database.execute(
                "INSERT INTO project_members(project_id, account_login, role) VALUES (?, ?, ?)",
                (project_id, login, role),
            )
        database.execute("DROP TABLE project_members_legacy")
        database.execute("PRAGMA user_version = 2")
        database.commit()
    finally:
        database.close()
