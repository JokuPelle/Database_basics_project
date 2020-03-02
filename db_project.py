# Basics of Database Systems Course Project

import sqlite3
from sqlite3 import Error
import sys

create_teachers = """CREATE TABLE IF NOT EXISTS teachers (
    teacherid INT NOT NULL PRIMARY KEY,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL);"""

create_students = """CREATE TABLE IF NOT EXISTS students (
    stid INT NOT NULL PRIMARY KEY,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    major TEXT NOT NULL);"""

create_courses = """CREATE TABLE IF NOT EXISTS courses (
    courseid TEXT NOT NULL PRIMARY KEY,
    teacherid INT references teachers(teacherid) ON UPDATE CASCADE ON DELETE SET NULL,
    name TEXT NOT NULL,
    credits INT NOT NULL,
    description TEXT,
    students INT,
    maxstudents INT);"""

create_attendances = """CREATE TABLE IF NOT EXISTS attendances (
    stid INT NOT NULL references students(stid) ON DELETE CASCADE,
    courseid TEXT NOT NULL references courses(courseid) ON DELETE CASCADE,
    grade INT);"""

# MAIN PROGRAM
try:
    conn = sqlite3.connect("dbproject.db")
    c = conn.cursor()
except Error as e:
    print(e)
    sys.exit()
# drop and create tables
c.execute("DROP TABLE IF EXISTS attendances;")
c.execute("DROP TABLE IF EXISTS courses;")
c.execute("DROP TABLE IF EXISTS students;")
c.execute("DROP TABLE IF EXISTS teachers;")
c.execute(create_teachers)
c.execute(create_students)
c.execute(create_courses)
c.execute(create_attendances)
# add data
c.execute(f"INSERT INTO students VALUES (547392, 'Juuso', 'Pelle', 'Software Engineering');")
c.execute(f"INSERT INTO students VALUES (392392, 'Max', 'Payne', 'Chemical Engineering');")
c.execute(f"INSERT INTO students VALUES (457888, 'Steven', 'Universe', 'Chemical Engineering');")
c.execute(f"INSERT INTO students VALUES (690420, 'Luz', 'Owlhouse', 'Software Engineering');")
c.execute(f"INSERT INTO teachers VALUES (145, 'Steven', 'Armstrong');")
c.execute(f"INSERT INTO teachers VALUES (420, 'Aurora', 'Mage');")
c.execute(f"INSERT INTO teachers VALUES (144, 'Brad', 'Garlinghouse');")
c.execute(f"INSERT INTO teachers VALUES (556, 'Allu', 'Dumle');")
c.execute(f"INSERT INTO courses VALUES ('CT60A4304', 145, 'Database Introduction', 3, 'Introduction to SQL databases', 32, 150);")
c.execute(f"INSERT INTO courses VALUES ('CT60A5530', 556, 'Project Management', 6, 'Course dedicated to project management', 59, 150);")
c.execute(f"INSERT INTO courses VALUES ('BM20A1601', 144, 'Matriisilaskenta', 4, NULL, 144, 200);")
c.execute(f"INSERT INTO courses VALUES ('CT10A7052', 420, 'Software Engineering Work Practise', 3, NULL, 35, 150);")
c.execute(f"INSERT INTO attendances VALUES (547392, 'CT60A4304', 5);")
c.execute(f"INSERT INTO attendances VALUES (547392, 'BM20A1601', NULL);")
c.execute(f"INSERT INTO attendances VALUES (690420, 'CT60A5530', 3);")
c.execute(f"INSERT INTO attendances VALUES (392392, 'CT10A7052', 4);")
c.execute(f"INSERT INTO attendances VALUES (457888, 'BM20A1601', 1);")
# while loop
while True:
    choice = int(input("""Select an option:
    1) SELECT
    2) INSERT
    3) DELETE
    4) UPDATE
    0) Close Program
    Your Choice: """))
    # close program
    if choice == 0:
        break
    # SELECT
    elif choice == 1:
        choice2 = int(input("""Select further option:
        1) Attendances by name (Stid - Name - Course - Grade)
        2) SELECT * FROM students
        3) SELECT * FROM teachers
        4) SELECT * FROM courses
        5) SELECT * FROM attendances
        Your choice: """))
        if choice2 == 1:
            c.execute("SELECT students.stid, students.firstname, students.lastname, courses.name, grade FROM attendances INNER JOIN students ON students.stid = attendances.stid INNER JOIN courses ON courses.courseid = attendances.courseid;")
            for row in c.fetchall():
                print(row)
        elif choice2 > 1 and choice2 < 6:
            table = ["null", "null", "students", "teachers", "courses", "attendances"]
            c.execute(f"SELECT * FROM {table[choice2]};")
            for row in c.fetchall():
                print(row)

    # INSERT
    elif choice == 2:
        choice2 = int(input("""Select further option:
        1) INSERT INTO students
        2) INSERT INTO teachers
        3) INSERT INTO courses
        4) INSERT INTO attendances
        Your choice: """))
        if choice2 == 1:
            stid = int(input("Give stid (int): "))
            fname = input("Give firstname: ")
            lname = input("Give lastname: ")
            major = input("Give major: ")
            c.execute(f"INSERT INTO students VALUES ({stid}, '{fname}', '{lname}', '{major}');")
        elif choice2 == 2:
            teacherid = int(input("Give teacherid (int): "))
            fname = input("Give firstname: ")
            lname = input("Give lastname: ")
            c.execute(f"INSERT INTO teachers VALUES ({stid}, '{fname}', '{lname}');")
        elif choice2 == 3:
            courseid = input("Give courseid: ")
            teacherid = int(input("Give teacherid (int): "))
            name = input("Give name: ")
            credit = int(input("Give credits (int): "))
            description = input("Give description: ")
            students = int(input("Give students (int): "))
            maxstudents = int(input("Give maxstudents (int): "))
            c.execute(f"INSERT INTO courses VALUES ('{courseid}', {teacherid}, '{name}', {credit}, '{description}', {students}, {maxstudents});")
        elif choice2 == 4:
            stid = int(input("Give stid (int): "))
            courseid = input("Give courseid: ")
            grade = int(input("Give grade (int): "))
            c.execute(f"INSERT INTO attendances VALUES ({stid}, '{courseid}', {grade});")

    # DELETE
    elif choice == 3:
        choice2 = int(input("""Choose table:
        1) DELETE FROM students
        2) DELETE FROM teachers
        3) DELETE FROM courses
        4) DELETE FROM attendances
        Your choice: """))
        if choice2 == 1:
            stid = int(input("Give student id to delete: "))
            c.execute(f"DELETE FROM students WHERE stid = {stid};")
        elif choice2 == 2:
            stid = int(input("Give teacher id to delete: "))
            c.execute(f"DELETE FROM teachers WHERE teacherid = {stid};")
        elif choice2 == 3:
            stid = input("Give course id to delete: ")
            c.execute(f"DELETE FROM courses WHERE courseid = '{stid}';")
        elif choice2 == 4:
            stid = int(input("Give student id to delete: "))
            courseid = input("Give course id to delete: ")
            c.execute(f"DELETE FROM courses WHERE courseid = '{courseid}' AND stid = {stid};")

    # UPDATE
    elif choice == 4:
        choice2 = int(input("""Select further option:
        1) UPDATE students
        2) UPDATE teachers
        3) UPDATE courses
        4) UPDATE attendances
        Your choice: """))
        if choice2 == 1:
            stid = int(input("Give stid (int) to update: "))
            c.execute(f"SELECT * FROM students WHERE stid = {stid}")
            print(c.fetchall()[0])
            fname = input("Give firstname: ")
            lname = input("Give lastname: ")
            major = input("Give major: ")
            c.execute(f"UPDATE students SET firstname = '{fname}', lastname = '{lname}', major = '{major}' WHERE stid = {stid};")
        elif choice2 == 2:
            teacherid = int(input("Give teacherid (int) to update: "))
            c.execute(f"SELECT * FROM teachers WHERE teacherid = {teacherid}")
            print(c.fetchall()[0])
            fname = input("Give firstname: ")
            lname = input("Give lastname: ")
            c.execute(f"UPDATE teachers SET firstname = {fname}, lastname = '{lname}' WHERE teacherid = {teacherid};")
        elif choice2 == 3:
            courseid = input("Give courseid to update: ")
            c.execute(f"SELECT * FROM courses WHERE courseid = '{courseid}';")
            print(c.fetchall()[0])
            teacherid = int(input("Give teacherid (int): "))
            name = input("Give name: ")
            credit = int(input("Give credits (int): "))
            description = input("Give description: ")
            students = int(input("Give students (int): "))
            maxstudents = int(input("Give maxstudents (int): "))
            c.execute(f"UPDATE courses SET teacherid = {teacherid}, name = '{name}', credits = {credit}, description = '{description}', students = {students}, maxstudents = {maxstudents} WHERE courseid = '{courseid}';")
        elif choice2 == 4:
            stid = int(input("Give stid (int) to update: "))
            courseid = input("Give courseid to update: ")
            c.execute(f"SELECT * FROM attendances WHERE stid = {stid} AND courseid = '{courseid}';")
            print(c.fetchall()[0])
            grade = int(input("Give grade (int): "))
            c.execute(f"UPDATE attendances SET grade = {grade} WHERE stid = {stid} AND courseid = '{courseid}';")
conn.close()