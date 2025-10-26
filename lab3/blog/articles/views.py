from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Article

# Create your views here.

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if request.user.is_anonymous:
        raise Http404
    
    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')
        
        if title and text:
            article = Article.objects.create(
                title=title,
                text=text,
                author=request.user
            )
            return redirect('get_article', article_id=article.id)
    
    return render(request, 'create_post.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if username and email and password:
            try:
                User.objects.get(username=username)
                return render(request, 'register.html', {'error': 'Пользователь с таким логином уже существует'})
            except User.DoesNotExist:
                User.objects.create_user(username=username, email=email, password=password)
                return redirect('login_view')
    
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('archive')
        else:
            return render(request, 'login.html', {'error': 'Неверный логин или пароль'})
    
    return render(request, 'login.html')
