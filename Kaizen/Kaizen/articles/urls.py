from django.urls import path
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.author_list, name="list"),
    path('About/', views.about),
    path('Homepage/', views.Homepage),
    path('', views.article_details, name="detail")
]
