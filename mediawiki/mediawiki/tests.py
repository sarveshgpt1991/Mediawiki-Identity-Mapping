from django.http import HttpResponse, HttpResponseRedirect
from people.models import *
import json
import os

def Db(request, tablename, filename):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    data = open(BASE_DIR+'/media/db/'+filename+'.json')
    data = json.load(data)
    if tablename == 'name':
        for i in data:
            s = Name.objects.create(id=i['id'], name=i['name'])
            s.save()
    elif tablename == 'country':
        for i in data:
            s = Country.objects.create(id=i['id'], country=i['country'])
            s.save()
    elif tablename == 'email':
        for i in data:
            s = Email.objects.create(id=i['id'], email=i['email'])
            s.save()
    return HttpResponse("Done!")