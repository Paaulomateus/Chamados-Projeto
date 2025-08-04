from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChamadoForm
from .models import Chamado
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ChamadoSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

@login_required
def chamado_list(request):
    chamados = Chamado.objects.all().order_by('-criado_em')
    return render(request, 'chamados/chamado_list.html', {'chamados': chamados})

@login_required
def chamado_create(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
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
        form = ChamadoForm(request.POST, instance=chamado)
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