from django.shortcuts import render, redirect
from django.http import Http404
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
    if not request.user.is_authenticated:
        return redirect('archive')
    
    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')
        
        if title and text:
            article = Article.objects.create(
                title=title,
                text=text,
                author=request.user
            )
            return redirect('archive')
    
    return render(request, 'create_post.html')
