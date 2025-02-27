import sqlite3

def create_student(conn, cursor, first_name, last_name, email):
    cursor.execute('''INSERT INTO students (first_name, last_name, email)
                   VALUES (?, ?, ?)''',
                   (first_name, last_name, email))
    conn.commit()
    
def remove_student(conn, cursor, student_id):
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    
def create_subject(conn, cursor, subject_name): 
    cursor.execute('''INSERT INTO subjects (subject_name) VALUES (?)''',
                   (subject_name,))
    conn.commit()

def remove_subject(conn, cursor, subject_id):
    cursor.execute('DELETE FROM subjects WHERE id = ?', (subject_id,))
    conn.commit()

def create_grade(conn, cursor, student_id, subject_id, score):
    cursor.execute('''INSERT INTO grades (student_id, subject_id, score) VALUES (?, ?, ?)''',
                   (student_id, subject_id, score))
    conn.commit()

def remove_grade(conn, cursor, grade_id):
    cursor.execute('DELETE FROM grades WHERE id = ?', (grade_id,))
    conn.commit()