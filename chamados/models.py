from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
        
class Chamado(models.Model):
    PRIORIDADES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    STATUS = [
        ('aberto', 'Aberto'),
        ('em_andamento', 'Em andamento'),
        ('fechado', 'Fechado'),
    ]

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    prioridade = models.CharField(max_length=10, choices=PRIORIDADES, default='media')
    status = models.CharField(max_length=15, choices=STATUS, default='aberto')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivo = models.FileField(upload_to='anexos/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.usuario} em {self.criado_em.strftime("%d/%m/%Y %H:%M")}'