from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from receitas.filters import ReceitaFilter
from receitas.models import Receita, Categoria
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):

    #lista receitas
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    #Buscando Categorias
    categorias = Categoria.objects.all()
    #Verificando se buscar esta no GET
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if 'buscar':
            receitas = receitas.filter(nome_receita__icontains=nome_a_buscar)
    #Filtro receitas
    receita_list = ReceitaFilter(request.GET, queryset=receitas)
    #Paginação
    paginator = Paginator(receita_list.qs, 1)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)
    #Montagem da estrutura de dados para view
    dados = {
        'receitas' : receitas_por_pagina,
        'filter' : receita_list,
        'categorias' : categorias
    }
    print(dados)
    #Return view
    return render(request, 'receitas/index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : receita
    }

    return render(request,'receitas/receita.html', receita_a_exibir)

def cria_receita(request):
    
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)

        receita = Receita.objects.create(pessoa=user, 
        nome_receita=nome_receita, ingredientes=ingredientes, 
        modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, 
        rendimento=rendimento, categoria=categoria, 
        fot_receita=foto_receita)

        receita.save()

        return redirect('dashboard')
    else:
        return render(request, 'receitas/cria_receita.html')   

def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = { 'receita' : receita }
    return render(request, 'receitas/edita_receita.html', receita_a_editar)

def atualiza_receita(request):
    if request.method == 'POST':

        r = Receita.objects.get(pk=request.POST['receita_id'])

        r.nome_receita=request.POST['nome_receita'] 
        r.ingredientes=request.POST['ingredientes']
        r.modo_preparo=request.POST['modo_preparo'] 
        r.tempo_preparo=request.POST['tempo_preparo'] 
        r.rendimento=request.POST['rendimento'] 
        r.categoria=request.POST['categoria']

        if 'foto_receita' in request.FILES:
            r.fot_receita=request.FILES['foto_receita']

        r.save()

        return redirect('dashboard')
