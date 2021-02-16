from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from .models import LivrosModel
from .forms import LivroModelForm

from django.urls import reverse_lazy
from django.contrib import messages

class LivrosView(LoginRequiredMixin, FormView):
    login_url = 'user/login/'
    redirect_field_name = ''
    template_name = 'livraria.html'
    form_class = LivroModelForm
    success_url = reverse_lazy('livraria')

    def get_context_data(self, **kwargs):
        context = super(LivrosView, self).get_context_data(**kwargs)
        user = self.request.user
        context['livros'] = LivrosModel.objects.filter(usuario=user)   
        return context

    def form_valid(self,form,*args,**kwargs):
        teste = form.save(commit=False)
        teste.usuario = self.request.user
        teste.save()
        messages.success(self.request, 'Livro salvo')
        return super(LivrosView, self).form_valid(form,*args,**kwargs)

    def form_invalid(self, form, *args3, **kwargs):
        messages.error(self.request,'Algo deu errado')
        return super(LivrosView, self).form_valid(form,*args,**kwargs)