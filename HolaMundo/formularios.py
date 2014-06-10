from django.forms import ModelForm
from HolaMundo.models import check
from HolaMundo.models import datospersonales


class FormularioPersonas(ModelForm):
    class Meta:
        model = check
        fields = ['nombre', 'accion']



