from django.db import models

# Create your models here.

class ProfesionDB(models.Model):
    nombre=models.CharField(max_length=75, verbose_name="nombre")

    def __str__(self) :
        return self.nombre
    
class AutorDB(models.Model):
    nombre = models.CharField(max_length=75, verbose_name="Nombre")
    fecha_nacimiento = models.DateField(verbose_name="fecha nacimiento", null=False, blank=False)
    fecha_fallecimiento = models.DateField(verbose_name="fecha de fallecimiento", null=True, blank=True)
    profesion = models.ManyToManyField(ProfesionDB, verbose_name="Profesion")


    class Meta:
        db_table = "Autores"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self) -> str:
        return self.nombre

class FraseDB(models.Model):
    frase = models.CharField(max_length=400, verbose_name="cita")
    autor_fk = models.ForeignKey(AutorDB, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Frase"
        verbose_name_plural = "Frases"