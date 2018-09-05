from django.contrib import admin
from django.contrib.auth.models import User
from .models import Blog

admin.site.register(Blog)
# admin.site.register(User)