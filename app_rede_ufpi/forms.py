from django import forms
from .models import Comentario, ComentariosComunidade

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']

class ComentarioForm2(forms.ModelForm):
    class Meta:
        model = ComentariosComunidade
        fields = ['conteudo']