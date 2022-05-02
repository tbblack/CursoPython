from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.urls import reverse
from receitas.models import Receita
from django.views.generic import View, ListView
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout

class IndexListView(ListView):
    model = Receita
    template_name = 'usuarios/index.html'

    def get_queryset(self):
        queryset = Receita.objects.filter(pessoa=self.request.user)
        return queryset
    
class SignupView(View):
    def get(self, request):
        data = { 'form': SignupForm() }     
        return render(request, 'usuarios/signup.html', data)
    
    def post(self, request):
        form = SignupForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            if username and password:

                user = User.objects.create_user(
                    username = username,
                    password = password
                )

                if user:
                    return HttpResponseRedirect(reverse('login'))
        
        data = { 
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }     
        return render(request, 'usuarios/signup.html', data)

class LoginView(View):
     def get(self, request):
        data = { 'form': LoginForm() }
        return render(request, 'usuarios/login.html', data)
    
     def post(self, request):
        
        form = LoginForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            if username and password \
                and authenticate(username=username, password=password):
                user = auth.authenticate(request, username=username, password=password)
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        
        data = { 
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }     
        return render(request, 'usuarios/login.html', data)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))
