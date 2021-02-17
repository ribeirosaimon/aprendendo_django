from .views import LivrosView, LivrosViewDelete, LivrosViewUpdate
from django.urls import path

urlpatterns = [
    path('livraria', LivrosView.as_view(template_name="livraria.html"),name='livraria'),
    path('add_livro', LivrosView.as_view(template_name="add_livro.html"),name='add_livro'),
    path('delete/<int:pk>', LivrosViewDelete.as_view(), name='deletar_livro'),
    path('editar/<int:pk>', LivrosViewUpdate.as_view(), name='editar_livro'),
]