from django.db import models

# Create your models here.
class Pregunta(models.Model):
    pregunta_text = models.CharField(max_length = 100)
    fecha = models.DateTimeField('fecha de publicacion')

    def __str__(self):              # codigo para evitar que salga el objeto como pregunta object
        return self.pregunta_text

class Seleccion(models.Model):
    seleccion_text = models.CharField(max_length = 200)
    fkpregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    def __str__(self):              # codigo para evitar que salga el objeto como pregunta object
        return self.seleccion_text
