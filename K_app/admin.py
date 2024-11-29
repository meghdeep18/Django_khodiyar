from django.contrib import admin
# Register your models here.
# blog/admin.py
from django.contrib import admin
from .models import Contact
from .models import Master
from .models import *



admin.site.register(Contact)
admin.site.register(Master)