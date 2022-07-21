from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('admin', views.admin, name='admin'),
    path('user', views.user, name='user'),
    path('police', views.police, name='police'),
    path('contact', views.contact, name='contact'),
   
    
]