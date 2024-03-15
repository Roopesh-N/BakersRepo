from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.LoginView,name='login'),
    path('homepage/',views.homepage_view,name='homepage'),
    path('signup/',views.signupView,name='signup'),
]