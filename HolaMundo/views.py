from HolaMundo.models import datospersonales
from django.shortcuts import render_to_response
from HolaMundo.models import check
from HolaMundo.formularios import FormularioPersonas
from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.


def datos(request):
    nombre = datospersonales.objects.all()

    return  render_to_response('datos.html',{'lista':nombre})



def mostrarTabla(request):
    personas = check.objects.all()
    return render_to_response('tabla.html',{'personas': personas })






def formulario(request):
    if request.method=="POST":
        formulario=FormularioPersonas(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/")
    else:
        formulario=FormularioPersonas()
    return render(request, 'check.html', {'formulario': formulario})