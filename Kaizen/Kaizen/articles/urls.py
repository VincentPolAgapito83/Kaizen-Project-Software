from django.urls import path
from .import views

urlpatterns = [
    path('', views.author_list),
    path('About/', views.about),
    path('Homepage/', views.Homepage)
]
