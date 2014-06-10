from django.db import models

# Create your models here.


class datospersonales(models.Model):
    nombre = models.CharField(max_length=150)
    puesto = models.CharField(max_length=150)
    foto =  models.FileField(upload_to='file')

    def __unicode__(self):
        return self.nombre
acciones = (
    ('Entrada', 'Entrada'),
    ('Salida', 'Salida'),)

class check(models.Model):

    nombre = models.ForeignKey(datospersonales)
    accion = models.CharField(max_length=10, choices=acciones)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)





def __unicode__(self):
        return self.nombre



