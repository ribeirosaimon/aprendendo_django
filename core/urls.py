from .views import LivrosView
from django.urls import path


urlpatterns = [
    path('livraria', LivrosView.as_view(template_name="livraria.html"),name='livraria'),
]