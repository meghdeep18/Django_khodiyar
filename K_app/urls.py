from .views import *
from django.urls import path, include

urlpatterns = [
    path('',index,name=''),
    path('Work',Work,name='Work'),
    path('contact',contact,name='contact'),

     path('contact_submit', contact_submit, name='contact_submit'),


   
]