from django import forms
from .models import Vuelo

class FormVueloCustom(forms.ModelForm):
    #campos del modelo
    class Meta:
        model = Vuelo
        fields = ('origen', 'destino', 'duracion')
        widgets = {
            'origen': forms.TextInput(attrs={'class': 'estilo_origen'}),
            'destino': forms.TextInput(attrs={'class': 'estilo_destino'}),
            'duracion': forms.TextInput(attrs={'class': 'estilo_duracion'}),
        }