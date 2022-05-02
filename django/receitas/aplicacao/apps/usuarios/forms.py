from django.forms import CharField, ModelForm
from django import forms
from django.contrib.auth.models import User


class SignupForm(ModelForm):   

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["username"].label = 'Usuário'

        self.fields["password"].widget.attrs.update({"class": "form-control"})    
        self.fields["password"].label = 'Senha'
        self.fields["password"].widget.input_type = 'password'
        
class LoginForm(forms.Form):  

    username = forms.CharField(label = 'Usuário')
    password = forms.CharField(label = 'Senha')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["username"].label = 'Usuário'

        self.fields["password"].widget.attrs.update({"class": "form-control"})
        self.fields["password"].label = 'Senha'
        self.fields["password"].widget.input_type = 'password'