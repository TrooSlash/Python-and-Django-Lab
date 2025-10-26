import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()

from django.contrib.auth.models import User
from articles.models import Article

# Создаем или обновляем суперпользователя admin
admin_user, created = User.objects.get_or_create(username='admin')
admin_user.set_password('admin')
admin_user.email = 'admin@admin.com'
admin_user.is_superuser = True
admin_user.is_staff = True
admin_user.save()

if created:
    print('✅ Создан новый суперпользователь: admin/admin')
else:
    print('✅ Обновлен существующий суперпользователь: admin/admin')

# Удаляем старые статьи если есть
Article.objects.all().delete()

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

for data in articles_data:
    article = Article.objects.create(
        title=data['title'],
        author=admin_user,
        text=data['text']
    )
    print(f'✅ Создана статья: {article.title}')

print(f'\n📊 Итого:')
print(f'   Пользователей: {User.objects.count()}')
print(f'   Статей: {Article.objects.count()}')
print(f'\n🔗 Теперь все проекты используют единую БД: shared_db/django_labs.db')
