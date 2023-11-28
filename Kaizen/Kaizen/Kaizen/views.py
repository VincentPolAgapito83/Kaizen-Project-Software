from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime
from django.contrib import auth
from django.contrib.auth.models import User


@login_required(login_url='Templates/login')
def Homepage(request):
    # return HttpResponse('Welcome To Kaizen Website')
    return render(request, 'Homepage.html')

def About(request):
    # return HttpResponse('About Us')
    return render(request, 'About.html')

def Registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('Username exists! try another username..')
                return redirect('Registration') 
            else:
                if User.objects.filter(email=email).exists():
                   print('email exists! try other email..')
                   return redirect('Registration')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    return redirect('Login')
        else:
            print('Passwords are not Matched...')
            return redirect('Register')    
    else:
        return render(request, 'Registration.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('Login was successful!')
            return redirect('Index')
        else:
            print('Invalid login!')
            return redirect('Login')
    else:  
        return render(request, 'Login.html')
    
def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print('You Are Logged out from this website..')
        return redirect('Login')
    
def index(request):
    article_list = article_list.objects.all()
    p = Paginator(article_list, 20)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context = {'articles': page}
    return render(request, 'index.html', context)

def SearchResults(request):

    category = request.GET.get('category')

    if category == None:
        articles = Article.objects.order_by('title').filter(is_published=True)
        page_num = request.GET.get("page")
        paginator = Paginator(articles, 2)
        try:
            articles = paginator.page(page_num)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
    else:
        articles = Article.objects.filter(article_title=article)

    articles = articles.objects.all()

    context ={
        'articles': articles
    }
    #return HttpResponse()
    return render(request, 'Search_Results.html')

def article_list(request):  
    # return HttpResponse('Article list')
    return render(request, 'articles/article_list.html')

def article_details(request):  
    # return HttpResponse('List Of Authors')
    return render(request, 'articles/article_details.html')


