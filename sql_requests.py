import sqlite3

database = "university.db"
conn = None
cursor = None

# Відкриття та закриття бази даних
def open():
    global conn, cursor
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

def close():
    global conn, cursor
    cursor.close()
    conn.close()

# Виконнання SQL-запитів
def do(query, *values):
    cursor.execute(query, values)
    conn.commit()

# Підготовка бази даних для роботи
def setup():
    open()
    do("""CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            major TEXT
        )""")
       
    do("""CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY,
            course_name TEXT,
            instructor TEXT
       )""")

    do("""CREATE TABLE IF NOT EXISTS students_courses (
            student_id INTEGER,
            course_id INTEGER,
       
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (course_id) REFERENCES courses(course_id),
       
            PRIMARY KEY (student_id, course_id)
       )""")
    
    close()


# Робота з базою даних:
# Стоврення нового студента
def create_student(name, age, major):
    # cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)", [name, age, major])
    # conn.commit()
    open()
    do("INSERT INTO students (name, age, major) VALUES (?, ?, ?)", name, age, major)
    close()

def create_course(course_name, instructor):
    open()
    do("INSERT INTO courses (course_name, instructor) VALUES (?, ?)", course_name, instructor)
    close()

