from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import pgettext_lazy


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        pRating = sum(Post.objects.filter(post_author=self).values_list('post_rating', flat=True))
        cRating = sum(Comment.objects.filter(comment_user__author=self).values_list('comment_rating', flat=True))
        pcRating = sum(Comment.objects.filter(comment_post__in=Post.objects.filter(post_author=self)).values_list('comment_rating', flat=True))

        self.rating = pRating * 3 + cRating + pcRating
        self.save()

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = pgettext_lazy('Автор', 'Автор')
        verbose_name_plural = pgettext_lazy('Авторы', 'Авторы')


class Category(models.Model):
    politics = 'PO'
    sport = 'SP'
    science = 'SC'
    education = 'ED'
    religion = 'RE'
    CATS = [
        (politics, pgettext_lazy('Политика','Политика')),
        (sport, pgettext_lazy('Спорт', 'Спорт')),
        (science, pgettext_lazy('Наука', 'Наука')),
        (education, pgettext_lazy('Образование', 'Образование')),
        (religion, pgettext_lazy('Религия', 'Религия'))
    ]
    category_name = models.CharField(max_length = 2, choices = CATS, default = politics, unique = True)
    subscribers = models.ManyToManyField(User, related_name='subscribers')
    
    def __str__(self):
        return f'{self.get_category_name_display()}'
        
    
    class Meta:
        verbose_name = pgettext_lazy('Категория', 'Категория')
        verbose_name_plural = pgettext_lazy('Категории', 'Категории')


class Post(models.Model):   
    news = 'NW'
    article = 'AR'
    CHOICE = [
        (news, pgettext_lazy('Новость', 'Новость')),
        (article, pgettext_lazy('Статья', 'Статья'))
    ]   

    post_type = models.CharField(max_length = 2, choices = CHOICE, default = news)
    post_date = models.DateTimeField(auto_now_add = True)
    post_title = models.CharField(max_length = 50)
    post_content = models.TextField()
    post_rating = models.IntegerField(default=0)
    post_author = models.ForeignKey(Author, on_delete = models.CASCADE)
    categories = models.ManyToManyField(Category, through='PostCategory')


    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()
    
    def preview(self):
        return self.post_content[:64]
    
    def __str__(self):
        return f'{self.post_title}'
    
    class Meta:
        verbose_name = pgettext_lazy('Пост', 'Пост')
        verbose_name_plural = pgettext_lazy('Посты', 'Посты')


class PostCategory(models.Model):
    posts = models.ForeignKey(Post, on_delete = models.CASCADE)
    categories = models.ForeignKey(Category, on_delete = models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete = models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add = True)
    comment_rating = models.IntegerField(default = 0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()
