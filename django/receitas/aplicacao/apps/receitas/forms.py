from django import forms

from .models import Receita

class ReceitaForm(forms.ModelForm):

    class Meta:
        model = Receita
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["pessoa"].widget.attrs.update({"class": "form-control"})
        self.fields["nome_receita"].widget.attrs.update({"class": "form-control"})
        self.fields["ingredientes"].widget.attrs.update({"class": "form-control"})
        self.fields["modo_preparo"].widget.attrs.update({"class": "form-control"})
        self.fields["tempo_preparo"].widget.attrs.update({"class": "form-control"})
        self.fields["rendimento"].widget.attrs.update({"class": "form-control"})
        self.fields["categoria"].widget.attrs.update({"class": "form-control"})
        self.fields["date_receita"].widget.attrs.update({"class": "form-control"})
        self.fields["fot_receita"].widget.attrs.update({"class": "form-control"})
        