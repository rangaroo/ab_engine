import os
import sqlite3

def create_database(name="experiments"):
    DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', f'{name}.db')

    if not os.path.exists(DB_PATH):
        with open(DB_PATH, 'w') as f:
            pass

    return DB_PATH

def insert_experiment(name, data):
    DB_PATH = create_database()

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS experiments (
            user_id INTEGER PRIMARY KEY,
            user_group TEXT,
            converted INTEGER,
            experiment_name TEXT
        );
        """)

    cur.executemany(f"INSERT INTO experiments VALUES(?, ?, ?, '{name}')", data)
    con.commit()

    res = cur.execute("SELECT * FROM experiments")
    res.fetchall()
