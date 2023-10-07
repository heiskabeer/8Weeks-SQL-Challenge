import sqlite3


def create_connection():

    with open('schema.sql', 'r') as f:
        script = f.read()

    conn = sqlite3.connect("danny.db")
    cursor = conn.cursor()
    cursor.executescript(script)
    conn.commit()
    conn.close()



if __name__ == '__main__':
    create_connection()

