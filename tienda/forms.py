from django import forms 
from .models import Categoria, Formato, Visual

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
        
        }
    

class FormatoForm(forms.ModelForm):
    class Meta:
        model = Formato
        fields = ['nombre', 'resolucion', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'resolucion': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
        }


class VisualForm(forms.ModelForm):
    class Meta:
        model = Visual
        fields = ['titulo', 'descripcion', 'categoria', 'formato', 'precio']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'formato': forms.Select(attrs={'class': 'form-select'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),

        }



class BuscarVisualForm(forms.Form):
    titulo = forms.CharField(
        label='Buscar Visual',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribi el titulo...'})
        )
    