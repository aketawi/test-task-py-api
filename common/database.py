import sqlite3


TABLE_SPEC: str = \
"""
CREATE TABLE requests(
    id INTEGER PRIMARY KEY,
    text TEXT,
    status TEXT,
    timestamp TIMESTAMP,
    sentiment TEXT,
    category TEXT
);
"""

def connect() -> sqlite3.Cursor:
    # TODO: check if db exists
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(TABLE_SPEC)
    return cur
