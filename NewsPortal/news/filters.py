from django import forms
from django.forms import DateInput
from django_filters import FilterSet
import django_filters
from .models import Category, Post
from django.utils.translation import gettext_lazy as _


class PostFilter(FilterSet):
    post_title = django_filters.CharFilter(field_name='post_title', lookup_expr='icontains', label=_('Название'), widget=forms.TextInput(attrs={'class': 'me-2 mb-2 form-control'}))
    post_content = django_filters.CharFilter(field_name='post_content', lookup_expr='icontains', label=_('Содержание'), widget=forms.TextInput(attrs={'class': 'me-2 mb-2 form-control'}))
    post_type = django_filters.ChoiceFilter(field_name='post_type', choices=Post.CHOICE, label=_('Тип'), empty_label=_('Все'), widget=forms.Select(attrs={'class': 'me-2 mb-2 form-control'}))
    post_date_gt = django_filters.DateFilter(
        field_name='post_date',
        label=_('С'),
        lookup_expr='gt',
        widget=DateInput(attrs={'type': 'date', 'class': 'me-2 form-control'})
        )

    post_date_lt = django_filters.DateFilter(
        field_name='post_date',
        label=_('По'),
        lookup_expr='lt',
        widget=DateInput(attrs={'type': 'date', 'class': 'me-2 form-control'})
        )

    categories = django_filters.ModelChoiceFilter(
        lookup_expr='exact',
        field_name='categories',
        queryset=Category.objects.all(),
        label=_('Категория'),
        empty_label=_('Все'),
        )

    class Meta:
        model = Post
        fields = []
