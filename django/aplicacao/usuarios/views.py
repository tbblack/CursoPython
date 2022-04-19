from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        # Validação se o nome esta vazio
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        # Validação se o email esta vazio
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')
        # Validação se a primeira senha é igual a segunda
        if senha != senha2:
            print('As senhas não são iguais')
            return redirect('cadastro')
        # Validação se o email ja esta cadastrado
        if User.objects.filter(email=email).exists():
            print('Usuario ja cadastrado')
            return redirect('cadastro')     
        # criado e salvando Usuario
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save

        print('Usuario criado com sucesso')
        return redirect('login')
    else:    
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
         # Validação se o email ou senha estão vazio
        if email == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('login realizado com sucesso')
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')

    
