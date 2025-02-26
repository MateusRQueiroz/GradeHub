import sqlite3


DB_FILE = 'data/GradeHub.db'


def connect_database():
    """
    Connects to the SQLite database and returns the connection and cursor.
    If the connection fails, returns None.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Failed to connect to database: {e}")
        return None, None

def create_students_db(conn, cursor):
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE)''')
        conn.commit()
    except sqlite3.Error as e: 
        print(f'Failed to create students table: {e}')

def create_subjects_db(conn, cursor):
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    subject_name TEXT NOT NULL UNIQUE)''')
        conn.commit()
    except sqlite3.Error as e:
        print(f'Failed to create subjects table: {e}')
    
def create_grades_db(conn, cursor):
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       student_id INTEGER,
                       subject_id INTEGER,
                       score INTEGER CHECK(score BETWEEN 0 AND 100),
                       FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
                       FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE)''')
        conn.commit()
    except sqlite3.Error as e: 
        print(f'Failed to create subjects table: {e}')