import os
import sqlite3

def create_database(name="experiments"):
    DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', f'{name}.db')

    if os.path.exists(DB_PATH):
        print("File already exists")
        return
    else:
        print("Creating a file")
        with open(DB_PATH, 'w') as f:
            pass

create_database()
