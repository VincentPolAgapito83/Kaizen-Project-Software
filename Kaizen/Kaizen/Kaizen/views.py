from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def Homepage(request):
    # return HttpResponse('Welcome To Kaizen Website')
    return render(request, 'Homepage.html')

def About(request):
    # return HttpResponse('About Us')
    return render(request, 'About.html')

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            # log in the user
            return redirect('articles:list')
    else:
        form = AuthenticationForm()
    # return HttpResponse('Login')
    return render(request, 'Login.html', {'form':form})

def Registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    # return HttpResponse('Sign-up')
    return render(request, 'Registration.html')

def article_list(request):  
    # return HttpResponse('Article list')
    return render(request, 'articles/article_list.html')

def article_details(request):  
    # return HttpResponse('List Of Authors')
    return render(request, 'articles/article_details.html')


