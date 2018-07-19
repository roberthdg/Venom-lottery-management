from django import forms
from .models import Cooperativa, Cliente, Credito, Pago, Garante
#from bootstrap3_datetime.widgets import DateTimePicker

class IngresarCooperativa(forms.ModelForm):
    class Meta:
        model = Cooperativa
        fields = ('ruc','nombre','correo')
        widgets = {
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def validar_ruc(self):
        ruc = self.cleaned_data.get('ruc')
        return ruc

    def validar_correo(self):
        email = self.cleaned_data.get('correo')
        email_base, provider = email.split("@")
        domain, extension = provider.split(".")
        return email

    def validar_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        return nombre

class IngresarCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        unique_together = ('ruc','cedula')
        fields = ('ruc','codigo_cliente','cedula','nombre', 'estado_juridico','fecha_nacimiento','direccion',
                  'telefono_fijo','telefono_celular','correo', 'deuda')
        widgets = {
            'ruc': forms.HiddenInput(),
            'codigo_cliente': forms.HiddenInput(),
            'deuda': forms.HiddenInput(),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_juridico': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'id': 'datepicker'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_fijo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_celular': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def validar_correo(self):
        email = self.cleaned_data.get('correo')
        email_base, provider = email.split("@")
        domain, extension = provider.split(".")
        return email

    def validar_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        return nombre

class IngresarGarante(forms.ModelForm):
     class Meta:
            model = Garante
            unique_together = ('codigo_credito','cedula')
            fields = ('codigo_credito','cedula','nombre','correo')
            widgets = {
                'codigo_credito': forms.HiddenInput(),
                'cedula': forms.TextInput(attrs={'class': 'form-control'}),
                'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                'correo': forms.TextInput(attrs={'class': 'form-control'}),
            }

class IngresarCredito(forms.ModelForm):
    class Meta:
        model = Credito


        fields = ('codigo_cliente','ruc','codigo_credito','fecha_concesion','fecha_vencimiento','tasa_interes','tipo',
                  'numero_cuotas', 'valor_cuota', 'frecuencia_pago','encaje', 'ahorro_programado', 'seguro','estado')
        widgets = {
            'ruc': forms.HiddenInput(),
            'codigo_cliente': forms.HiddenInput(),
            'codigo_credito': forms.HiddenInput(),
            'estado': forms.HiddenInput(),
            'fecha_concesion': forms.DateInput(attrs={'id': 'datepicker'}),
            'fecha_vencimiento': forms.DateInput(attrs={'id': 'datepicker2'}),
            'tasa_interes': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_cuotas': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_cuota': forms.TextInput(attrs={'class': 'form-control'}),
            'frecuencia_pago': forms.TextInput(attrs={'class': 'form-control'}),
            'encaje': forms.TextInput(attrs={'class': 'form-control'}),
            'ahorro_programado': forms.TextInput(attrs={'class': 'form-control'}),
            'seguro': forms.TextInput(attrs={'class': 'form-control'}),
        }

class IngresarPago(forms.ModelForm):
     class Meta:
            model = Pago
            fields = ('codigo_credito','tasa','tasa_mora','monto','fecha_pago')
            widgets = {
                'codigo_credito': forms.HiddenInput(),
                'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': "0.01"}),
                'tasa': forms.NumberInput(attrs={'class': 'form-control', 'step': "0.01"}),
                'tasa_mora': forms.NumberInput(attrs={'class': 'form-control','step': "0.01"}),
                'fecha_pago': forms.DateInput(attrs={'id': 'datepicker'}),
            }

