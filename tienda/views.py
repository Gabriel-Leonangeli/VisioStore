from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Categoria, Formato, Visual
from .forms import CategoriaForm, FormatoForm, VisualForm, BuscarVisualForm

def index(request):
    visuales = Visual.objects.all()
    return render(request, 'tienda/index.html', {'visuales': visuales})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'tienda/categorias.html', {'form': form})

def crear_formato(request):
    if request.method == 'POST':
        form = FormatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FormatoForm()
    return render(request, 'tienda/formatos.html', {'form': form})

@login_required
def crear_visual(request):
    if request.method == 'POST':
        form = VisualForm(request.POST, request.FILES)
        if form.is_valid():
            visual = form.save(commit=False)
            visual.user = request.user  # asigna el usuario logueado
            visual.save()
            return redirect('mis_visuales')
    else:
        form = VisualForm()
    return render(request, 'tienda/visuales.html', {'form': form})

@login_required
def mis_visuales(request):
    visuales = Visual.objects.filter(user=request.user)
    return render(request, 'tienda/mis_visuales.html', {'visuales': visuales})

@login_required
def editar_visual(request, visual_id):
    visual = get_object_or_404(Visual, id=visual_id, user=request.user)
    if request.method == 'POST':
        form = VisualForm(request.POST, request.FILES, instance=visual)
        if form.is_valid():
            form.save()
            return redirect('mis_visuales')
    else:
        form = VisualForm(instance=visual)
    return render(request, 'tienda/editar_visual.html', {'form': form})

@login_required
def eliminar_visual(request, visual_id):
    visual = get_object_or_404(Visual, id=visual_id, user=request.user)
    if request.method == 'POST':
        visual.delete()
        return redirect('mis_visuales')
    return render(request, 'tienda/eliminar_visual.html', {'visual': visual})

def buscar_visual(request):
    resultados = []
    if request.method == 'GET':
        form = BuscarVisualForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultados = Visual.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscarVisualForm()
    return render(request, 'tienda/buscar.html', {'form': form, 'resultados': resultados})

def about(request):
    return render(request, 'tienda/about.html')
