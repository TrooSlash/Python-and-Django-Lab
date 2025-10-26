from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    
    def get_excerpt(self):
        return self.text[:140] + "..." if len(self.text) > 140 else self.text
    
    def __str__(self):
        return self.title
