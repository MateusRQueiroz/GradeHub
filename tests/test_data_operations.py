import sqlite3 
import pytest 
from src.data_operations import insert_student, remove_student, insert_subject, remove_subject, insert_grade, remove_grade
from src.database import create_grades_db, create_students_db, create_subjects_db

@pytest.fixture

def db_connection():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    create_students_db(conn, cursor)
    create_subjects_db(conn, cursor)
    create_grades_db(conn, cursor)
    yield conn, cursor
    conn.close()

def test_insert_student_empty(db_connection):
    conn, cursor = db_connection
    insert_student(conn, cursor, "", "", "")
    cursor.execute('SELECT COUNT(*) FROM students')
    result = cursor.fetchone()
    assert result[0] == 0, "No student should be inserted"

def test_insert_student(db_connection): 
    conn, cursor = db_connection
    insert_student(conn, cursor, "James", "Smith", "James@gmail.com")
    cursor.execute('''SELECT first_name, last_name, email FROM students WHERE first_name = ? AND last_name = ?''',
                   ("James", "Smith"))
    result = cursor.fetchone()
    assert result is not None, "Student should be inserted"
    assert result[0] == "James", "First name should be 'James'"
    assert result[1] == "Smith", "Last name should be 'Smith'"
    assert result[2] == "James@gmail.com"

def test_remove_student_empty(db_connection):
    conn, cursor = db_connection 
    insert_student(conn, cursor, "James", "Smith", "James@gmail.com")
    remove_student(conn, cursor, None)
    cursor.execute('''SELECT COUNT(*) FROM students''')
    result = cursor.fetchone()
    assert result[0] == 1, "No student should be removed"

def test_remove_student(db_connection):
    conn, cursor = db_connection
    insert_student(conn, cursor, "James", "Smith", "James@gmail.com")
    remove_student(conn, cursor, 1)
    cursor.execute('''SELECT COUNT(*) FROM students''')
    result = cursor.fetchone()
    assert result[0] == 0, "Student should be removed"

def test_insert_subject_empty(db_connection):
    conn, cursor = db_connection
    insert_subject(conn, cursor, "") 
    cursor.execute('''SELECT COUNT(*) FROM subjects''')
    result = cursor.fetchone()
    assert result[0] == 0, "Subject should not be inserted"

def test_insert_subject(db_connection): 
    conn, cursor = db_connection
    insert_subject(conn, cursor, "Math")
    cursor.execute('''SELECT subject_name FROM subjects WHERE subject_name = ?''',
                   ("Math",))
    result = cursor.fetchone()
    assert result is not None, "Subject should be inserted"
    assert result[0] == "Math", "Subject name should be 'Math'"

def test_remove_subject_empty(db_connection):
    conn, cursor = db_connection
    insert_subject(conn, cursor, "Math")
    remove_subject(conn, cursor, None)
    cursor.execute('''SELECT COUNT(*) FROM subjects''')
    result = cursor.fetchone()
    assert result[0] == 1, "Subject should not be removed"

def test_remove_subject(db_connection):
    conn, cursor = db_connection 
    insert_subject(conn, cursor, "Math")
    remove_subject(conn, cursor, 1)
    cursor.execute('''SELECT COUNT(*) FROM subjects''')
    result = cursor.fetchone()
    assert result[0] == 0, "Subject should be removed"

def test_insert_grade_empty(db_connection): 
    conn, cursor = db_connection
    cursor.execute("PRAGMA foreign_keys = ON")
    insert_student(conn, cursor, "James", "Smith", "James@gmail.com")
    insert_subject(conn, cursor, "Math")
    insert_grade(conn, cursor, None, None, None)
    cursor.execute('''SELECT COUNT(*) FROM grades''')
    result = cursor.fetchone()
    assert result[0] == 0, "Grade should not be inserted"

def test_insert_grade(db_connection):
    conn, cursor = db_connection
    cursor.execute("PRAGMA foreign_keys = ON")
    insert_student(conn, cursor, "James", "Smith", "James@gmail.com")
    insert_subject(conn, cursor, "Math")

    cursor.execute('''SELECT id FROM students WHERE first_name = ?''',
                   ("James",))
    student_id = cursor.fetchone()[0]
    cursor.execute('''SELECT id FROM subjects WHERE subject_name = ?''',
                   ("Math",))
    subject_id = cursor.fetchone()[0]

    insert_grade(conn, cursor, student_id, subject_id, 100)
    cursor.execute('''SELECT score FROM grades WHERE id = ?''',
                   (1,))
    result = cursor.fetchone()
    assert result is not None, "Grade should be inserted"
    assert result[0] == 100, "Grade should be '100'"


def test_insert_grade_over(db_connection):
    conn, cursor = db_connection
    cursor.execute("PRAGMA foreign_keys = ON")
    insert_student(conn, cursor, "James", "Smith", "James@gmail.com")
    insert_subject(conn, cursor, "Math")

    cursor.execute('''SELECT id FROM students WHERE first_name = ?''',
                   ("James",))
    student_id = cursor.fetchone()[0]
    cursor.execute('''SELECT id FROM subjects WHERE subject_name = ?''',
                   ("Math",))
    subject_id = cursor.fetchone()[0]

    insert_grade(conn, cursor, student_id, subject_id, 105)
    cursor.execute('''SELECT COUNT(*) FROM grades''')
    result = cursor.fetchone()
    assert result[0] == 0, "Grade should not be inserted"

def test_insert_grade_under(db_connection):
    conn, cursor = db_connection
    cursor.execute("PRAGMA foreign_keys = ON")
    insert_student(conn, cursor, "James", "Smith", "James@gmail.com")
    insert_subject(conn, cursor, "Math")

    cursor.execute('''SELECT id FROM students WHERE first_name = ?''',
                   ("James",))
    student_id = cursor.fetchone()[0]
    cursor.execute('''SELECT id FROM subjects WHERE subject_name = ?''',
                   ("Math",))
    subject_id = cursor.fetchone()[0]

    insert_grade(conn, cursor, student_id, subject_id, -5)
    cursor.execute('''SELECT COUNT(*) FROM grades''')
    result = cursor.fetchone()
    assert result[0] == 0, "Grade should not be inserted"

def test_remove_grade_empty(db_connection):
    conn, cursor = db_connection
    cursor.execute("PRAGMA foreign_keys = ON")
    insert_student(conn, cursor, "James", "Smith", "James@gmail.com")
    insert_subject(conn, cursor, "Math")

    cursor.execute('''SELECT id FROM students WHERE first_name = ?''',
                   ("James",))
    student_id = cursor.fetchone()[0]
    cursor.execute('''SELECT id FROM subjects WHERE subject_name = ?''',
                   ("Math",))
    subject_id = cursor.fetchone()[0]

    insert_grade(conn, cursor, student_id, subject_id, 50)
    remove_grade(conn, cursor, None)
    cursor.execute('''SELECT COUNT(*) FROM grades''')
    result = cursor.fetchone()
    assert result[0] == 1

def test_remove_grade(db_connection):
    conn, cursor = db_connection
    cursor.execute("PRAGMA foreign_keys = ON")
    insert_student(conn, cursor, "James", "Smith", "James@gmail.com")
    insert_subject(conn, cursor, "Math")

    cursor.execute('''SELECT id FROM students WHERE first_name = ?''',
                   ("James",))
    student_id = cursor.fetchone()[0]
    cursor.execute('''SELECT id FROM subjects WHERE subject_name = ?''',
                   ("Math",))
    subject_id = cursor.fetchone()[0]

    insert_grade(conn, cursor, student_id, subject_id, 50)
    remove_grade(conn, cursor, 1)
    cursor.execute('''SELECT COUNT(*) FROM grades''')
    result = cursor.fetchone()
    assert result[0] == 0
