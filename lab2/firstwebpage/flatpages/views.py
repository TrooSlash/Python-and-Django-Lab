"""
Лабораторная работа №2-4 - Представления (Views)

Представления в Django - это функции которые обрабатывают HTTP-запросы.
Когда пользователь заходит на страницу, Django вызывает соответствующее
представление и возвращает ответ (обычно HTML страницу).
"""

from django.shortcuts import render
from django.http import HttpResponse
from django import template


def home(request):
    """
    Главная страница сайта.
    
    Параметры:
        request - объект HTTP запроса, содержит информацию о пользователе,
                  его браузере, cookies и т.д.
    
    Возвращает:
        HTML страницу отрендеренную из шаблона index.html
        
    render() - функция Django которая берет шаблон, подставляет в него
    данные (если есть) и возвращает готовый HTML.
    """
    return render(request, 'templates/index.html')
