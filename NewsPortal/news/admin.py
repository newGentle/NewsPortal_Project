from django.contrib import admin
from .models import Post, Category, Author, PostCategory
# Register your models here.

class role_inline(admin.TabularInline):
    model = PostCategory
    extra = 1

class postAdmin(admin.ModelAdmin):
    inlines = (role_inline,)

admin.site.register(Post, postAdmin)
admin.site.register(Author)
admin.site.register(Category)
