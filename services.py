import sqlite3

class UniversityManagment():
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def add_student(self):
        name = input("Ім'я: ")
        age = input("Вік: ")
        major = input("Магістратура: ")

        self.cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)", [name, age, major])
        self.conn.commit()

        print("Студента додано")

    def add_course(self):
        course_name = input("Ім'я курсу: ")
        instructor = input("Іструктор: ")

        self.cursor.execute("INSERT INTO courses (course_name, instructor) VALUES (?, ?)", [course_name, instructor])
        self.conn.commit()

        print("Курс додано")

    def show_students(self):
        self.cursor.execute("SELECT * FROM students")
        students = self.cursor.fetchall()

        for student in students:
            print(student)
    
    def show_courses(self):
        self.cursor.execute("SELECT * FROM courses")
        courses = self.cursor.fetchall()

        for course in courses:
            print(course)

    def register_student_on_course(self):
        course_id = input("ID курса: ")
        student_id = input("ID студента: ")

        self.cursor.execute("INSERT INTO students_courses (course_id, student_id) VALUES (?, ?)", [course_id, student_id])
        self.conn.commit()

    def show_course_students(self):
        course_id = input("ID курса: ")

        self.cursor.execute("SELECT * FROM students_courses WHERE course_id == ?", [course_id])
        students_ids = self.cursor.fetchall()

        for student_id in students_ids:
            self.cursor.execute("SELECT * FROM students WHERE id == ?", [student_id])
            print(self.cursor.fetchall()[0])
