from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('user_home', views.user_home, name='user_home'),
    path('view_challan/<num>', views.view_challan, name='view_challan'),
    path('challa_list', views.challa_list, name='challa_list'),
    path('compliant', views.compliant, name='compliant'),
    path('payments/<int:id>', views.payments, name='payments'),
    path('paymentrequest', views.paymentrequest, name='paymentrequest'),
    path('u_complient/<int:id>', views.u_complient, name='u_complient'),
    path('u_logout', views.u_logout, name='u_logout'),
]