# -*- coding: utf-8 -*-
"""
Лабораторные работы №3-6
Представления (views) для блога

Представления - это функции которые обрабатывают запросы пользователей
и возвращают HTML страницы. Каждая функция отвечает за свою страницу.
"""

from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User  # Встроенная модель пользователя Django
from django.contrib.auth import authenticate, login  # Функции для авторизации
from .models import Article  # Моя модель статьи из models.py


def archive(request):
    """
    Лаба 3: Главная страница - архив всех статей
    Просто получаем все статьи из базы и передаем в шаблон
    """
    # Article.objects.all() - получает ВСЕ записи из таблицы Article
    posts = Article.objects.all()
    # render() - рендерит HTML шаблон и передает в него переменные
    return render(request, 'archive.html', {"posts": posts})


def get_article(request, article_id):
    """
    Лаба 4: Страница отдельной статьи
    article_id приходит из URL (например /article/1/ -> article_id=1)
    """
    try:
        # Пытаемся найти статью по id
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        # Если статьи с таким id нет - возвращаем ошибку 404
        raise Http404


def create_post(request):
    """
    Лаба 5: Создание новой статьи через форму
    Доступно только авторизованным пользователям!
    """
    # Проверяем авторизован ли пользователь
    # is_anonymous = True если пользователь не вошел в систему
    if request.user.is_anonymous:
        raise Http404  # Если не авторизован - показываем 404
    
    # Если пришел POST запрос - значит пользователь отправил форму
    if request.method == "POST":
        # Получаем данные из формы
        title = request.POST.get('title')
        text = request.POST.get('text')
        
        # Проверяем что оба поля заполнены
        if title and text:
            # Создаем новую статью в базе данных
            article = Article.objects.create(
                title=title,
                text=text,
                author=request.user  # Автор - текущий пользователь
            )
            # Перенаправляем на страницу созданной статьи
            return redirect('get_article', article_id=article.id)
    
    # Если GET запрос - просто показываем пустую форму
    return render(request, 'create_post.html')


def register(request):
    """
    Лаба 6: Регистрация нового пользователя
    """
    if request.method == "POST":
        # Получаем данные из формы регистрации
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if username and email and password:
            try:
                # Проверяем, есть ли уже пользователь с таким логином
                User.objects.get(username=username)
                # Если есть - показываем ошибку
                return render(request, 'register.html', {'error': 'Пользователь с таким логином уже существует'})
            except User.DoesNotExist:
                # Если такого пользователя нет - создаем нового
                # create_user() - специальный метод, он хэширует пароль
                User.objects.create_user(username=username, email=email, password=password)
                # После регистрации перенаправляем на страницу входа
                return redirect('login_view')
    
    # Показываем форму регистрации
    return render(request, 'register.html')


def login_view(request):
    """
    Лаба 6: Вход в систему (авторизация)
    """
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # authenticate() проверяет логин и пароль
        # Возвращает объект пользователя если данные верные, иначе None
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # login() создает сессию для пользователя
            login(request, user)
            # Перенаправляем на главную страницу
            return redirect('archive')
        else:
            # Если данные неверные - показываем ошибку
            return render(request, 'login.html', {'error': 'Неверный логин или пароль'})
    
    # Показываем форму входа
    return render(request, 'login.html')
