import sqlite3
import pytest
from src.database import connect_database, create_students_db, create_subjects_db, create_grades_db

@pytest.fixture

def db_connection():
    '''Fixture for database connection and cursor for testing'''
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    yield conn, cursor
    conn.close()

def test_connect_database():
    '''Tests the connect_database function'''
    conn, cursor = connect_database()
    assert conn is not None, "Connection should not be None"
    assert cursor is not None, "Cursor shuld not be None"
    conn.close()

def test_create_students_db(db_connection):
    conn, cursor = db_connection 
    create_students_db(conn, cursor)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name= 'students'")
    result = cursor.fetchone()
    assert result is not None, "Students table should exist"
    assert result[0] == "students", "Table name should be 'students'"

def test_create_subjects_db(db_connection): 
    conn, cursor = db_connection
    create_subjects_db(conn, cursor)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name= 'subjects'")
    result = cursor.fetchone()

    assert result is not None, "Subjects table should exist"
    assert result[0] == "subjects", "Table name should be 'subjects'"

def test_create_grades_db(db_connection):
    conn, cursor = db_connection
    cursor.execute("PRAGMA foreign_keys = ON")

    create_students_db(conn, cursor)
    create_subjects_db(conn, cursor)
    create_grades_db(conn, cursor)

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='grades'")
    result = cursor.fetchone()
    assert result is not None, "Grades table should exist"
    assert result[0] == "grades", "Table name should be 'grades'"
    
    cursor.execute("PRAGMA foreign_key_list('grades')")
    foreign_keys = cursor.fetchall()
    assert len(foreign_keys) == 2, "Grades table should have 2 foreign keys"
    referenced_tables = {fk[2] for fk in foreign_keys}
    assert "students" in referenced_tables, "Grades table should reference students table"
    assert "subjects" in referenced_tables, "Grades table should reference subjects table"
