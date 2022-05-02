from django.urls import path

from . import views

urlpatterns = [
    path('cadastro/', views.SignupView.as_view(), name='cadastro'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('index/', views.IndexListView.as_view(), name='index'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup')
]