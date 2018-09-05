from .models import Paper, ConferencePaper, Conference, Quality, Project, Researcher
import django_filters
from django import forms


class PaperFilter(django_filters.FilterSet):
    title= django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Paper
        fields = ['num','title','year',]

class Calidad(django_filters.FilterSet):
    id = django_filters.ModelChoiceFilter(queryset=Quality.objects.values_list('id', flat=True).order_by('-value'))
    value = django_filters.LookupChoiceFilter(
        field_class=forms.FloatField,
        lookup_choices=[
            ('exact', 'Equals'),
            ('gt', 'Greater than'),
            ('lt', 'Lower than'),
        ]
    )
    class Meta:
        model = Quality
        fields = ['id','value',]

class ProjectFilter(django_filters.FilterSet):
    type = django_filters.CharFilter(lookup_expr='icontains')
    from_date=django_filters.DateFilter(lookup_expr='gt')
    
    class Meta:
        model = Project
        fields = {
            'title':['contains',],
            'from_date':['gt', 'lt',],
            'to_date':['gt','lt',],
        }

class Participantes(django_filters.FilterSet):
    login = django_filters.ModelChoiceFilter(queryset=Researcher.objects.values_list('login', flat=True).order_by('login'))
    class Meta:
        model = Researcher
        fields=['login']

