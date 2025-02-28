import sqlite3

def insert_student(conn, cursor, first_name, last_name, email):
    if not first_name.strip() or not last_name.strip():
        print('First name and last name cannot be empty')
        return
    try:
        cursor.execute('''INSERT INTO students (first_name, last_name, email)
                    VALUES (?, ?, ?)''',
                    (first_name, last_name, email))
        conn.commit()
    except sqlite3.Error as e:
        print(f'Unable to insert student {e}')
    
def remove_student(conn, cursor, student_id):
    if student_id is None:
        print('Student id cannot be none')
        return
    try:
        cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f'Unable to remove student {e}')
    
def insert_subject(conn, cursor, subject_name): 
    if not subject_name.strip():
        print('Subject name cannot be empty')
        return
    try:
        cursor.execute('''INSERT INTO subjects (subject_name) VALUES (?)''',
                    (subject_name,))
        conn.commit()
    except sqlite3.Error as e:
        print(f'Unable to insert subject {e}')

def remove_subject(conn, cursor, subject_name):
    if subject_name is None: 
        print('Subject name cannot be none')
    try:
        cursor.execute('DELETE FROM subjects WHERE subject_name = ?', (subject_name,))
        conn.commit()
    except sqlite3.Error as e:
        print(f'Unable to remove subject {e}')

def insert_grade(conn, cursor, student_id, subject_name, score):
    if student_id is None or subject_name == '' or score is None:
        print('Student id, subject name, and the score cannot be empty')
        return
    try: 
        cursor.execute('''SELECT id FROM subjects WHERE subject_name = ?''',
                       (subject_name,)) 
        subject_id_result = cursor.fetchone()
        
        if subject_id_result is None:
            print(f"Subject '{subject_name}' does not exist.")
            return
        
        subject_id = subject_id_result[0]
        cursor.execute('''INSERT INTO grades (student_id, subject_id, score) VALUES (?, ?, ?)''',
                    (student_id, subject_id, score))
        conn.commit()
    except sqlite3.Error as e:
        print(f'Unable to insert grade: {e}')

def remove_grade(conn, cursor, student_id, subject_name):
    if not student_id or not subject_name:
        print("Student ID and subject name cannot be empty.")
        return
    try:
        cursor.execute('''
            DELETE FROM grades
            WHERE student_id = ?
            AND subject_id = (SELECT id FROM subjects WHERE subject_name = ?)
        ''', (student_id, subject_name))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error removing grade: {e}")
