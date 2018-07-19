from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

urlpatterns = [

   url(r'^iniciar_sesion/$', login, {'template_name':'usuario/login.html'}),
   url(r'^validar/$', views.validar_tipo, name='validar_tipo'),
   url(r'^inicio/$', login, {'template_name':'cooperativa/inicio.html'}, name='inicio'),
   url(r'^cerrar_sesion/$', logout, {'template_name':'/usuario/logout.html'}),

   url(r'^listado/$', views.cooperativa_listado, name=u'cooperativa_listado'),
   url(r'^buscar/(?P<ruc>[0-9]+)$', views.cooperativa_buscar, name=u'cooperativa_buscar'),
   url(r'^ingresar$', views.cooperativa_ingresar, name=u'cooperativa_ingresar'),

   url(r'^cliente/ingresar$', views.cliente_ingresar, name=u'cliente_ingresar'),
   url(r'^cliente/ingresar/aprobado$', views.cliente_ingresar_exito, name=u'cliente_ingresar_exito'),
   url(r'^cliente/listado/$', views.cliente_listado, name=u'cliente_listado'),
   url(r'^cliente/buscar$', views.cliente_buscar, name=u'cliente_buscar'),
   url(r'^cliente/datos/(?P<cedula>[0-9]+)$', views.datos_cliente, name=u'datos_cliente'),

   url(r'^credito/ingresar$', views.credito_buscar_cliente, name=u'credito_buscar_cliente'),
   url(r'^credito/ingresar/datos$', views.credito_ingresar_datos, name=u'credito_ingresar_datos'),
   url(r'^credito/datos/$', views.datos_credito, name=u'datos_credito'),
   url(r'^credito/buscar$', views.credito_buscar, name=u'credito_buscar'),
   url(r'^credito/ingresar/error/$', views.credito_buscar_error, name=u'credito_buscar_error'),

   url(r'^garante/ingresar/datos$', views.credito_ingresar_datos, name=u'credito_ingresar_datos'),
   url(r'^credito/ingresar/error/$', views.credito_buscar_error, name=u'credito_buscar_error'),


   url(r'^pago/ingresar$', views.pago_buscar_cliente, name=u'pago_buscar_cliente'),
   url(r'^pago/ingresar/datos$', views.pago_ingresar_datos, name=u'pago_ingresar_datos'),
   url(r'^pago/ingresar/error/$', views.pago_buscar_error, name=u'pago_buscar_error')



   ]