from receitas.filters import ReceitaFilter
from receitas.models import Receita
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django_filters.views import FilterView


from django.views.generic import TemplateView, CreateView, ListView, DetailView
from receitas.forms import ReceitaForm


class TemplateHomeView(TemplateView):
    template_name = 'index.html'

class ReceitaCreateView(CreateView):
    template_name = 'cria_receitas.html'
    model = Receita
    form_class = ReceitaForm
    success_url = '/lista-receitas/'

class ReceitaListView(FilterView):
    model = Receita
    context_object_name = 'receita'
    template_name = 'lista_receitas.html'
    paginate_by = 1
    filterset_class = ReceitaFilter
      
class ReceitaDetailView(DetailView):
    model = Receita
    template_name = 'receita_detalhes.html'
    context_object_name = 'receita'



