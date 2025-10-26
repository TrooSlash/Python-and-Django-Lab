// Лабораторная работа №7 - Часть 2: Работа с DOM
// Сворачивание/разворачивание статей

document.addEventListener('DOMContentLoaded', function() {
    // Получаем все кнопки с классом fold-button
    var buttons = document.getElementsByClassName("fold-button");
    
    // Добавляем обработчик события для каждой кнопки
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener("click", function(event) {
            var button = event.target;
            var post = button.parentElement;
            
            // Получаем элементы статьи
            var articleText = post.querySelector('.article-text');
            var articleAuthor = post.querySelector('.article-author');
            var articleDate = post.querySelector('.article-created-date');
            
            // Проверяем текущее состояние
            if (post.className.indexOf("folded") !== -1) {
                // Статья свернута - разворачиваем
                post.className = post.className.replace(" folded", "");
                button.innerHTML = "Свернуть";
            } else {
                // Статья развернута - сворачиваем
                post.className = post.className + " folded";
                button.innerHTML = "Развернуть";
            }
        });
    }
});
