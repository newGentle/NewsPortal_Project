from django.db.models.signals import m2m_changed
from django.dispatch import receiver 
from django.core.mail import send_mail
from .models import PostCategory
from NewsPortal.settings import DEFAULT_FROM_EMAIL
 

@receiver(m2m_changed, sender=PostCategory)
def notify_subscribers(sender, instance, **kwargs):
    
    print(kwargs)
 
    # send_mail(
    #     subject=subject,
    #     message=instance.message,
    #     from_email=DEFAULT_FROM_EMAIL,
    #     recipient_list=[''],
    # )