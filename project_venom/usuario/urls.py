from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^iniciar_sesion/$', login, {'template_name':'login.html'}),
    url(r'^validar/$', views.validar_tipo, name='validar_tipo'),
    url(r'^inicio/$', login, {'template_name':'plantilla_inicio.html'}),
    url(r'^cerrar_sesion/$', logout, {'template_name':'logout.html'}),
    url(r'^deudor/(?P<codigo_deudor>)$', views.validar_tipo, name='validar_tipo'),


]