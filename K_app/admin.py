from django.contrib import admin

# Register your models here.
# blog/admin.py
from django.contrib import admin
from .models import BlogPost, Category, Tag

admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(Tag)
