from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChamadoForm, ComentarioForm
from .models import Chamado
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ChamadoSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator

@login_required
def chamado_list(request):
    busca = request.GET.get('busca', '')
    status = request.GET.get('status', '')
    prioridade = request.GET.get('prioridade', '')
    pagina = request.GET.get('page', 1)

    chamados = Chamado.objects.all()

    if busca:
        chamados = chamados.filter(titulo__icontains=busca) | chamados.filter(descricao__icontains=busca)
    
    if status:
        chamados = chamados.filter(status=status)

    if prioridade:
        chamados = chamados.filter(prioridade=prioridade)

    chamados = chamados.order_by('-criado_em')

    paginator = Paginator(chamados, 10)
    page_obj = paginator.get_page(pagina)

    valores = {
        'busca': busca,
        'status': status,
        'prioridade': prioridade
    }

    return render(request, 'chamados/chamado_list.html', {
        'page_obj': page_obj,
        'valores': valores
    })


@login_required
def chamado_create(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('chamado_list')
    else:
        form = ChamadoForm()
    
    return render(request, 'chamados/chamado_form.html', {'form': form})

@login_required
def chamado_edit(request, pk):
    chamado = get_object_or_404(Chamado, pk=pk)
    if request.method == 'POST':
        form = ChamadoForm(request.POST, request.FILES, instance=chamado)
        if form.is_valid():
            form.save()
            return redirect('chamado_list')
    else:
        form = ChamadoForm(instance=chamado)
    
    return render(request, 'chamados/chamado_form.html', {'form': form})

@login_required
def chamado_delete(request, pk):
    chamado = get_object_or_404(Chamado, pk=pk)
    if request.method == 'POST':
        chamado.delete()
        return redirect('chamado_list')
    
    return render(request, 'chamados/chamado_confirm_delete.html', {'chamado': chamado})

class ChamadoViewSet(viewsets.ModelViewSet):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer
    permission_classes = [IsAuthenticated]
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect('chamado_list')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect(request.GET.get('next') or 'chamado_list')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'chamados/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

from django.contrib.auth.decorators import login_required

@login_required
def chamado_detail(request, pk):
    chamado = get_object_or_404(Chamado, pk=pk)
    comentarios = chamado.comentarios.order_by('criado_em')
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.chamado = chamado
            comentario.usuario = request.user
            comentario.save()
            return redirect('chamado_detail', pk=pk)
    else:
        form = ComentarioForm()
    return render(request, 'chamados/chamado_detail.html', {'chamado': chamado, 'comentarios': comentarios, 'form': form})
