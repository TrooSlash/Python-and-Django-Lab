"""
Лабораторная работа №2-4 - Маршрутизация URL

Этот файл определяет какие URL-адреса доступны на сайте
и какие представления (views) их обрабатывают.

Когда пользователь вводит адрес в браузере, Django ищет его здесь
и вызывает соответствующую функцию из views.py.

Документация Django: https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from flatpages import views  # Импортируем наши представления

# Список всех URL-маршрутов сайта
urlpatterns = [
    # Админ-панель Django - доступна по адресу /admin/
    path('admin/', admin.site.urls),
    
    # Главная страница - пустой путь '' означает корень сайта (http://localhost:8000/)
    path('', views.home, name='home'),
    
    # Дополнительный URL /hello/ - тоже ведет на главную страницу
    path('hello/', views.home, name='hello'),
]
