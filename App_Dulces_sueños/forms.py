from django import forms
from .models import Modelo

class ModeloForm(forms.ModelForm):
    
    class Meta:
        model = Modelo
        fields = '__all__'
