import services

university = services.UniversityManagment("university.db")

while 1:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7):")

    # Створення студента
    if choice == "1":
        university.add_student()

    # Створення курсу
    elif choice == "2":
        university.add_course()

    # Показати список студентів
    elif choice == "3":
        university.show_students()

    # Показати список курсів
    elif choice == "4":
        university.show_courses()

    # Зареєструвати студента на курс
    elif choice == "5":
        university.register_student_on_course()

    # Показати студентів на конкретному курсі
    elif choice == "6":
        university.show_course_students()

    # Вихід з програми
    elif choice == "7":
        break

    # Якщо введено невірна опція
    else:
        continue
