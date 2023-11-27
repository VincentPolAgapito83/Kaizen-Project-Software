from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    File = models.FileField(default='default.pdf', blank=True)
    #author = models.ForeignKey(author)



    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50] + '...'