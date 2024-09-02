from .views import *
from django.urls import path, include

urlpatterns = [
    path('',index,name=''),
    path('Work',Work,name='Work'),
    path('contact',contact,name='contact'),

     path('contact_submit', contact_submit, name='contact_submit'),


    # path('blog', blog, name='blog'),


    # path('blog', blog, name='blog'),
    # path('<slug:slug>/', blog_detail, name='blog_detail'),
    # path('category/<slug:slug>/', category_posts, name='category_posts'),

]