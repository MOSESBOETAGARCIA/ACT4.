from django.db import models

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    fecha_ingreso = models.DateField()
    domicilio = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: EMPLEADO
# ==========================================
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    domicilio = models.TextField()
    fecha_ingreso = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
