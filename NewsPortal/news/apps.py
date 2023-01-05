from django.apps import AppConfig
from django.utils.translation import pgettext_lazy

class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
    verbose_name = pgettext_lazy('Новости', 'Новости')

    def ready(self):
        import news.signals
