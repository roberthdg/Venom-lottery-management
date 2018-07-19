from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, HttpResponseRedirect
from .models import Cooperativa, Cliente, Usuario_cooperativa, Credito, Pago, Garante
from .forms import IngresarCooperativa, IngresarCliente, IngresarCredito, IngresarGarante,IngresarPago
from django.utils.crypto import get_random_string


def validar_tipo(request):
 l = request.user.groups.values_list('name',flat=True)
 if (l[0]=='cooperativas'):
        pagina='../inicio/'
 else:
        pagina='../lolazo'

 return redirect(pagina)

#           Vistas del modelo Cooperativa

def cooperativa_listado(request):
    cooperativas_listado = Cooperativa.objects.all()
    context = {'cooperativas_listado': cooperativas_listado}
    return render(request,'cooperativa/listado.html',context)

def cooperativa_buscar(request,ruc):
    try:
        cooperativa = Cooperativa.objects.get(pk=ruc)
    except Cooperativa.DoesNotExist:
        raise Http404("Cooperativa no existe")
    return render(request, 'cooperativa/buscar.html',{'cooperativa': cooperativa} )

def cooperativa_ingresar(request):
    form = IngresarCooperativa(request.POST)
    titulo = 'Ingresar Cooperativa'
    if form.is_valid():
        instance = form.save()
        instance.save()
    context = {"titulo": titulo,
               "form": form
    }
    return render(request, 'cooperativa/ingresar.html',context )


#           Vistas del modelo Cliente


def cliente_ingresar(request):
        usuario = request.user
        usuario_cooperativa = Usuario_cooperativa.objects.get(usuario_id=usuario.id)
        codigo = get_random_string(length=32)
        form = IngresarCliente(request.POST or None, initial={'ruc': usuario_cooperativa.cooperativa, 'codigo_cliente': codigo, 'deuda':0})
        if form.is_valid():
            instance = form
            instance.save()
            return HttpResponseRedirect('/cooperativa/cliente/ingresar/aprobado')
        titulo = 'Ingresar Cliente'
        context = {"titulo": titulo,
                   "form": form
         }
        return render(request, 'cliente/ingresar.html', context)

def cliente_ingresar_exito(request):

    return render(request, 'cliente/ingresar_exito.html')

def cliente_buscar(request):
    titulo = 'Ingresar Cliente'
    if request.method == 'GET':
       search_query = request.GET.get('search_box', None)

    context = {"titulo": titulo,
               "form": search_query
    }
    return render(request, 'cliente/buscar.html',context )

def cliente_listado(request):
    cliente_listado = Cliente.objects.all()
    context = {'cliente_listado': cliente_listado}
    return render(request,'cliente/listado.html',context)

def datos_cliente(request,cedula):
    cliente = None
    match = True
    try:
        cliente = Cliente.objects.get(cedula=cedula)
    except Cliente.DoesNotExist:
        match = False
    return render(request,'cliente/datos_buscar.html', {'cliente'  :cliente, 'match' : match})

#    Vistas del crédito

def credito_buscar_cliente(request):
    return render(request, 'credito/ingresar.html')

def credito_ingresar_datos(request):
        cedula=request.GET['cedula']
        if cedula == '':
            return HttpResponseRedirect('/cooperativa/credito/ingresar')
        else:
            try:
                cliente = Cliente.objects.get(cedula=cedula)
            except Cliente.DoesNotExist:
                return HttpResponseRedirect('/cooperativa/credito/ingresar/error')
            usuario = request.user
            usuario_cooperativa = Usuario_cooperativa.objects.get(usuario_id=usuario.id)
            codigo = get_random_string(length=7)
            form = IngresarCredito(request.POST or None, initial={'estado':'Activo','ruc': usuario_cooperativa.cooperativa, 'codigo_cliente':cliente, 'codigo_credito': codigo})
            if form.is_valid():
                instance = form
                instance.save()

                c=str(instance['codigo_credito'].value())
                return HttpResponseRedirect('/cooperativa/credito/datos/?codigo='+c+'&n=1')
        context = {
                       "form": form
        }
        return render(request, 'credito/ingresar_datos.html', context)

def credito_buscar(request):
    titulo = 'Ingresar código del crédito'
    if request.method == 'GET':
       search_query = request.GET.get('search_box', None)

    context = {"titulo": titulo,
               "form": search_query
    }
    return render(request, 'credito/buscar.html',context )

def datos_credito(request):
    codigo=request.GET['codigo']
    n=request.GET['n']
    credito=None
    match = True
    garante_listado = Garante.objects.all()
    pago_listado = Pago.objects.all()
    try:
        credito = Credito.objects.get(codigo_credito=codigo)
    except Credito.DoesNotExist:
        match = False
    return render(request,'credito/datos_buscar.html', {'credito':credito, 'match' : match,
                                                        'n': n, 'garante_listado': garante_listado,
                                                        'pago_listado': pago_listado})


def credito_buscar_error(request):
    return render(request, 'credito/ingresar_error.html')


#    Vistas del garante

def pago_buscar_cliente(request):
    return render(request, 'pago/ingresar.html')

def garante_ingresar_datos(request):
        cedula=request.GET['cedula']
        if cedula == '':
            return HttpResponseRedirect('/cooperativa/pago/ingresar')
        else:
            try:
                cliente = Cliente.objects.get(cedula=cedula)
            except Cliente.DoesNotExist:
                return HttpResponseRedirect('/cooperativa/credito/ingresar/error')
            credito = Credito.objects.get(codigo_cliente=cliente,estado='Activo')
            form = IngresarPago(request.POST or None, initial={'codigo_credito': credito})
            if form.is_valid():
                instance = form
                instance.save()
                c=str(instance['codigo_credito'].value())
                return HttpResponseRedirect('/cooperativa/credito/datos/?codigo='+c+'&n=2')
        context = {
                       "form": form
        }
        return render(request, 'pago/ingresar_datos.html', context)


def garante_ingresar_error(request):
    return render(request, 'credito/ingresar_error.html')





#    Vistas del pago

def pago_buscar_cliente(request):
    return render(request, 'pago/ingresar.html')

def pago_ingresar_datos(request):
        cedula=request.GET['cedula']
        if cedula == '':
            return HttpResponseRedirect('/cooperativa/pago/ingresar')
        else:
            try:
                cliente = Cliente.objects.get(cedula=cedula)
            except Cliente.DoesNotExist:
                return HttpResponseRedirect('/cooperativa/pago/ingresar/error')
            try:
                credito = Credito.objects.get(codigo_cliente=cliente,estado='Activo')
            except Credito.DoesNotExist:
                return HttpResponseRedirect('/cooperativa/pago/ingresar/error')
            form = IngresarPago(request.POST or None, initial={'codigo_credito': credito})
            if form.is_valid():
                instance = form
                instance.save()
                c=str(instance['codigo_credito'].value())
                return HttpResponseRedirect('/cooperativa/credito/datos/?codigo='+c+'&n=2')
        context = {
                       "form": form
        }
        return render(request, 'pago/ingresar_datos.html', context)


def pago_buscar_error(request):
    return render(request, 'pago/ingresar_error.html')



