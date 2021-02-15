from django.shortcuts import render
from django.views.generic import TemplateView
from .models import LivrosModel

class LivrosView(TemplateView):
    template_name = 'livraria.html'
    def get_context_data(self, **kwargs):
        context = super(LivrosView, self).get_context_data(**kwargs)
        user = self.request.user
        context['livros'] = LivrosModel.objects.filter(usuario=user)   
        print(context)
        return context