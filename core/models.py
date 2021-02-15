from django.db import models
from users.models import CustomUser
from django.contrib.auth import get_user_model

class LivrosModel(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nome_livro = models.CharField('Livro', max_length=100)
    paginas = models.IntegerField()
    autor = models.CharField('Autor',max_length=100)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.nome_livro