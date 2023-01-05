from .models import Post
from modeltranslation.translator import register, TranslationOptions

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('post_title', 'post_content',)
