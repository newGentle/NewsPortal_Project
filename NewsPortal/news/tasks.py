import datetime
from .models import Post, Category, User
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from celery import shared_task
from django.utils.translation import gettext as _

@shared_task
def weekly_notify(*args, **kwargs):
    today = datetime.datetime.now()    
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(post_date__gte=last_week).order_by('-post_date')
    categories = set(posts.values_list('categories__category_name', flat=True))
    username = set(Category.objects.filter(category_name__in=categories).values_list('subscribers__username', flat=True))
    subscribers = set(Category.objects.filter(category_name__in=categories).values_list('subscribers__email', flat=True))
    userID = set(Category.objects.filter(category_name__in=categories).values_list('subscribers__pk', flat=True))
    
    for UID, subn, name in zip(userID, subscribers, username):
        
        # print(f'{UID} - {name} - {subn} -> {posts.filter(categories__subscribers=UID)}')
        html_content = render_to_string(
            template_name='subscribers_email_notify_weekly.html',
            context={
                'posts': posts.filter(categories__subscribers=UID),
                'posts_link': settings.SITE_URL,
                'username': name,
            }

            )
        send_mail(
            subject=_('Посты за неделю'),
            message='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=(subn,),
            html_message=html_content,
            
            )

        # msg.attach_alternative(html_content, 'text/html')
        
        # msg.send()


@shared_task
def new_post_notify(postid):
    # if kwargs['action'] == 'post_add':
    post = Post.objects.get(pk=postid)
    categories = post.categories.all()
    subscribers = []
    for cats in categories:
        subscribers += cats.subscribers.all()
    username = [usr.username for usr in subscribers]
    subscribers = [usr.email for usr in subscribers]

    html_content = render_to_string(
        template_name='subscribers_email_notify.html',
        context={
            'text': post.preview(),
            'post_link': f'{settings.SITE_URL}/{post.pk}',
            'username': username,
        }
    )
    msg = EmailMultiAlternatives(
        subject=post.post_title,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
