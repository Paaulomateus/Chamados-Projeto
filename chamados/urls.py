from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('', views.chamado_list, name='chamado_list'),
    path('novo/', views.chamado_create, name='chamado_create'),
    path('editar/<int:pk>/', views.chamado_edit, name='chamado_edit'),
    path('excluir/<int:pk>/', views.chamado_delete, name='chamado_delete'),
    path('detalhe/<int:pk>/', views.chamado_detail, name='chamado_detail'),
    path('register/', RegisterView.as_view(), name='register'),
]

