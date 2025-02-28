import sqlite3
import pandas as pd
from database import create_grades_db, create_students_db, create_subjects_db, connect_database
from data_operations import insert_grade, insert_student, insert_subject, remove_grade, remove_student,remove_subject
from tabulate import tabulate
from analysis import fetch_report_card, fetch_student_rankings, fetch_subject_averages, fetch_students

DB_FILE = 'data/GradeHub.db'

def display_menu():
    print("\n--- GradeHub Menu ---")
    print("1. Insert Student")
    print("2. Remove Student")
    print("3. Insert Subject")
    print("4. Remove Subject")
    print("5. Insert Grade")
    print("6. Remove Grade")
    print("7. View Students")
    print("8. Fetch Student Rankings")
    print("9. Fetch Subject Averages")
    print("10. Fetch Report Card for a Student")
    print("11. Exit")

def main():
    conn, cursor = connect_database()
    if conn is None or cursor is None:
        return

    create_students_db(conn, cursor)
    create_subjects_db(conn, cursor)
    create_grades_db(conn, cursor)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1': 
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            insert_student(conn, cursor, first_name, last_name, email)

        elif choice == '2': 
            student_id = input("Enter student ID to remove: ")
            if student_id.isdigit():
                remove_student(conn, cursor, int(student_id))
            else:
                print("Invalid student ID. Please enter a number.")

        elif choice == '3':
            subject_name = input("Enter subject name: ")
            insert_subject(conn, cursor, subject_name)

        elif choice == '4': 
            subject_name = input("Enter subject name to remove: ")
            remove_subject(conn, cursor, str(subject_name))

        elif choice == '5': 
            student_id = input("Enter student ID: ")
            subject_name = input("Enter subject name: ")
            score = input("Enter score (0-100): ")
            if student_id.isdigit() and score.isdigit():
                insert_grade(conn, cursor, int(student_id), str(subject_name), int(score))
            else:
                print("Invalid input. Please enter numbers for ID and score.")

        elif choice == '6': 
            student_id = input("Enter student ID: ")
            subject_name = input("Enter subject name: ")
            remove_grade(conn, cursor, int(student_id), str(subject_name))
        
        elif choice == '7':
            students_list = fetch_students(conn)
            print(tabulate(students_list, headers='keys', tablefmt = 'simple', showindex='never'))

        elif choice == '8': 
            rankings = fetch_student_rankings(conn)
            print("\nStudent Rankings:\n")
            print(tabulate(rankings, headers='keys', tablefmt = 'simple', showindex='never'))

        elif choice == '9':  
            averages = fetch_subject_averages(conn)
            print("\nSubject Averages:\n")
            print(tabulate(averages, headers='keys', tablefmt = 'simple', showindex="never"))

        elif choice == '10': 
            student_id = input("Enter student ID: ")
            if student_id.isdigit():
                report_card = fetch_report_card(conn, int(student_id))
                print("\nReport Card:\n")
                print(tabulate(report_card, headers='keys', tablefmt = "simple", showindex="never"))
            else:
                print("Invalid student ID. Please enter a number.")

        elif choice == '11':  
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()