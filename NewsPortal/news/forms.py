from django import forms
from django.forms import ValidationError
from .models import Post

class PostForm(forms.ModelForm):
    post_title = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    post_content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Post
        fields = [
            'post_title',
            'post_content',
            'categories',
            'post_author',
        ]
        labels = {
            'post_author': 'Автор',
            'categories': 'Категория',
        }

    def clean(self):
        cleaned = super().clean()
        content = cleaned.get('post_content')
        title = cleaned.get('post_title')
        if title == content:
            raise ValidationError('Название и контент не должны быть одинаковыми')
        return cleaned