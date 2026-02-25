# database.py

import sqlite3
from datetime import datetime

DB_NAME = "analysis.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT,
        result TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_analysis(query, result):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO analysis (query, result, created_at)
    VALUES (?, ?, ?)
    """, (query, result, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()
    conn.close()