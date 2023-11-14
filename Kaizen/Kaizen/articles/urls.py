from django.urls import path
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.article_list,name="list"),
    path('{?P<slug>[\w-]+}', views.article_details, name="detail")
]
