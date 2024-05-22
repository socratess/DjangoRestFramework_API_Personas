from django.db import models

class persona(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False)
    apellido = models.CharField(max_length=255, blank=False, null=False)
    celular = models.IntegerField(blank=False, null=False)
    correo = models.EmailField(max_length=255,blank=False, null=False)

