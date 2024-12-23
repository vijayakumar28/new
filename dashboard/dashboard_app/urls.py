
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views 
from django.contrib import admin

urlpatterns = [
    
    path('', views.indexpage, name='dashboard'),
    path('login/', views.loginpage, name='login'), 
    path('register/', views.registerpage, name='register'),
    path('password/', views.passwordpage, name='forgot_password'),
    path('401/', views.fo1page, name='401'),
    path('404/', views.fofpage, name='404'),
    path('500/', views.foopage, name='500'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), 
    path('property/', views.propertypage, name='property_page'),
    path('property_form/', views.allproperty, name='property_form'),
]





