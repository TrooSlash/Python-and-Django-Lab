/**
 * Лабораторная работа №7 - Часть 2: Работа с DOM
 * 
 * Этот скрипт добавляет интерактивность на страницу -
 * кнопки для сворачивания и разворачивания статей.
 * 
 * DOM (Document Object Model) - это представление HTML страницы как дерева объектов.
 * JavaScript может изменять DOM, и страница будет обновляться.
 */

// DOMContentLoaded срабатывает когда HTML страница полностью загружена
// Это нужно чтобы скрипт выполнился после того как все элементы появились на странице
document.addEventListener('DOMContentLoaded', function() {
    
    // Получаем все кнопки с классом "fold-button"
    // getElementsByClassName возвращает коллекцию (похоже на массив) всех элементов с этим классом
    var buttons = document.getElementsByClassName("fold-button");
    
    // Проходим по всем кнопкам и добавляем обработчик клика
    for (var i = 0; i < buttons.length; i++) {
        
        // addEventListener добавляет функцию которая вызовется при клике
        buttons[i].addEventListener("click", function(event) {
            
            // event.target - это элемент на который кликнули (кнопка)
            var button = event.target;
            
            // parentElement - родительский элемент (div со статьей)
            var post = button.parentElement;
            
            // Проверяем, есть ли у статьи класс "folded" (свернута)
            // indexOf возвращает -1 если подстрока не найдена
            if (post.className.indexOf("folded") !== -1) {
                // Статья свернута - нужно развернуть
                // Убираем класс "folded" из списка классов
                post.className = post.className.replace(" folded", "");
                // Меняем текст кнопки
                button.innerHTML = "Свернуть";
            } else {
                // Статья развернута - нужно свернуть
                // Добавляем класс "folded"
                post.className = post.className + " folded";
                // Меняем текст кнопки
                button.innerHTML = "Развернуть";
            }
        });
    }
});
