from django.contrib import admin
from .models import Categoria, Chamado, Comentario

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'prioridade', 'status', 'criado_em')
    list_filter = ('prioridade', 'status')
    search_fields = ('titulo', 'descricao')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'chamado', 'usuario', 'criado_em')
    search_fields = ('texto', 'usuario__username')
    list_filter = ('criado_em',)
