from django.contrib import admin
from .models import Cooperativa, Cliente, Gerente, Credito, Pago, Usuario_cooperativa, Garante

myModels = [Cooperativa, Usuario_cooperativa,Cliente, Gerente, Credito, Pago, Garante]

admin.site.register(myModels)