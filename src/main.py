import sqlite3

db_file = 'GradeHub.db'

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON;")

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               first_name TEXT NOT NULL,
               last_name TEXT NOT NULL, 
               email TEXT NOT NULL UNIQUE)
               ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               subject_name TEXT NOT NULL UNIQUE)
               ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               student_id INTEGER,
               subject_id INTEGER,
               score INTEGER CHECK(score BETWEEN 0 AND 100),
               FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
               FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
               )''')

conn.commit()
conn.close()
