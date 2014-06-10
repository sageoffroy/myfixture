from django.contrib import admin
from models import Seleccion, Grupo, Partido, SeleccionAdmin, Prode, Resultado, Jugador, Tecnico, Estadio


admin.site.register(Seleccion, SeleccionAdmin)
admin.site.register(Partido)
admin.site.register(Grupo)
admin.site.register(Prode)
admin.site.register(Resultado)
admin.site.register(Jugador)
admin.site.register(Tecnico)
admin.site.register(Estadio)


