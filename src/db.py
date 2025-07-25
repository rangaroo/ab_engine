import os
import sqlite3

def create_database(name="experiments"):
    DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', f'{name}.db')

    if not os.path.exists(DB_PATH):
        with open(DB_PATH, 'w') as f:
            pass

    return DB_PATH

def insert_data(table_name, data):
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

    # If the rows with experiment_name to be inserted already exist in the database, they will get deleted and replaced with the current data
    rows_to_check = cur.execute("""
        SELECT user_id FROM experiments
        WHERE experiment_name=?;
    """, (table_name, ))

    if rows_to_check.fetchone():
        cur.execute("""
            DELETE FROM experiments
            WHERE experiment_name=?;
        """, (table_name, ))

    cur.executemany(f"INSERT INTO experiments VALUES(?, ?, ?, '{table_name}')", data)
    con.commit()

    # Check what was inserted
    res = cur.execute("""
        SELECT * FROM experiments
        WHERE experiment_name=?;
    """, (table_name, ))
    print(res.fetchall())
