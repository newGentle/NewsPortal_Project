import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import PostForm
from .filters import PostFilter
from .models import Category, Post, User
from .tasks import new_post_notify
from django.utils.translation import gettext as _
import pytz
from django.utils import timezone
# Create your views here.


class PostsList(ListView):
    model = Post
    ordering = '-post_date'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        if (self.request.user in User.objects.all()):
            today = datetime.datetime.today()
            today = today.replace(hour=0, minute=0, second=0)
            context['author_posts'] = Post.objects.filter(post_author__user=self.request.user).filter(post_date__gte=(today)).count
            
        # context['author_posts'] = datetime.time
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['same_post_author'] = self.get_object().post_author.user.id
        context['is_subscribed'] = Category.objects.filter(subscribers=self.request.user.id)
        return context


@login_required
def subscribe(request, *args, **kwargs):
    Category.objects.get(pk=int(kwargs['pk'])).subscribers.add(request.user.id)
    
    return redirect('/')

@login_required
def unsubscribe(request, *args, **kwargs):
    Category.objects.get(pk=int(kwargs['pk'])).subscribers.remove(request.user.id)
    return redirect('/')


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    form_class = PostForm
    model = Post
    template_name = 'postedit.html'
    success_url = reverse_lazy('posts_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_type'] = Post.CHOICE
        context['categories'] = Category.objects.all
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = Post.news
        post.save()
        new_post_notify.apply_async([post.pk], countdown = 60)
        return super().form_valid(form)


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    form_class = PostForm
    model = Post
    template_name = 'postedit.html'
    success_url = reverse_lazy('posts_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_type'] = Post.CHOICE
        context['categories'] = Category.objects.all
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = Post.article
        post.save()
        new_post_notify.apply_async([post.pk], countdown = 60)
        return super().form_valid(form)

    
class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'postedit.html'
    success_url = reverse_lazy('posts_list')


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post')
    model = Post
    template_name = 'postdelete.html'
    success_url = reverse_lazy('posts_list')


class lang_and_tz_settings(TemplateView):
    template_name = 'settings.html'
    success_url = reverse_lazy('settings')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = timezone.now()
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('settings')

