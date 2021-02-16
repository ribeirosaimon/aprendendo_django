from django import forms
from .models import LivrosModel

class LivroModelForm(forms.ModelForm):
    class Meta:
        model = LivrosModel
        fields = ['nome_livro', 'paginas','autor'] 
        
'''

class LivroModelForm(forms.Form):
    nome_livro = forms.CharField(label='Nome',max_length=100)
    paginas = forms.IntegerField(label='Paginas')
    autor = forms.CharField(label='Autor',max_length=100)
'''