from django.urls import path
from . import views

urlpatterns = [
    path('', views.chamado_list, name='chamado_list'),
    path('novo/', views.chamado_create, name='chamado_create'),
    path('editar/<int:pk>/', views.chamado_edit, name='chamado_edit'),
    path('excluir/<int:pk>/', views.chamado_delete, name='chamado_delete'),
]

