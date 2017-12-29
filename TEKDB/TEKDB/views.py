from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import *

def get_related(request, model_name, id):
    from django.apps import apps
    import json
    if not (request.user.is_authenticated() and request.user.has_perm('tekdb.chage_%s' % model_name.lower())):
        return HttpResponse('Unauthorized', status=401)
    data = json.dumps([])
    try:
        model = apps.get_model('TEKDB', model_name)
        instance = model.objects.get(pk=id)
        if hasattr(instance, 'get_related_objects'):
            data = json.dumps(instance.get_related_objects(id))
    except:
        pass
    return HttpResponse(data, content_type='application/json')
