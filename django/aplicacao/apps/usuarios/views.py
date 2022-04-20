from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def cadastro(request):
    """ Cadastra uma nova pessoa no sistema """
    if request.method == 'POST':

        # Validação se o nome esta vazio
        if campo_vazio(request.POST['nome']):
            messages.error(request, 'O campo nome não pode ficar em branco') 
            return redirect('cadastro')

        # Validação se o email esta vazio
        if campo_vazio(request.POST['email']):
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('cadastro')

        # Validação se a primeira senha é igual a segunda
        if senhas_nao_sao_iguais(request.POST['password'], request.POST['password2']):
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')

        # Validação se o email ja esta cadastrado
        if User.objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'Usuario ja cadastrado')
            return redirect('cadastro') 

        # Validação se o username ja esta cadastrado
        if User.objects.filter(username=request.POST['nome']).exists():
            messages.error(request, 'Usuario ja cadastrado')
            return redirect('cadastro')    

        # criado e salvando Usuario
        user = User.objects.create_user(username=request.POST['nome'], email=request.POST['email'], password=request.POST['password'])
        user.save

        messages.success(request, 'Usuario criado com sucesso')
        return redirect('login')
    else:    
        return render(request, 'usuarios/cadastro.html')

def login(request):
    """ Realiza o login de uma pessoa no sistema """
    if request.method == 'POST':

         # Validação se o email ou senha estão vazio
        if campo_vazio(request.POST['email']) or campo_vazio(request.POST['senha']):
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')
        
        if User.objects.filter(email=request.POST['email']).exists():
            nome = User.objects.filter(email=request.POST['email']).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=request.POST['senha'])
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')

def logout(request):
    """ Realiza o logout de uma pessoa no sistema """
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    """ Busca receitas para a pagina de Dashboard """
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)
        dados = {
            'receitas' : receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def campo_vazio(campo):
    """ Valida se o campo esta vazio """
    return not campo.strip()

def senhas_nao_sao_iguais(senha, senha2):
    """ Valida se a senha 1 e senha 2 estão iguais """
    return senha != senha2