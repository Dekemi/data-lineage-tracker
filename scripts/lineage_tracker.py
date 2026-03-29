import sqlite3
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "db")
os.makedirs(db_path, exist_ok=True)

db_file = os.path.join(db_path, "lineage.db")

conn = sqlite3.connect(db_file)

def log_lineage(source, target, transformation):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS lineage (
        source TEXT,
        target TEXT,
        transformation TEXT,
        timestamp TEXT
    )
    """)

    cursor.execute("""
    INSERT INTO lineage VALUES (?, ?, ?, ?)
    """, (source, target, transformation, datetime.now()))

    conn.commit()