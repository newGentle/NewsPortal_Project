from django.db.models.signals import m2m_changed
from django.dispatch import receiver 
from django.core.mail import send_mail
from .models import PostCategory, Post
from NewsPortal.settings import DEFAULT_FROM_EMAIL
from django.shortcuts import get_object_or_404
 

@receiver(m2m_changed, sender=PostCategory)
def notify_subscribers(sender, instance, **kwargs):
    
    # print(kwargs['action'])
    if kwargs['action'] == 'post_add':
        categories = instance.categories.all().values_list('id', flat=True)
        subscribers = []
        for cats in categories:
            subscribers += categories.subscribers.all
        print(categories)
    # send_mail(
    #     subject=subject,
    #     message=instance.message,
    #     from_email=DEFAULT_FROM_EMAIL,
    #     recipient_list=[''],
    # )