from django.shortcuts import render
from .models import LivrosModel
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LivroModelForm

class LivrosView(LoginRequiredMixin, FormView):
    login_url = 'user/login/'
    redirect_field_name = ''
    template_name = 'livraria.html'
    def get_context_data(self, **kwargs):
        context = super(LivrosView, self).get_context_data(**kwargs)
        user = self.request.user
        context['livros'] = LivrosModel.objects.filter(usuario=user)   
        return context

class LivroCreateView():
    pass
    #https://stackoverflow.com/questions/20852744/django-formview-not-saving