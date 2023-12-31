from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = "Kaizen"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('About/', views.About, name="about"),
    path('Login/', views.Login, name="Login"),
    path('index/', views.index),
    path('Search_result', views.SearchResults, name="SearchResults"),
    path('Registration/', views.Registration, name="Registration"),
    path('articles/', include('articles.urls')),
    path('members/', include('members.urls')),
    path('', views.Homepage),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
