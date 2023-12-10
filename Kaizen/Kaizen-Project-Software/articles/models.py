from django.db import models
from django.conf import settings
from datetime import date

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    File = models.FileField(default='default.pdf', blank=True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50] + '...'
    
class Author(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()

    def __str__(self):
        return self.name()  
    
class Entry(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.article