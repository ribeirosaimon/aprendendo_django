from django.contrib import admin
from .models import LivrosModel

@admin.register(LivrosModel)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('usuario','nome_livro','paginas','autor')
    exclude = ['usuario',]

    def get_queryset(self, request):
        qs = super(LivroAdmin, self).get_queryset(request)
        return qs.filter(usuario=request.user)

    def save_model(self,request,obj,form,change):
        obj.usuario = request.user
        super().save_model(request, obj, form, change)