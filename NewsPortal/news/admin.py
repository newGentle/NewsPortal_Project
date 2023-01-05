from django.contrib import admin
from .models import Post, Category, Author, PostCategory
from modeltranslation.admin import TranslationAdmin
# Register your models here.


class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1


class PostAdmin(TranslationAdmin, admin.ModelAdmin):
    model = Post
    inlines = (PostCategoryInline,)
    list_display = ("post_title", "preview",)
    list_filter = ("post_date",)
    fields = ('post_title', 'post_content', 'post_author', 'post_type')


class CategoryAdmin(admin.ModelAdmin):
    inlines = (PostCategoryInline,)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author)
