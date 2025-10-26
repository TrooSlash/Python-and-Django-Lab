import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()

from django.contrib.auth.models import User
from articles.models import Article

# Получаем пользователя admin
admin_user = User.objects.get(username='admin')

# Создаем 3 статьи
articles_data = [
    {
        'title': 'Первая статья о Django',
        'text': 'Django - это мощный фреймворк для веб-разработки на Python. Он позволяет быстро создавать надежные веб-приложения. Django следует принципу DRY (Don\'t Repeat Yourself) и включает множество встроенных возможностей.'
    },
    {
        'title': 'Работа с моделями в Django',
        'text': 'Модели в Django - это классы Python, которые описывают структуру базы данных. Каждая модель соответствует таблице в БД. Django ORM позволяет работать с базой данных без написания SQL запросов напрямую.'
    },
    {
        'title': 'Шаблоны и представления',
        'text': 'Представления в Django обрабатывают запросы пользователей и возвращают ответы. Шаблоны позволяют создавать динамические HTML страницы. Django использует собственную систему шаблонов с простым синтаксисом.'
    }
]

# Добавляем статьи
for data in articles_data:
    article = Article.objects.create(
        title=data['title'],
        author=admin_user,
        text=data['text']
    )
    print(f'Создана статья: {article.title}')

print(f'\nВсего статей в базе: {Article.objects.count()}')
