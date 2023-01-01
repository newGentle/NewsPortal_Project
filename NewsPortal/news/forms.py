from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ValidationError
from .models import Post
from django.utils.translation import gettext as _


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
            'post_author': _('Автор'),
            'categories': _('Категория'),
        }

    def clean(self):
        cleaned = super().clean()
        content = cleaned.get('post_content')
        title = cleaned.get('post_title')
        if title == content:
            raise ValidationError(_('Название и контент не должны быть одинаковыми'))
        return cleaned
