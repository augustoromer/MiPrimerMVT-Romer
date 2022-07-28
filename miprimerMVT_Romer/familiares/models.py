from django.db import models

class Familiares (models.Model):
    dni = models.IntegerField() #unique=True pero se rompe al darle la segunda vez al server. probé agregarle un try/except al error pero caigo en el hecho de que pierde utilidad cuando los datos no lo carga el usuario que ve la página
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    parentesco = models.CharField(max_length=50)
    rama_familiar = models.CharField(max_length=50, default='Sin relación ascendente')

