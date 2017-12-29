from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.gis.admin import GeoModelAdmin, OSMGeoAdmin
from django.utils.translation import ugettext, ugettext_lazy as _
import nested_admin

from .models import *

from TEKDB.settings import ADMIN_SITE_HEADER
admin.site.site_header = ADMIN_SITE_HEADER

from TEKDB.settings import BASE_DIR

#############
### FORMS ###
#############
class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        # widgets = {
        #     'medialink':forms.FileInput
        # }
        fields = '__all__'

class PlacesResourceEventForm(forms.ModelForm):
    class Meta:
        model = PlacesResourceEvents
        widgets = {
            'relationshipdescription': forms.Textarea
        }
        fields = '__all__'

class MediaCitationEventsForm(forms.ModelForm):
    class Meta:
        model = MediaCitationEvents
        widgets = {
            'relationshipdescription': forms.Textarea
        }
        fields = '__all__'

class PlacesCitationEventsForm(forms.ModelForm):
    class Meta:
        model = PlacesCitationEvents
        widgets = {
            'relationshipdescription': forms.Textarea
        }
        fields = '__all__'

class PlacesMediaEventsForm(forms.ModelForm):
    class Meta:
        model = PlacesMediaEvents
        widgets = {
            'relationshipdescription': forms.Textarea
        }
        fields = '__all__'

class PlacesResourceCitationEventsForm(forms.ModelForm):
    class Meta:
        model = PlacesResourceCitationEvents
        widgets = {
            'relationshipdescription': forms.Textarea
        }
        fields = '__all__'

class PlacesResourceMediaEventsForm(forms.ModelForm):
    class Meta:
        model = PlacesResourceMediaEvents
        widgets = {
            'relationshipdescription': forms.Textarea
        }
        fields = '__all__'

class ResourceActivityMediaEventsForm(forms.ModelForm):
    class Meta:
        model = ResourceActivityMediaEvents
        widgets = {
            'relationshipdescription': forms.Textarea
        }
        fields = '__all__'

class ResourceActivityCitationEventsForm(forms.ModelForm):
    class Meta:
        model = ResourceActivityCitationEvents
        widgets = {
            'relationshipdescription': forms.Textarea
        }
        fields = '__all__'

class ResourceResourceEventsForm(forms.ModelForm):
    class Meta:
        model = ResourceResourceEvents
        widgets = {
            'relationshipdescription': forms.Textarea
        }
        fields = '__all__'

class ResourcesCitationEventsForm(forms.ModelForm):
    class Meta:
        model = ResourcesCitationEvents
        widgets = {
            'relationshipdescription': forms.Textarea
        }
        fields = '__all__'

class ResourcesMediaEventsForm(forms.ModelForm):
    class Meta:
        model = ResourcesMediaEvents
        widgets = {
            'relationshipdescription': forms.Textarea
        }
        fields = '__all__'

###############
### INLINES ###
###############

#### ACTIVITIES ####
class ResourcesactivitymediaeventsInline(admin.TabularInline):
    model = ResourceActivityMediaEvents
    fields = ('mediaid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'Related Media'

class NestedResourcesactivitymediaeventsInline(nested_admin.NestedTabularInline):
    model = ResourceActivityMediaEvents
    fields = ('mediaid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'Related Media'

class ResourcesactivitycitationeventsInline(admin.TabularInline):
    model = ResourceActivityCitationEvents
    fields = ('citationid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'Related Bibliographic Sources'

class NestedResourcesactivitycitationeventsInline(nested_admin.NestedTabularInline):
    model = ResourceActivityCitationEvents
    fields = ('citationid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'Related Bibliographic Sources'

#### PLACESRESOURCES ####
class NestedPlacesresourcecitationeventsInline(nested_admin.NestedTabularInline):
    model = PlacesResourceCitationEvents
    fields = ('citationid','relationshipdescription','pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related Bibliographic Sources'
    form = PlacesResourceCitationEventsForm

class NestedPlacesresourcemediaeventsInline(nested_admin.NestedTabularInline):
    model = PlacesResourceMediaEvents
    fields = ('mediaid','relationshipdescription','pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related media'
    form = PlacesResourceMediaEventsForm

class NestedPlaceresourcelocalityeventInline(nested_admin.NestedTabularInline):
    model = LocalityPlaceResourceEvent
    fields = ('localityid',)
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related localities'

class NestedPlacesresourceactivityeventInline(nested_admin.NestedStackedInline):
    model = ResourcesActivityEvents
    fieldsets = (
        ('', {
            'fields': (('participants', 'technique','relationshipdescription'),
                ('activityshortdescription', 'activitylongdescription', )
            )
        }),
    )
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related Activities'
    inlines = [
        NestedResourcesactivitycitationeventsInline,
        NestedResourcesactivitymediaeventsInline,
    ]

#### PLACES ####
class NestedPlacesalternativenameInline(nested_admin.NestedTabularInline):
    model = PlaceAltIndigenousName
    fields = ('altindigenousnameid', 'altindigenousname')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'alternate names'

class PlaceGISSelectionsInline(nested_admin.NestedTabularInline):
    model = PlaceGISSelections
    fields = ('placelabel', 'sourcefc')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'Place GIS Selections'

class NestedPlacesresourceeventsInline(nested_admin.NestedStackedInline):
    model = PlacesResourceEvents
    fieldsets = (
        ('', {
            'fields': ('resourceid', 'relationshipdescription',
                ('partused', 'customaryuse', 'barterresource'),
                ('season', 'timing'),
                ('january', 'february', 'march'), ('april', 'may', 'june'),
                ('july', 'august', 'september'), ('october', 'november',
                'december'), 'year', 'islocked'
            )
        }),
    )
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related resources'
    form = PlacesResourceEventForm
    inlines = [
        NestedPlacesresourcecitationeventsInline,
        NestedPlacesresourcemediaeventsInline,
        # NestedPlaceresourcelocalityeventInline,
        NestedPlacesresourceactivityeventInline,
    ]

class NestedPlaceslocalityInline(nested_admin.NestedTabularInline):
    model = Locality
    fields = ('indigenousname', 'englishname', 'localitytype')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related localities'

class NestedPlacesmediaeventsInline(nested_admin.NestedTabularInline):
    model = PlacesMediaEvents
    fields = ('mediaid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related media'
    form = PlacesMediaEventsForm

class NestedPlacescitationeventsInline(nested_admin.NestedTabularInline):
    model = PlacesCitationEvents
    fields = ('citationid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    max_num = 9999
    verbose_name_plural = 'related Bibliographic Sources'
    form = PlacesCitationEventsForm

#### CITATIONS ####
class CitationplacesresourceeventsInline(admin.TabularInline):
    model = PlacesResourceCitationEvents
    fields = ('placeresourceid','relationshipdescription','pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related place-resources'
    form = PlacesResourceCitationEventsForm

class CitationplaceseventsInline(admin.TabularInline):
    model = PlacesCitationEvents
    fields = ('placeid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    form = PlacesCitationEventsForm
    verbose_name_plural = 'related places'

class CitationresourceseventsInline(admin.TabularInline):
    model = ResourcesCitationEvents
    fields = ('resourceid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    form = ResourcesCitationEventsForm
    verbose_name_plural = 'related resources'

class CitationmediaeventsInline(admin.TabularInline):
    model = MediaCitationEvents
    fields = ('mediaid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    form = MediaCitationEventsForm
    verbose_name_plural = 'related media'

class CitationresourcesactivityeventsInline(admin.TabularInline):
    model = ResourceActivityCitationEvents
    fields = ('resourceactivityid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related activities'

#### MEDIA ####
class MediaplaceseventsInline(admin.TabularInline):
    model = PlacesMediaEvents
    fields = ('placeid','relationshipdescription','pages')
    extra = 0
    classes = ['collapse', 'open']
    form = PlacesMediaEventsForm
    verbose_name_plural = 'related places'

class MediacitationeventsInline(admin.TabularInline):
    model = MediaCitationEvents
    fields = ('citationid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    form = MediaCitationEventsForm
    verbose_name_plural = 'related Bibliographic Sources'

class MediaresourceseventsInline(admin.TabularInline):
    model = ResourcesMediaEvents
    fields = ('resourceid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    form = ResourcesMediaEventsForm
    verbose_name_plural = 'related resources'

class MediaplacesresourceeventsInline(admin.TabularInline):
    model = PlacesResourceMediaEvents
    fields = ('placeresourceid','relationshipdescription','pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related place-resources'
    form = PlacesResourceMediaEventsForm

class MediaresourcesactivityeventsInline(admin.TabularInline):
    model = ResourceActivityMediaEvents
    fields = ('resourceactivityid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related activities'

#### RESOURCES ####
class NestedResourcesMediaEventsInline(nested_admin.NestedTabularInline):
    model = ResourcesMediaEvents
    fields = ('mediaid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related media'
    form = ResourcesMediaEventsForm

class NestedResourcesCitationEventsInline(nested_admin.NestedTabularInline):
    model = ResourcesCitationEvents
    fields = ('citationid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related Bibliographic Sources'
    form = ResourcesCitationEventsForm

class NestedResourcesPlaceEventsInline(nested_admin.NestedStackedInline):
    model = PlacesResourceEvents
    fieldsets = (
        ('', {
            'fields': ('placeid', 'relationshipdescription',
                ('partused', 'customaryuse', 'barterresource'),
                ('season', 'timing'),
                ('january', 'february', 'march'), ('april', 'may', 'june'),
                ('july', 'august', 'september'), ('october', 'november',
                'december'), 'year', 'islocked'
            )
        }),
    )
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related places'
    form = PlacesResourceEventForm
    inlines = [
        NestedPlacesresourcecitationeventsInline,
        NestedPlacesresourcemediaeventsInline,
        # NestedPlaceresourcelocalityeventInline,
        NestedPlacesresourceactivityeventInline,
    ]
class ResourcesPlaceEventsStackedInline(admin.StackedInline):
    model= PlacesResourceEvents

class NestedResourceResourceEventsInline(nested_admin.NestedTabularInline):
    model = ResourceResourceEvents
    fields = ('altresourceid', 'relationshipdescription')
    fk_name = 'resourceid'
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related resources'
    form = ResourceResourceEventsForm

class NestedResourceAltIndigenousNameInline(nested_admin.NestedTabularInline):
    model = ResourceAltIndigenousName
    fields = ('resourceid', 'altindigenousname')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'Alternate Name'

#### LOCALITIES ####
class LocalityplaceresourceeventInline(admin.TabularInline):
    model = LocalityPlaceResourceEvent
    fields = ('placeresourceid',)
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related place-resources'

class LocalityGISSelectionsInline(admin.TabularInline):
    model = LocalityGISSelections
    fields = ('localitylabel', 'sourcefc')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'Locality GIS Selections'

####################
### MODEL ADMINS ###
####################
#### PROXY MODELS ####
class RecordAdminProxy(admin.ModelAdmin):
    readonly_fields = ('enteredbyname', 'enteredbytribe','enteredbytitle','enteredbydate',
    'modifiedbyname','modifiedbytribe','modifiedbytitle','modifiedbydate')

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if hasattr(instance, 'enteredbyname'):
            if instance.enteredbyname == None:
                instance.enteredbyname = request.user.username
                instance.enteredbytribe = request.user.affiliation
                instance.enteredbytitle = request.user.title
            instance.modifiedbyname = request.user.username
            instance.modifiedbytribe = request.user.affiliation
            instance.modifiedbytitle = request.user.title
        instance.save()
        return instance

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if hasattr(instance, 'enteredbyname'):
                if instance.enteredbyname == None:
                    instance.enteredbyname = request.user.username
                    instance.enteredbytribe = request.user.affiliation
                    instance.enteredbytitle = request.user.title
                instance.modifiedbyname = request.user.username
                instance.modifiedbytribe = request.user.affiliation
                instance.modifiedbytitle = request.user.title
            instance.save()

class NestedRecordAdminProxy(nested_admin.NestedModelAdmin):
    readonly_fields = ('enteredbyname', 'enteredbytribe','enteredbytitle','enteredbydate',
    'modifiedbyname','modifiedbytribe','modifiedbytitle','modifiedbydate')

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if hasattr(instance, 'enteredbyname'):
            if instance.enteredbyname == None:
                instance.enteredbyname = request.user.username
                instance.enteredbytribe = request.user.affiliation
                instance.enteredbytitle = request.user.title
            instance.modifiedbyname = request.user.username
            instance.modifiedbytribe = request.user.affiliation
            instance.modifiedbytitle = request.user.title
        instance.save()
        return instance

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if hasattr(instance, 'enteredbyname'):
                if instance.enteredbyname == None:
                    instance.enteredbyname = request.user.username
                    instance.enteredbytribe = request.user.affiliation
                    instance.enteredbytitle = request.user.title
                instance.modifiedbyname = request.user.username
                instance.modifiedbytribe = request.user.affiliation
                instance.modifiedbytitle = request.user.title
            instance.save()

#### RECORD MODELS ####
class RecordModelAdmin(admin.ModelAdmin):
    record_form = '%s/TEKDB/templates/admin/RecordForm.html' % BASE_DIR
    add_form_template = record_form
    change_form_template = record_form

    def change_view(self, request, object_id, form_url='', extra_context={}):
        object_instance = self.model.objects.get(pk=object_id)
        extra_context['related_objects'] = object_instance.get_related_objects(object_id)
        return super(RecordModelAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

class CitationsAdmin(RecordAdminProxy):
    list_display = ('referencetype','title','referencetext',
    'modifiedbyname','modifiedbydate','enteredbyname','enteredbydate')
    fieldsets = (
        (None, {
            'classes': ('citation-ref-type',),
            'fields': ('referencetype',)
        }),
        ('Book', {
            'classes': ('citation-book-form',),
            'fields': (
                'title',
                ('authorprimary', 'year'),
                'authorsecondary',
                ('publisher', 'publishercity'),
                'referencetext',
                'comments'
            )
        }),
        ('Edited Volume', {
            'classes': ('citation-volume-form',),
            'fields': (
                'title',
                ('authorprimary', 'year'),
                'authorsecondary',
                ('publisher', 'publishercity'),
                'seriestitle',
                ('seriesvolume','serieseditor'),
                'referencetext',
                'comments'
            )
        }),
        ('Interview', {
            'classes': ('citation-interview-form',),
            'fields': (
                ('intervieweeid', 'year'),
                'interviewerid',
                'placeofinterview',
                'referencetext',
                'comments'
            )
        }),
        ('Other', {
            'classes': ('citation-other-form',),
            'fields': (
                'title',
                ('authorprimary', 'year'),
                'authorsecondary',
                ('publisher', 'publishercity'),
                'seriestitle',
                ('seriesvolume','serieseditor'),
                ('journal', 'journalpages'),
                'preparedfor',
                'referencetext',
                'comments'
            )
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        })
    )

    add_form_template = '%s/TEKDB/templates/admin/CitationsForm.html' % BASE_DIR
    change_form_template = '%s/TEKDB/templates/admin/CitationsForm.html' % BASE_DIR
    inlines = [
        CitationplaceseventsInline,
        CitationresourceseventsInline,
        CitationmediaeventsInline,
        CitationplacesresourceeventsInline,
        CitationresourcesactivityeventsInline,
    ]
    search_fields = (
        'referencetype__documenttype', 'intervieweeid__firstname',
        'intervieweeid__lastname', 'interviewerid__lastname',
        'interviewerid__firstname', 'authortype__authortype',
        'interviewerid__village', 'intervieweeid__village',
        'interviewerid__relationshiptootherpeople',
        'intervieweeid__relationshiptootherpeople',
        'referencetext', 'authorprimary', 'authorsecondary',
        'placeofinterview', 'title', 'seriestitle',
        'seriesvolume', 'serieseditor', 'publisher',
        'publishercity', 'preparedfor', 'comments',
        'journal',
        'enteredbyname', 'enteredbytribe', 'modifiedbyname',
        'modifiedbytribe'
    )

class MediaAdmin(RecordAdminProxy):
    readonly_fields = ('medialink',
    'enteredbyname', 'enteredbytribe','enteredbytitle','enteredbydate',
    'modifiedbyname','modifiedbytribe','modifiedbytitle','modifiedbydate')
    list_display = ('medianame','mediatype','modifiedbyname','modifiedbydate',
    'enteredbyname','enteredbydate')
    fieldsets = (
        (None, {
            'fields': (('medianame','mediatype','limitedaccess'),'mediafile','medialink','mediadescription')
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        }),
    )
    from TEKDB.settings import BASE_DIR
    add_form_template = '%s/TEKDB/templates/admin/MediaForm.html' % BASE_DIR
    change_form_template = '%s/TEKDB/templates/admin/MediaForm.html' % BASE_DIR
    inlines = [
        MediaplaceseventsInline,
        MediacitationeventsInline,
        MediaresourceseventsInline,
        MediaplacesresourceeventsInline,
        MediaresourcesactivityeventsInline,
    ]
    search_fields = (
        'medianame', 'mediadescription', 'medialink',
        'mediatype__mediatype', 'mediatype__mediacategory',
        'enteredbyname', 'enteredbytribe', 'modifiedbyname',
        'modifiedbytribe'
    )
    form = MediaForm

class PlacesAdmin(NestedRecordAdminProxy, OSMGeoAdmin, RecordModelAdmin):
    list_display = ('indigenousplacename','englishplacename','modifiedbyname',
    'modifiedbydate','enteredbyname','enteredbydate')
    fieldsets = (
        (None, {
            'fields':(
                ('indigenousplacename','indigenousplacenamemeaning'),
                'englishplacename',
                ('planningunitid','primaryhabitat'),
                'tribeid',
                'geometry'
            )
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
                ('Source','DigitizedBy','DigitizedDate')
            )
        }),
    )

    search_fields = (
        'englishplacename', 'indigenousplacename', 'indigenousplacenamemeaning',
        'planningunitid__planningunitname', 'primaryhabitat__habitat',
        'tribeid__tribeunit','tribeid__tribe','tribeid__federaltribe',
        'enteredbyname', 'enteredbytribe', 'modifiedbyname',
        'modifiedbytribe'
    )

    from TEKDB.settings import DATABASE_GEOGRAPHY
    #TODO: check SRID from settings, set lat/lon in 4326, then convert to 3857 if necessary
    default_lon = DATABASE_GEOGRAPHY['default_lon']
    default_lat = DATABASE_GEOGRAPHY['default_lat']
    default_zoom = DATABASE_GEOGRAPHY['default_zoom']
    map_template = DATABASE_GEOGRAPHY['map_template']

class ResourcesAdmin(NestedRecordAdminProxy):
    list_display = ('commonname','indigenousname', 'modifiedbyname',
        'modifiedbydate','enteredbyname','enteredbydate')
    fieldsets = (
        (None, {
            'fields':(
                ('commonname', 'indigenousname'),
                ('genus', 'species'),
                'resourceclassificationgroup'
            )
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        }),
    )
    inlines = [
        # ResourcesActivityEventsInline,        #tied to place-resource
        NestedResourcesMediaEventsInline,
        NestedResourcesCitationEventsInline,

        NestedResourcesPlaceEventsInline,     #Original
        # ResourcesPlaceEventsStackedInline,

        NestedResourceResourceEventsInline,
        NestedResourceAltIndigenousNameInline,
        # ResourceGISSelectionsInline,          #TODO: make this work
    ]
    search_fields = (
        'commonname', 'indigenousname', 'genus', 'species',
        'resourceclassificationgroup__resourceclassificationgroup',
        'enteredbyname', 'enteredbytribe', 'modifiedbyname',
        'modifiedbytribe'
    )
    ordering = ('commonname',)

class ResourcesActivityEventsAdmin(RecordAdminProxy):
    list_display = ('placeresourceid', 'relationshipdescription',
    'modifiedbyname','modifiedbydate', 'enteredbyname','enteredbydate')
    fieldsets = (
        (None, {
            'fields': ('placeresourceid',)
        }),
        ('Activity', {
            'fields': (('participants', 'technique'), 'relationshipdescription', 'activityshortdescription', 'activitylongdescription')
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        }),
    )
    search_fields = (
        'placeresourceid__resourceid__commonname', 'placeresourceid__placeid__englishplacename',
        'placeresourceid__placeid__indigenousplacename', 'relationshipdescription',
        'activityshortdescription__activity', 'activitylongdescription',
        'participants__participants', 'technique__techniques',
        # 'customaryuse__usedfor', 'gear', 'timing__timing', 'timingdescription',
        #'partused__partused',
        'enteredbyname', 'enteredbytribe', 'enteredbytitle', 'modifiedbyname',
        'modifiedbytribe', 'modifiedbytitle'
    )
    inlines = [
        ResourcesactivitycitationeventsInline,
        ResourcesactivitymediaeventsInline,
    ]

class LocalityAdmin(RecordAdminProxy, OSMGeoAdmin):
    list_display = ('placeid', 'englishname', 'indigenousname',
    'modifiedbyname','modifiedbydate', 'enteredbyname','enteredbydate')
    fieldsets = (
        (None, {
            'fields': ('placeid', 'englishname', 'indigenousname', 'geometry')
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
                ('Source','DigitizedBy','DigitizedDate')
            )
        }),
    )
    search_fields = ('placeid__indigenousplacename', 'placeid__englishplacename',
    'englishname', 'indigenousname', 'enteredbyname', 'enteredbytribe',
    'enteredbytitle', 'modifiedbyname', 'modifiedbytribe', 'modifiedbytitle')
    inlines = [
        LocalityplaceresourceeventInline,
        LocalityGISSelectionsInline,
    ]
    from TEKDB.settings import DATABASE_GEOGRAPHY
    default_lon = DATABASE_GEOGRAPHY['default_lon']
    default_lat = DATABASE_GEOGRAPHY['default_lat']
    default_zoom = DATABASE_GEOGRAPHY['default_zoom']
    map_template = DATABASE_GEOGRAPHY['map_template']

#### RELATIONSHIP MODELS ####
class PlacesResourceEventsAdmin(NestedRecordAdminProxy):
    list_display = ('placeid', 'resourceid', 'partused', 'season','enteredbyname','enteredbydate','modifiedbyname','modifiedbydate')
    fieldsets = (
        ('', {
            'fields': (('placeid', 'resourceid'),'relationshipdescription',
                ('partused', 'barterresource'),
                ('season', 'timing'),
                ('january', 'february', 'march', 'april', 'may', 'june'),
                ('july', 'august', 'september', 'october', 'november',
                'december'), 'year', 'islocked'
            )
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        }),
    )
    form=PlacesResourceEventForm
    inlines = [
        NestedPlacesresourcecitationeventsInline,
        NestedPlacesresourcemediaeventsInline,
        # NestedPlaceresourcelocalityeventInline,
        NestedPlacesresourceactivityeventInline,
    ]

class MediaCitationEventsAdmin(RecordAdminProxy):
    list_display = ('mediaid','citationid','enteredbyname','enteredbydate','modifiedbyname','modifiedbydate')
    fieldsets = (
        ('', {
            'fields': (('mediaid','citationid'), 'relationshipdescription','pages')
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        })
    )
    form = MediaCitationEventsForm

class PlacesCitationEventsAdmin(RecordAdminProxy):
    list_display = ('placeid','citationid','enteredbyname','enteredbydate','modifiedbyname','modifiedbydate')
    fieldsets = (
        ('', {
            'fields': (('placeid','citationid'), 'relationshipdescription','pages')
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        })
    )
    form = PlacesCitationEventsForm

class PlacesMediaEventsAdmin(RecordAdminProxy):
    list_display = ('placeid','mediaid','enteredbyname','enteredbydate','modifiedbyname','modifiedbydate')
    fieldsets = (
        ('', {
            'fields': (('placeid','mediaid'), 'relationshipdescription','pages')
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        })
    )
    form = PlacesMediaEventsForm

class PlacesResourceCitationEventsAdmin(RecordAdminProxy):
    list_display = ('placeresourceid','citationid','enteredbyname','enteredbydate','modifiedbyname','modifiedbydate')
    fieldsets = (
        ('', {
            'fields': (('placeresourceid','citationid'), 'relationshipdescription','pages')
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        })
    )
    form = PlacesResourceCitationEventsForm

class PlacesResourceMediaEventsAdmin(RecordAdminProxy):
    list_display = ('placeresourceid','mediaid','enteredbyname','enteredbydate','modifiedbyname','modifiedbydate')
    fieldsets = (
        ('', {
            'fields': (('placeresourceid','mediaid'), 'relationshipdescription','pages')
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        })
    )
    form = PlacesResourceMediaEventsForm

class ResourceActivityCitationEventsAdmin(RecordAdminProxy):
    list_display = ('resourceactivityid','citationid','enteredbyname','enteredbydate','modifiedbyname','modifiedbydate')
    fieldsets = (
        ('', {
            'fields': (('resourceactivityid','citationid'), 'relationshipdescription','pages')
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        })
    )
    form = ResourceActivityCitationEventsForm

class ResourceActivityMediaEventsAdmin(RecordAdminProxy):
    list_display = ('resourceactivityid','mediaid','enteredbyname','enteredbydate','modifiedbyname','modifiedbydate')
    fieldsets = (
        ('', {
            'fields': (('resourceactivityid','mediaid'), 'relationshipdescription','pages')
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        })
    )
    form = ResourceActivityMediaEventsForm

class ResourceResourceEventsAdmin(RecordAdminProxy):
    list_display = ('resourceid','altresourceid','enteredbyname','enteredbydate','modifiedbyname','modifiedbydate')
    fieldsets = (
        ('', {
            'fields': (('resourceid','altresourceid'), 'relationshipdescription')
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        })
    )
    form = ResourceResourceEventsForm

class ResourcesCitationEventsAdmin(RecordAdminProxy):
    list_display = ('resourceid','citationid','enteredbyname','enteredbydate','modifiedbyname','modifiedbydate')
    fieldsets = (
        ('', {
            'fields': (('resourceid','citationid'), 'relationshipdescription', 'pages')
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        })
    )
    form = ResourcesCitationEventsForm

class ResourcesMediaEventsAdmin(RecordAdminProxy):
    list_display = ('resourceid','mediaid','enteredbyname','enteredbydate','modifiedbyname','modifiedbydate')
    fieldsets = (
        ('', {
            'fields': (('resourceid','mediaid'), 'relationshipdescription', 'pages')
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        })
    )
    form = ResourcesMediaEventsForm

class LocalityPlaceResourceEventAdmin(RecordAdminProxy):
    list_display = ('localityid','placeresourceid','enteredbyname','enteredbydate','modifiedbyname','modifiedbydate')
    fieldsets = (
        ('', {
            'fields': (('localityid','placeresourceid'),)
        }),
        ('History', {
            'fields': (
                ('enteredbyname','enteredbytitle','enteredbytribe','enteredbydate'),
                ('modifiedbyname','modifiedbytitle','modifiedbytribe','modifiedbydate'),
            )
        })
    )

#####################
#### AUTH MODELS ####
#####################
class UsersAdmin(UserAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'affiliation',
        'accesslevel','title','last_login', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        (_('Personal info'), {'fields': (
            'first_name', 'last_name', 'email', 'affiliation', 'title',
        )}),
        (_('Permissions'), {'fields': ('accesslevel',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = (
        'username', 'first_name', 'last_name', 'affiliation', 'email'
        'title', 'accesslevel__accesslevel'
    )

admin.site.register(Citations, CitationsAdmin)
# admin.site.register(Locality, LocalityAdmin)
# admin.site.register(LocalityGISSelections)
# admin.site.register(LocalityPlaceResourceEvent, LocalityPlaceResourceEventAdmin)
admin.site.register(LookupActivity)
admin.site.register(LookupCustomaryUse)
admin.site.register(LookupHabitat)
# admin.site.register(LookupLocalityType)
admin.site.register(LookupMediaType)
admin.site.register(LookupParticipants)
admin.site.register(LookupPartUsed)
admin.site.register(LookupPlanningUnit)
admin.site.register(LookupReferenceType)
admin.site.register(LookupResourceGroup)
admin.site.register(LookupSeason)
admin.site.register(LookupTechniques)
admin.site.register(LookupTiming)
admin.site.register(LookupTribe)
admin.site.register(Media, MediaAdmin)
admin.site.register(MediaCitationEvents, MediaCitationEventsAdmin)
admin.site.register(People)
admin.site.register(PlaceAltIndigenousName)
# admin.site.register(PlaceGISSelections)
admin.site.register(Places, PlacesAdmin)
admin.site.register(PlacesCitationEvents, PlacesCitationEventsAdmin)
admin.site.register(PlacesMediaEvents,PlacesMediaEventsAdmin)
admin.site.register(PlacesResourceCitationEvents, PlacesResourceCitationEventsAdmin)
admin.site.register(PlacesResourceEvents, PlacesResourceEventsAdmin)
admin.site.register(PlacesResourceMediaEvents, PlacesResourceMediaEventsAdmin)
admin.site.register(ResourceActivityCitationEvents, ResourceActivityCitationEventsAdmin)
admin.site.register(ResourceActivityMediaEvents, ResourceActivityMediaEventsAdmin)
admin.site.register(ResourceAltIndigenousName)
admin.site.register(ResourceResourceEvents, ResourceResourceEventsAdmin)
admin.site.register(Resources, ResourcesAdmin)
admin.site.register(ResourcesActivityEvents, ResourcesActivityEventsAdmin)
admin.site.register(ResourcesCitationEvents, ResourcesCitationEventsAdmin)
admin.site.register(ResourcesMediaEvents, ResourcesMediaEventsAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(UserAccess)

###Cruft
admin.site.register(LookupAuthorType)
admin.site.register(LookupUserInfo)
admin.site.register(CurrentVersion)
