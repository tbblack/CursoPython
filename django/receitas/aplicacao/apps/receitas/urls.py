from django.urls import path
from django.contrib import admin

from .views import *
from receitas import views

app_name = 'receitas'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplateHomeView.as_view()),
    path('lista-receitas/', views.ReceitaListView.as_view(), name='lista-receitas'),
    path('cria-receitas/', views.ReceitaCreateView.as_view()),
    path('receita-detalhes/<int:pk>', views.ReceitaDetailView.as_view(), name='receita-detalhes')
]