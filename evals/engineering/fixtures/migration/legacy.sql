PRAGMA foreign_keys = ON;
CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    login TEXT UNIQUE NOT NULL,
    display_name TEXT NOT NULL
);
CREATE TABLE projects (
    id INTEGER PRIMARY KEY,
    slug TEXT UNIQUE NOT NULL
);
CREATE TABLE project_members (
    project_id INTEGER NOT NULL REFERENCES projects(id),
    account_id INTEGER NOT NULL REFERENCES accounts(id),
    role TEXT NOT NULL,
    PRIMARY KEY (project_id, account_id)
);
INSERT INTO accounts(id, login, display_name) VALUES
    (42, 'amy', 'Amy A.'),
    (105, 'li', 'Li N.'),
    (7, 'zoe', 'Zoe R.');
INSERT INTO projects(id, slug) VALUES
    (20, 'billing'),
    (4, 'search');
INSERT INTO project_members(project_id, account_id, role) VALUES
    (20, 7, 'owner'),
    (20, 42, 'reviewer'),
    (4, 105, 'owner');
PRAGMA user_version = 1;
