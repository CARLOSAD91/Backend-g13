from django import forms

class RecetaForm(forms.Form):
  titulo = forms.CharField(label='Título', max_length=100, required=True)
  ingredientes = forms.CharField(label='Ingredientes', widget=forms.Textarea)
  preparacion = forms.CharField(label='Preparación', widget=forms.Textarea)
  autor = forms.CharField(label='Autor', max_length=100, required=True)
  