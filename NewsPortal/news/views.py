from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from .filters import PostFilter
from .models import  Category, Post
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
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['same_post_author'] = self.get_object().post_author.user.id
        context['is_subscribed'] = Category.objects.filter(subscribe_cat__id=self.request.user.id)
        return context
    
    def add_sub(request):
        
        return request


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
        # authors = Post.objects.filter(post_author__user__username=self.request.user.username).values_list('post_author__user__id', flat=True)
        # user = self.request.user.id 
        # if user in authors:
        #     context['post_author'] = self.request.user
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = Post.news 
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