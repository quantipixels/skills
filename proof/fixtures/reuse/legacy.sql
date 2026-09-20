CREATE TABLE accounts (id TEXT PRIMARY KEY, state TEXT NOT NULL, cents INTEGER NOT NULL, suspended INTEGER NOT NULL DEFAULT 0);
INSERT INTO accounts VALUES ('legacy', 'O', 3700, 1);
INSERT INTO accounts VALUES ('closed', 'C', 1900, 0);
