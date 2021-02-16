from django import forms
from .models import LivrosModel

class LivroModelForm(forms.ModelForm):
    class Meta:
        model = LivrosModel
        user = self.request.user
        fields = [user,'nome_livro', 'paginas','autor']