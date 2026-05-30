from django.contrib import admin
from .models import Carrera, Profesor, Materia, Aula, ReservaAula, HorarioMateria

admin.site.register(Carrera)
admin.site.register(Profesor)
admin.site.register(Materia)
admin.site.register(Aula)
admin.site.register(ReservaAula)
admin.site.register(HorarioMateria)