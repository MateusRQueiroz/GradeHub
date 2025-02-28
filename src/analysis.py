import pandas as pd

def fetch_student_rankings(conn):
    query = '''SELECT students.id AS students_id,
                students.first_name, 
                students.last_name,
                subjects.subject_name,
                grades.score AS average_grade
            FROM grades
            JOIN students ON grades.student_id = students.id
            JOIN subjects ON grades.subject_id = subjects.id'''

    df = pd.read_sql_query(query, conn)
    avg_grade = df.groupby(['students_id', 'first_name', 'last_name'])['average_grade'].mean().reset_index()
    avg_grade = avg_grade.sort_values(by='average_grade', ascending=False).reset_index(drop=True)
    return avg_grade 

def fetch_students(conn):
    query = '''SELECT students.id as student_id,
                        students.first_name,
                        students.last_name,
                        students.email
                    FROM students'''
    df = pd.read_sql_query(query,conn)
    return df

def fetch_subject_averages(conn):
    query = '''SELECT subjects.id as subject_id,
                subjects.subject_name,
                grades.score AS average 
                FROM grades
                JOIN subjects ON grades.subject_id = subjects.id'''
    df = pd.read_sql_query(query, conn)
    subjects_avg_grade = df.groupby(['subject_id', 'subject_name'])['average'].mean().reset_index()
    subjects_avg_grade = subjects_avg_grade.sort_values(by='average', ascending=False).reset_index(drop=True)
    return subjects_avg_grade

def fetch_report_card(conn, student_id):
    query = '''SELECT 
                subjects.id AS subject_id,
                subjects.subject_name,
                grades.score AS grade
            FROM grades
            JOIN students ON grades.student_id = students.id
            JOIN subjects ON grades.subject_id = subjects.id
            WHERE students.id = ?'''
    
    df = pd.read_sql_query(query, conn, params=(student_id,))
    sorted_report_card = df.sort_values(by='grade', ascending=False).reset_index(drop=True)
    return sorted_report_card

