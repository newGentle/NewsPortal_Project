from django.contrib import admin
from .models import Author, Post, Category
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
