
from django import forms
from django.db.models.query import QuerySet
from django.forms import widgets
from django_filters.filters import ModelMultipleChoiceFilter
from .models import Post,Tag
import django_filters
from django_filters import CharFilter

class PostFilter(django_filters.FilterSet):
    headline = CharFilter('headline',lookup_expr='icontains')
    tags = ModelMultipleChoiceFilter(queryset= Tag.objects.all(),
        widget = forms.CheckboxSelectMultiple)
    class Meta:
        model = Post
        fields = ['headline', 'tags']