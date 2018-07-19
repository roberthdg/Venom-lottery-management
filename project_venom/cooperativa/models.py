from django.db import models
from django.contrib.auth.models import User

class Cooperativa(models.Model):
    ruc = models.CharField(max_length=200, primary_key=True)
    nombre = models.CharField(max_length=200)
    razon_social = models.CharField(max_length=200, blank=True)
    estado_juridico = models.CharField(max_length=200, blank=True)
    provincia = models.CharField(max_length=200, blank=True)
    canton = models.CharField(max_length=200, blank=True)
    parroquia = models.CharField(max_length=200, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    telefono_fijo = models.CharField(max_length=200, blank=True)
    telefono_celular = models.CharField(max_length=200, blank=True)
    correo = models.CharField(max_length=200, blank=True)

    def __str__(self):
       return 'Cooperativa ' + self.nombre + ' (RUC: ' + self.ruc+')'

class Usuario_cooperativa(models.Model):
    usuario = models.OneToOneField(User)
    cooperativa = models.ForeignKey(Cooperativa)
    nivel_permiso = models.IntegerField()

class Gerente(models.Model):
    ruc = models.ForeignKey(Cooperativa,on_delete=models.CASCADE)
    id = models.CharField(max_length=200, primary_key=True)
    nombre = models.CharField(max_length=200)
    telefono_fijo = models.CharField(max_length=200)
    telefono_celular = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)

class Cliente(models.Model):
    ruc = models.ForeignKey(Cooperativa, on_delete=models.CASCADE)
    codigo_cliente = models.CharField(max_length=200, primary_key=True)
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=200)
    estado_juridico = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono_fijo = models.CharField(max_length=200)
    telefono_celular = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    deuda = models.FloatField()
    def __str__(self):
        return 'Nombre: '+self.nombre + ', Cédula: ' + str(self.cedula) + ', Cooperativa: ' + str(self.ruc.nombre)

class Credito(models.Model):
    codigo_cliente = models.ForeignKey(Cliente)
    ruc = models.ForeignKey(Cooperativa)
    codigo_credito = models.CharField(max_length=200, primary_key=True)
    fecha_concesion = models.DateField()
    fecha_vencimiento = models.DateField()
    tasa_interes = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    numero_cuotas = models.IntegerField()
    valor_cuota = models.FloatField()
    frecuencia_pago = models.IntegerField()
    encaje = models.FloatField()
    ahorro_programado = models.CharField(max_length=200)
    seguro = models.CharField(max_length=200)
    estado= models.CharField(max_length=200)
    def __str__(self):
        return ''+ self.codigo_credito + ' (cédula: ' + str(self.codigo_cliente.cedula) +')'

class Garante(models.Model):
    codigo_credito = models.ForeignKey(Credito)
    nombre = models.CharField(max_length=200)
    cedula = models.IntegerField()
    estado_juridico = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono_fijo = models.CharField(max_length=200)
    telefono_celular = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)

    def __str__(self):
        return ''+ self.nombre + ' (cédula: ' + str(self.cedula) +')'

class Pago(models.Model):
    codigo_credito = models.ForeignKey(Credito)
    tasa = models.CharField(max_length=200)
    tasa_mora = models.CharField(max_length=200)
    monto = models.FloatField()
    forma_pago = models.CharField(max_length=200)
    fecha_pago = models.DateField()

