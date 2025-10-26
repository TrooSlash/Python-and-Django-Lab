// Лабораторная работа №7 - Часть 1: Основы JavaScript

// Массив студентов группы
var groupmates = [
    {
        name: "Иван",
        surname: "Иванов",
        group: "ИС-101",
        marks: [5, 4, 5, 5, 4]
    },
    {
        name: "Петр",
        surname: "Петров",
        group: "ИС-101",
        marks: [4, 4, 3, 4, 5]
    },
    {
        name: "Сидор",
        surname: "Сидоров",
        group: "ИС-102",
        marks: [3, 3, 4, 3, 4]
    },
    {
        name: "Мария",
        surname: "Смирнова",
        group: "ИС-101",
        marks: [5, 5, 5, 5, 5]
    },
    {
        name: "Анна",
        surname: "Козлова",
        group: "ИС-102",
        marks: [4, 5, 4, 5, 4]
    }
];

// Функция для дополнения строки пробелами справа
function rpad(str, length) {
    while (str.length < length) {
        str = str + " ";
    }
    return str;
}

// Функция для вывода списка студентов
function printStudents(students) {
    console.log(rpad("Имя", 15) + rpad("Фамилия", 15) + rpad("Группа", 10) + "Оценки");
    console.log("=".repeat(60));
    
    for (var i = 0; i < students.length; i++) {
        var student = students[i];
        var line = rpad(student.name, 15) + 
                   rpad(student.surname, 15) + 
                   rpad(student.group, 10) + 
                   student.marks.join(", ");
        console.log(line);
    }
}

// Вывод всех студентов
console.log("Список всех студентов группы:");
console.log(groupmates);
console.log("\nФорматированный вывод:");
printStudents(groupmates);
