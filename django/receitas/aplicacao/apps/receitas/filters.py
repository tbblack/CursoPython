import django_filters
from receitas.models import Receita, Categoria

class ReceitaFilter(django_filters.FilterSet):
   

    class Meta:
        model = Receita
        fields = ['nome_receita', 'categoria' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['nome_receita'].field.widget.attrs.update({"class": "form-control"})
        self.filters["nome_receita"].lookup_expr = 'icontains'

        self.filters["categoria"].queryset=Categoria.objects.all()
        self.filters["categoria"].field.widget.attrs.update({"class": "form-control", 'onchange': 'this.form.submit()'})
        