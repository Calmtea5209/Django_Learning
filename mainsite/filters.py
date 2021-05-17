from django import forms
from .models import Write
import django_filters

class articleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    model = Write
    fields = ['title']
