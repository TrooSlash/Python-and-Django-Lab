from django.shortcuts import render
from django.http import HttpResponse
from django import template

# Простое представление - просто выводит текст
def home(request):
    # Теперь используем HTML шаблон вместо простого текста
    return render(request, 'templates/index.html')
