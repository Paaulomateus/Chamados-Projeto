from django.contrib import admin
from .models import Categoria, Chamado
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'prioridade', 'status', 'criado_em')
    list_filter = ('prioridade', 'status')
    search_fields = ('titulo', 'descricao')