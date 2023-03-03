from django.contrib import admin

# Register your models here.

from .models import Rooms, Messages, Chat_Users

admin.site.register(Rooms)
admin.site.register(Messages)
admin.site.register(Chat_Users)