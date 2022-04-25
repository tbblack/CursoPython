import django_filters
from receitas.models import Receita

class ReceitaFilter(django_filters.FilterSet):

    categoria = django_filters.CharFilter()

    class Meta:
        model = Receita
        fields = ('categoria',)