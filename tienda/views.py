from django.shortcuts import render, redirect
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


def crear_visual(request):
    if request.method == 'POST':
        form = VisualForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VisualForm()
    return render(request, 'tienda/visuales.html', {'form': form})


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

