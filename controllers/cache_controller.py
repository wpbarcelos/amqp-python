# from app import app
# from flask import jsonify, request
# from controllers import send_event

import sqlite3
import json
import os

DB_FILE = os.getenv("DB_FILE", "/.data/database.sqlite")

def get_document_by_id(doc_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        print(f'DOC_ID {doc_id}')
        print(f'SQL: SELECT body FROM cache WHERE id = {str(doc_id)}')
        cursor.execute('SELECT body FROM cache WHERE id = ? ', (str(doc_id),))
        result = cursor.fetchone()
        if result:
            document = json.loads(result[0])
            if 'classificacao' in document and isinstance(document['classificacao'], str):
                document['classificacao'] = json.loads(document['classificacao'])
            return document
        return None
    except Exception as e:
        print(f"Error retrieving from database: {e} {e.line}")
        raise
    finally:
        conn.close()