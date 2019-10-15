from django.http import HttpResponse, Http404
from django.shortcuts import render
from dal import autocomplete
from django.db.models import Q
from .models import *

def get_related(request, model_name, id):
    from django.apps import apps
    import json
    if not (request.user.is_authenticated() and request.user.has_perm('TEKDB.change_%s' % model_name.lower())):
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

class PlaceResourceAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return PlacesResourceEvents.objects.none()
        qs = PlacesResourceEvents.objects.all()

        if self.q:
            qs = qs.filter(
                Q(placeid__indigenousplacename__icontains=self.q) |
                Q(placeid__englishplacename__icontains=self.q) |
                Q(resourceid__commonname__icontains=self.q) |
                Q(resourceid__indigenousname__icontains=self.q) |
                Q(resourceid__genus__icontains=self.q) |
                Q(resourceid__species__icontains=self.q)
            ).order_by('resourceid__commonname', 'placeid__indigenousplacename')

        return qs
