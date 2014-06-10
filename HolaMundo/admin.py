from HolaMundo.models import datospersonales
from HolaMundo.models import check

from django.contrib import admin

# Register your models here.

class detalle(admin.ModelAdmin):
    list_display = ("nombre",)



admin.site.register(datospersonales, detalle)
admin.site.register(check, detalle)


