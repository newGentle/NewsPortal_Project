from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chat_Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default=None)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Messages(models.Model):
    author = models.ForeignKey(Chat_Users, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey('Rooms', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Rooms(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    created = models.DateField(auto_now_add=True)
    members = models.ManyToManyField(Chat_Users, blank=True)

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):

        return f'{self.name}'

