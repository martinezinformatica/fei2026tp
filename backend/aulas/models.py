from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank=False)
    apellido = models.CharField(max_length=128, null=False, blank=False)
    mostrar = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Materia(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank=False)
    cant_alumnos = models.IntegerField(default=0, null=False)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, db_column='id_carrera')
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, db_column='id_profesor')

    def __str__(self):
        return self.nombre


class Aula(models.Model):
    descripcion = models.CharField(max_length=128, null=False, blank=False)
    ubicacion = models.CharField(max_length=128, null=False, blank=False)  
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion
    
class ReservaAula(models.Model):
    id_aula = models.ForeignKey(Aula, on_delete=models.CASCADE, db_column='id_aula')
    fh_desde = models.DateTimeField(null=False)
    fh_hasta = models.DateTimeField(null=False)
    observacion = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f"Reserva Aula {self.id_aula_id} ({self.fh_desde})"


class HorarioMateria(models.Model):
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, db_column='id_materia')
    id_reserva = models.ForeignKey(ReservaAula, on_delete=models.CASCADE, db_column='id_reserva')
    fh_desde = models.DateTimeField(null=False)
    fh_hasta = models.DateTimeField(null=False)

    def __str__(self):
        return f"Horario Materia {self.id_materia_id}"