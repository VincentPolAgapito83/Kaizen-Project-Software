from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
    # return HttpResponse('Welcome To Kaizen Website')
    return render(request, 'Homepage.html')

def About(request):
    # return HttpResponse('About Us')
    return render(request, 'About.html')

def Login(request):
    # return HttpResponse('Login')
    return render(request, 'Login.html')

def Registration(request):
    # return HttpResponse('Sign-up')
    return render(request, 'Registration.html')

def authors(request):  
    # return HttpResponse('List Of Authors')
    return render(request, 'articles/authors_list.html')

def article_details(request):  
    # return HttpResponse('List Of Authors')
    return render(request, 'articles/article_details.html')


