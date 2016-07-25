from django.shortcuts import render
#from . import views
from views import ProyectoView, ProyectoSeleccionView
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    url(r'^pregunta(?P<id>[0-9]+)/$', csrf_exempt(ProyectoView.as_view()), name='member'),

    url(r'^pregunta/', csrf_exempt(ProyectoView.as_view()), name='member'),

    url(r'^seleccion(?P<id>[0-9]+)/$', csrf_exempt(ProyectoSeleccionView.as_view()), name='member'),

]
