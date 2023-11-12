from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def author_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/author_list.html', {'articles': articles})  

def Homepage(request):
    # return HttpResponse('Welcome To Kaizen Website')
    return render(request, 'Homepage.html')

def about(request):
    # return HttpResponse('About Us')
    return render(request, 'About.html')

def Logout(request):
    # return HttpResponse('Homepage')
    return render(request, 'Homepage.html')

def article_details(request, slug):  
    return HttpResponse(slug)
    


