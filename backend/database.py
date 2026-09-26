import sqlite3
import os 
DB_PATH = os.path.join(os.path.dirname(__file__),"watchlist.db")

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    connection = get_connection()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL, 
        type TEXT NOT NULL CHECK(type IN ('movie','game','book')),
        rating INTEGER NOT NULL,
        note text
        )
        """)
    connection.commit()
    connection.close()