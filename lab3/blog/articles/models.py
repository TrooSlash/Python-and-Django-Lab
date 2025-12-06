# -*- coding: utf-8 -*-
"""
Лабораторная работа №3
Модель статьи для блога

Модель - это класс который описывает структуру таблицы в базе данных.
Django автоматически создает таблицу на основе этого класса.
"""

from django.db import models
from django.contrib.auth.models import User  # Встроенная модель пользователя


class Article(models.Model):
    """
    Модель статьи блога
    Каждое поле = столбец в таблице базы данных
    """
    # id - первичный ключ, Django создает автоматически, но объявляем явно для Pylance
    id: int
    
    # CharField - текстовое поле с ограничением длины (для заголовка)
    title = models.CharField(max_length=200)
    
    # ForeignKey - связь с другой таблицей (автор - это пользователь)
    # on_delete=CASCADE означает: если удалить пользователя - удалятся и его статьи
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # TextField - большое текстовое поле без ограничений (для текста статьи)
    text = models.TextField()
    
    # DateField - поле для даты
    # auto_now_add=True - дата заполняется автоматически при создании
    created_date = models.DateField(auto_now_add=True)
    
    def get_excerpt(self):
        """
        Метод для получения отрывка статьи (первые 140 символов)
        Используется на главной странице чтобы не показывать весь текст
        """
        if len(self.text) > 140:
            return self.text[:140] + "..."
        return self.text
    
    def __str__(self):
        """
        Этот метод вызывается когда нужно преобразовать объект в строку
        Например в админке Django будет показывать заголовок статьи
        """
        return self.title
