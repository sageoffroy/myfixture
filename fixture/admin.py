from django.contrib import admin
from models import Seleccion, Grupo, Partido, SeleccionAdmin, Prode, Resultado


admin.site.register(Seleccion, SeleccionAdmin)
admin.site.register(Partido)
admin.site.register(Grupo)
admin.site.register(Prode)
admin.site.register(Resultado)

