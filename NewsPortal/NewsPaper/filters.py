import django_filters
from django import forms

from django_filters import FilterSet


from .models import Post


class PostFilter(FilterSet):
    date = django_filters.DateFilter(
        field_name='date_created',
        lookup_expr='gte',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
           'post_author__author_id__username':['icontains'],
       }