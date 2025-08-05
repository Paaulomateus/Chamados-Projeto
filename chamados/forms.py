from django import forms
from .models import Chamado, Comentario

class ChamadoForm(forms.ModelForm):
    
    class Meta:
         model = Chamado
         fields = ('titulo', 'descricao', 'prioridade', 'status', 'arquivo')

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escreva seu comentário aqui...'}),
        }