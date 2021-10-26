from django.http import HttpResponse, Http404
from django.shortcuts import render
from dal import autocomplete
from django.db.models import Q
from .models import *

def get_related(request, model_name, id):
    from django.apps import apps
    import json
    if not (request.user.is_authenticated and request.user.has_perm('TEKDB.change_%s' % model_name.lower())):
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

class CitationAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower
        if not self.request.user.is_authenticated:
            return Citations.objects.none()
        qs = Citations.objects.all()

        if self.q:
            qs = Citations.keyword_search(self.q)

        return qs.order_by(Lower('referencetype__documenttype'), Lower('title'), Lower('intervieweeid__firstname'), Lower('intervieweeid__lastname'), 'year')

class MediaAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower
        if not self.request.user.is_authenticated:
            return Media.objects.none()
        qs = Media.objects.all()

        if self.q:
            qs = qs.filter(
                Q(medianame__icontains=self.q) |
                Q(mediatype__mediatype__icontains=self.q) |
                Q(mediatype__mediacategory__icontains=self.q)
            )

        return qs.order_by(Lower('medianame'), Lower('mediatype__mediatype'))

class PlaceAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower
        if not self.request.user.is_authenticated:
            return Places.objects.none()
        qs = Places.objects.all()

        if self.q:
            qs = Places.keyword_search(self.q)

        return qs.order_by(Lower('indigenousplacename'), Lower('englishplacename'))

class PlaceResourceAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower
        if not self.request.user.is_authenticated:
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
            )

        return qs.order_by(Lower('resourceid__commonname'), Lower('placeid__indigenousplacename'))

class ResourceAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower
        if not self.request.user.is_authenticated:
            return Resources.objects.none()
        qs = Resources.objects.all()

        if self.q:
            qs = Resources.keyword_search(self.q)

        return qs.order_by(Lower('commonname'))

class ResourceActivityAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower
        if not self.request.user.is_authenticated:
            return ResourcesActivityEvents.objects.none()
        qs = ResourcesActivityEvents.objects.all()

        if self.q:
            qs = qs.filter(
                Q(placeresourceid__placeid__indigenousplacename__icontains=self.q) |
                Q(placeresourceid__placeid__englishplacename__icontains=self.q) |
                Q(placeresourceid__resourceid__commonname__icontains=self.q) |
                Q(placeresourceid__resourceid__indigenousname__icontains=self.q) |
                Q(placeresourceid__resourceid__genus__icontains=self.q) |
                Q(placeresourceid__resourceid__species__icontains=self.q) |
                Q(activityshortdescription__activity__icontains=self.q)
            )

        return qs.order_by(Lower('placeresourceid__resourceid__commonname'), Lower('placeresourceid__placeid__indigenousplacename'), Lower('activityshortdescription__activity'))
