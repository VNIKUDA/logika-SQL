import sqlite3

# підключення до бази даних (створення або відкриття
conn = sqlite3.connect('university.db')

# створення курсора для виконання SQL-запитів
cursor = conn.cursor()

# створення таблиці students
cursor.execute("""CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    major TEXT
)""")

# створення таблиці courses
cursor.execute("""CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    instructor INTEGER
)""")

# створення таблиці students_courses
cursor.execute("""CREATE TABLE IF NOT EXISTS students_courses (
    student_id INTEGER,
    course_id INTEGER,
    grade INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
    PRIMARY KEY (student_id, course_id)
)""")

conn.commit()  # збереження змін
conn.close()  # закриття з'єднання з базою даних

print("Tables created successfully")
