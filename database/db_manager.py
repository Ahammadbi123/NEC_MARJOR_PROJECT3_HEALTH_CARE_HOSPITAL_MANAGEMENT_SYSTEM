import sqlite3

DB_NAME = "healthcare.db"

def create_connection():
    return sqlite3.connect(DB_NAME)

def create_users_table():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def add_user(name,email,password,role):

    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO users
        (name,email,password,role)
        VALUES(?,?,?,?)
        """,(name,email,password,role))

        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()

def get_user(email):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    return user
