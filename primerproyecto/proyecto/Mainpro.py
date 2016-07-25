from .models import Pregunta, Seleccion


class MainProyect():
    def __init__(self, request):
        self._request = request
        self._data = None
        self.response_data = {'error':[], 'data':{}}
        self.code = 200
        self._fields = ['pregunta_text','fecha']
        self.valid = 0

    def error_confirm(self):
        return True if len(self.response_data['error'])>0 else False

    #para listar un solo registro
    def get(self,id):
        try:
            one = Pregunta.objects.get(id=id)
            self.response_data['data'].update({
                'id':one.id,
                'pregunta':one.pregunta_text,
                'fecha':one.fecha if one.fecha else ''})
        except Exception as e:
             self.response_data['error'] = str(e)
             self.code = 500

    #para lsitar todos los registros
    def get_all(self):
        try:
            self.response_data['data'] = []
            users = Pregunta.objects.all()
            for one in users:
                data={
                    'id':one.id,
                    'pregunta':one.pregunta_text,
                    'fecha':one.fecha if one.fecha else ''}
                self.response_data['data'].append(data)
        except Exception as e:
             self.response_data['error'] = str(e)
             self.code = 500

    def post(self):
        try:
            self._data = dict((k,self._request.POST[k]) for k in self._fields if k in self._request.POST)
            self.valid=2
            self.validate()
            self.validar_pre()
            if not self.error_confirm():
                self._save()
        except Exception as e:
            print e
            self.code = 500
            self.response_data['error']=str(e)

    def validar_pre(self):
        if Pregunta.objects.filter(pregunta_text=self._request.POST['pregunta_text']).exists():
            self.response_data['error'] = 'Pregunta ya Existe'
            self.code = 409
            return
        else:self._data['pregunta_text'] = self.unicode_string(self._data['pregunta_text'])

    def validate(self):
        if self.valid == 2:
            for k in self._fields:
                if not k in self._request.POST:
                    self.response_data['error'].append('Field %s Required' % (k))
                    self.code = 409
        if 'pregunta_text' in self._request.POST and len(self._request.POST['pregunta_text'])!=0:
            if len(self._request.POST['pregunta_text'])>100:
                self.response_data['error'] = 'Pregunta Muy larga'
                self.code = 409
                return
        if 'fecha' in self._request.POST and len(self._request.POST['fecha'])!=0:
            if len(self._request.POST['fecha'])>200:
                self.response_data['error'] = 'Fecha muy larga'
                self.code = 409
                return
            else:self._data['fecha'] = str(self._data['fecha'])

#-- herramienta la uso para la decodicacion de los caracteres especiales --
    def unicode_string(self,string):
        try:
            st = unicode(string)
            st = st.encode('unicode_escape')
            return st
        except:
            return string

    def decode_string(self,string):
        try:
            return string.decode('unicode_escape')
        except:
            return string

    def put(self,kwargs):
        if 'id' in kwargs:
            self.valid=1
            self._data = dict((k,self._request.POST[k]) for k in self._fields if k in self._request.POST)
            self.validate()
            #self.validar_pre()
            if not self.error_confirm():
                self._data.update({'id':int(kwargs['id'])})
                self._save()
        else:
            self.response_data['error']='Id is Required'
            self.code = 500

    #eliminar un registro de usuario
    def delete(self,kwargs):
        if 'id' in kwargs:
            dele=Pregunta.objects.get(id=kwargs['id'])
            dele.delete()
        else:
            self.response_data['error']='Id is Required'
            self.code = 500

    def _save(self):
        if not 'id' in self._data:
            self.I = Pregunta(**self._data)
            self.I.save()
        else:
            upda = Pregunta.objects.filter(id=self._data['id']).update(**self._data)
            self.I = Pregunta.objects.get(id=self._data['id'])
        self.response_data['data'].update({
            'id':self.I.id,
            'pregunta':self.I.pregunta_text,
            'fecha':self.I.fecha})
        self.code = 201

class MainProyectS():
    def __init__(self, request):
        self._request = request
        self._data = None
        self.response_data = {'error':[], 'data':{}}
        self.code = 200
        self._fields = ['seleccion_text','fkpregunta_id']
        self.valid = 0

    def error_confirm(self):
        return True if len(self.response_data['error'])>0 else False

    def get(self,id):
        try:
            one = Pregunta.objects.get(id=id)
            sel = Seleccion.objects.all().filter(fkpregunta_id=id)
            self.response_data['data'] = []
            for obj in sel:
                data={
                    'id':obj.id,
                    'seleccion':obj.seleccion_text}
                self.response_data['data'].append(data)
        except Exception as e:
             self.response_data['error'] = str(e)
             self.code = 500
