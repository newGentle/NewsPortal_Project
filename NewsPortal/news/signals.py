from django.dispatch import receiver 
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import User
from django.conf import settings
from django.shortcuts import get_object_or_404
from allauth.account.signals import email_confirmed
from django.utils.translation import gettext as _
 
@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
    user = User.objects.get(email=email_address.email)
    user.is_active = True
    user.save()

    html_content = render_to_string(
            template_name='greeting_user.html',
            context={
                'user': user.username,
                'site_url': f'{settings.SITE_URL}'
                }

            )
    send_mail(
        subject=_('Добро пожаловать в наш МИР'),
        message='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=(user.email, ),
        html_message=html_content,
        )


# @receiver(m2m_changed, sender=PostCategory)
# def notify_subscribers(sender, instance, **kwargs):
    
#     # print(kwargs['action'])
#     if kwargs['action'] == 'post_add':
#         categories = instance.categories.all()
#         subscribers = []
#         for cats in categories:
#             subscribers += cats.subscribers.all()

#         username = [usr.username for usr in subscribers]
#         subscribers =[usr.email for usr in subscribers]

#         html_content = render_to_string(
#             template_name='subscribers_email_notify.html',
#             context={
#                 'text': instance.preview(),
#                 'post_link': f'{SITE_URL}/{instance.id}',
#                 'username': username,
#             }
#         )
#         msg = EmailMultiAlternatives(
#             subject=instance.post_title,
#             from_email=DEFAULT_FROM_EMAIL,
#             to=subscribers,
#         )

#         msg.attach_alternative(html_content, 'text/html')
#         msg.send()
