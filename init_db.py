import os
from dotenv import load_dotenv
import sqlite3
load_dotenv()


DB_FILE = os.getenv("DB_FILE", "./data/database.sqlite")

def init_db():
    """ Initialize database and create table if not exists"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cache (
            id TEXT PRIMARY KEY,
            body TEXT,
            context TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

    print(' ! Banco de dados inicializado')
