from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('About/', views.About),
    path('Login/', views.Login),
    path('Registration/', views.Registration),
    path('articles/', include('articles.urls')),
    path('members/', include('members.urls')),
    path('', views.Homepage),
]
