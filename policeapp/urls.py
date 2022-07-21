from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('police_home', views.police_home, name='police_home'),
    path('upload_challan', views.upload_challan, name='upload_challan'),
    path('get_details', views.get_details, name='get_details'),
    path('cancel', views.cancel, name='cancel'),
    path('post', views.post, name='post'),
    path('p_logout', views.p_logout, name='p_logout'),
    # path('dami', views.dami, name='dami'),
    # path('cancel1', views.cancel1, name='cancel1'),
    # path('view_details', views.view_details, name='view_details'),
]
