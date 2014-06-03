from django.contrib import admin
from models import Seleccion, Grupo, Partido, SeleccionAdmin


admin.site.register(Seleccion, SeleccionAdmin)
admin.site.register(Partido)
admin.site.register(Grupo)

