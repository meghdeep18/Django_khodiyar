from .views import *
from django.urls import path, include

urlpatterns = [
    path('',index,name=''),
    path('Work',Work,name='Work'),
    path('contact',contact,name='contact'),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
 
    path('signup_func',signup_func,name='signup_func'),
    path('login_func',login_func,name='login_func'),
     path('contact_submit', contact_submit, name='contact_submit'),


   
]