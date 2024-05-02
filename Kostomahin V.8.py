import random
import pandas as pd
from datetime import datetime

# Списки возможных фамилий и имен
last_names = ["Иванов", "Петров", "Сидоров", "Смирнов", "Попов", "Соколов", "Лебедев", "Козлов", "Новиков", "Васильев"]
first_names = ["Алексей", "Михаил", "Виктор", "Сергей", "Дмитрий", "Анна", "Мария", "Екатерина", "Ольга", "Татьяна"]

# Создаем примерный список предметов
subjects = ["Математика", "История", "Физика", "Химия", "Литература", "Биология"]

# Функция для создания зачетки для студента
def create_gradebook():
    gradebook = []
    num_subjects = random.randint(3, 5)  # От 3 до 5 предметов
    for _ in range(num_subjects):
        subject = random.choice(subjects)  # Выбираем случайный предмет
        exam_date = datetime(2023, random.randint(1, 12), random.randint(1, 28))  # Случайная дата экзамена в 2023 году
        teacher = f"Преподаватель {random.choice(last_names)} {random.choice(first_names)}"  # Имя преподавателя
        raw_grade = random.randint(0, 10)  # Случайная оценка от 0 до 10
        # Преобразуем оценку в диапазон 0-5
        scaled_grade = (raw_grade / 10) * 5
        gradebook.append({"Предмет": subject, "Дата экзамена": exam_date, "ФИО преподавателя": teacher, "Оценка": scaled_grade})
    return gradebook

# Функция для создания списка студентов
def create_student_list(num_students):
    students = []
    for _ in range(num_students):
        last_name = random.choice(last_names)  # Случайная фамилия
        first_name = random.choice(first_names)  # Случайное имя
        birth_date = datetime(random.randint(1995, 2005), random.randint(1, 12), random.randint(1, 28))  # Случайная дата рождения
        gradebook = create_gradebook()  # Создаем зачетку для студента
        students.append({"ФИО": f"{last_name} {first_name}", "Дата рождения": birth_date, "Зачетка": gradebook})
    return students

# Функция для вывода списка студентов и их среднеарифметических оценок
def print_student_table(students):
    data = []
    for student in students:
        grades = [entry["Оценка"] for entry in student["Зачетка"]]
        average_grade = sum(grades) / len(grades)  # Вычисляем среднее арифметическое
        data.append({"ФИО": student["ФИО"], "Средняя оценка": average_grade})

    # Создаем DataFrame и выводим его в виде таблицы
    df = pd.DataFrame(data)
    print(df)

# Создаем список из 5 студентов
students = create_student_list(5)

# Выводим список студентов вместе с их средними оценками
print_student_table(students)
