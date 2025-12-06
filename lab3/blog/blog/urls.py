# -*- coding: utf-8 -*-
"""
Лабораторные работы №3-6
Маршруты URL для блога

Здесь настраивается какой URL какую функцию (view) вызывает.
Например: когда пользователь заходит на /article/1/ - вызывается get_article
"""

from django.contrib import admin
from django.urls import path
from articles import views  # Импортирую мои представления из приложения articles

# Список всех URL маршрутов
urlpatterns = [
    # Админка Django (стандартная, создается автоматически)
    path('admin/', admin.site.urls),
    
    # Лаба 3: Главная страница - архив статей
    # '' означает корень сайта (http://127.0.0.1:8000/)
    path('', views.archive, name='archive'),
    
    # Лаба 4: Страница отдельной статьи
    # <int:article_id> - это параметр URL, число передается в функцию get_article
    path('article/<int:article_id>/', views.get_article, name='get_article'),
    
    # Лаба 5: Создание новой статьи
    path('article/new/', views.create_post, name='create_post'),
    
    # Лаба 6: Регистрация нового пользователя
    path('register/', views.register, name='register'),
    
    # Лаба 6: Вход в систему
    path('login/', views.login_view, name='login_view'),
]
