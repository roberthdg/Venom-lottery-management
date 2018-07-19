from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def validar_tipo(request):
 l = request.user.groups.values_list('name',flat=True)
 if (l[0]=='cooperativas'):
        pagina='../inicio/'
 else:
        pagina='../lolazo'

 return redirect(pagina)

def cooperativas(request):
    nombre = 'holis'
    password = 'mongolis'
    args= {'usuario':nombre, 'password':password}
    return render(request, 'home.html', args)

def cooperativa_listado(request,ruc):
    return HttpResponse("<h2>Detalles de la coopetativa RUC: " + str(ruc) + "</h2>")

