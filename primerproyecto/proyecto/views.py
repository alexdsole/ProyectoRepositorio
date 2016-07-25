from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.http import QueryDict
from proyecto.Mainpro import  MainProyect,MainProyectS
import json
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.


class ProyectoView(View):
    def get(self, request, *args, **kwargs):
        _ge = MainProyect(request)
        #GET one
        if 'id' in kwargs:
            _ge.get(int(kwargs['id']))
        #GET all
        else:_ge.get_all()
        data = _ge.response_data
        data.update({'code':_ge.code})
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='application/json')

    def post(self, request, *args, **kwargs):
        _create = MainProyect(request)
        _create.post()
        data = _create.response_data
        data.update({'code':_create.code})
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='application/json')

    def delete(self, request, *args, **kwargs):
        request.POST=request.GET
        _de = MainProyect(request)
        _de.delete(kwargs)
        data = _de.response_data
        data.update({'code':_de.code})
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='application/json')

    def put(self, request, *args, **kwargs):
        request.POST = QueryDict(request.read())
        _update = MainProyect(request)
        _update.put(kwargs)
        data = _update.response_data
        data.update({'code':_update.code})
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='application/json')

class ProyectoSeleccionView(View):

    def get(self, request, *args, **kwargs):
        _ge = MainProyectS(request)
        if 'id' in kwargs:
            _ge.get(int(kwargs['id']))
        data = _ge.response_data
        data.update({'code':_ge.code})
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='application/json')
