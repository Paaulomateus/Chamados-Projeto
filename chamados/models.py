from django.db import models

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

    def __str__(self):
        return self.titulo