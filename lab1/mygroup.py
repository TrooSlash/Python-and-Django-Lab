# -*- coding: utf-8 -*-
# Список студентов группы

groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Мария",
        "surname": "Козлова",
        "exams": ["Математика", "Физика", "Химия"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Дмитрий",
        "surname": "Соколов",
        "exams": ["История", "Литература", "Биология"],
        "marks": [3, 3, 4]
    },
    {
        "name": "Анна",
        "surname": "Морозова",
        "exams": ["Английский", "Математика", "Информатика"],
        "marks": [5, 5, 4]
    },
    {
        "name": "Сергей",
        "surname": "Новиков",
        "exams": ["Физика", "Химия", "Биология"],
        "marks": [3, 4, 3]
    }
]


# Функция для вывода всех студентов в виде таблицы
def print_students(students):
    # Печатаем шапку таблицы
    print("Имя".ljust(15), "Фамилия".ljust(15), "Экзамены".ljust(40), "Оценки".ljust(20))
    print("-" * 90)  # Линия-разделитель
    
    # Проходим по каждому студенту в списке
    for student in students:
        # Выводим данные студента
        print(
            student["name"].ljust(15),
            student["surname"].ljust(15),
            str(student["exams"]).ljust(40),
            str(student["marks"]).ljust(20)
        )
    
    print()  # Пустая строка в конце


# Функция для фильтрации студентов по средней оценке
def filter_by_average(students):
    # Просим пользователя ввести минимальный средний балл
    try:
        min_average = float(input("Введите минимальный средний балл: "))
    except ValueError:
        print("Ошибка! Введите число.")
        return
    
    print(f"\nСтуденты со средним баллом выше {min_average}:\n")
    
    # Переменная для подсчета найденных студентов
    found = False
    
    # Проверяем каждого студента
    for student in students:
        # Считаем средний балл (сумма оценок / количество оценок)
        average = sum(student["marks"]) / len(student["marks"])
        
        # Если средний балл выше заданного
        if average > min_average:
            found = True
            # Выводим информацию о студенте
            print(f"{student['name']} {student['surname']} - средний балл: {average:.2f}")
    
    if not found:
        print("Студентов с таким средним баллом не найдено.")
    
    print()


# Запускаем программу
if __name__ == "__main__":
    print("=== СПИСОК ВСЕХ СТУДЕНТОВ ===\n")
    print_students(groupmates)
    
    print("\n=== ФИЛЬТРАЦИЯ ПО СРЕДНЕМУ БАЛЛУ ===\n")
    filter_by_average(groupmates)
