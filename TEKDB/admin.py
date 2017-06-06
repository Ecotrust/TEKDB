from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    Resources,
    Places,
    Locality,
    Citations,
    Media,
    LocalityPlaceResourceEvent,
    MediaCitationEvents,
    PlaceAltIndigenousName,
    PlaceGISSelections,
    PlacesCitationEvents,
    PlacesMediaEvents,
    PlacesResourceCitationEvents,
    PlacesResourceEvents,
    PlacesResourceMediaEvents,
    ResourceActivityCitationEvents,
    ResourceActivityMediaEvents,
    ResourceAltIndigenousName,
    ResourceResourceEvents,
    ResourcesActivityEvents,
    ResourcesCitationEvents,
    ResourcesMediaEvents,
    Users,
    People
)

### INLINES ###
#### CITATIONS ####
class CitationplaceseventsInline(admin.TabularInline):
    model = PlacesCitationEvents
    fields = ('placeid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']

class CitationresourceseventsInline(admin.TabularInline):
    model = ResourcesCitationEvents
    fields = ('resourceid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']

class CitationmediaeventsInline(admin.TabularInline):
    model = MediaCitationEvents
    fields = ('mediaid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']

#### MEDIA ####
class MediaplaceseventsInline(admin.TabularInline):
    model = PlacesMediaEvents
    fields = ('placeid','relationshipdescription','pages')
    extra = 0
    classes = ['collapse', 'open']

class MediacitationeventsInline(admin.TabularInline):
    model = MediaCitationEvents
    fields = ('citationid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']

class MediaresourceseventsInline(admin.TabularInline):
    model = ResourcesMediaEvents
    fields = ('resourceid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']

#### PLACES ####
class PlacesalternativenameInline(admin.TabularInline):
    model = PlaceAltIndigenousName
    fields = ('altindigenousnameid', 'altindigenousname')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'alternate indigenous names'

class PlaceGISSelectionsInline(admin.TabularInline):
    model = PlaceGISSelections
    fields = ('placelabel', 'sourcefc')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'Place GIS Selections'

class PlacesresourceeventsInline(admin.StackedInline):
    model = PlacesResourceEvents
    fieldsets = (
        ('', {
            'fields': ('resourceid', 'relationshipdescription', 'partused',
                'customaryuse', 'barterresource', 'season', 'timing',
                ('january', 'february', 'march'), ('april', 'may', 'june'),
                ('july', 'august', 'september'), ('october', 'november',
                'december'), 'year', 'islocked'
            )
        }),
    )
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related resources'

class PlaceslocalityInline(admin.TabularInline):
    model = Locality
    fields = ('indigenousname', 'englishname', 'localitytype')
    extra = 0
    classes = ['collapse', 'open']

class PlacesmediaeventsInline(admin.TabularInline):
    model = PlacesMediaEvents
    fields = ('mediaid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related media'

class PlacescitationeventsInline(admin.TabularInline):
    model = PlacesCitationEvents
    fields = ('citationid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    max_num = 9999
    verbose_name_plural = 'related citations'

#### RESOURCES ####
class ResourcesMediaEventsInline(admin.TabularInline):
    model = ResourcesMediaEvents
    fields = ('mediaid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related media'

class ResourcesCitationEventsInline(admin.TabularInline):
    model = ResourcesCitationEvents
    fields = ('citationid', 'relationshipdescription', 'pages')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related citations'

class ResourcesPlaceEventsInline(admin.TabularInline):
    model = PlacesResourceEvents
    fieldsets = (
        ('', {
            'fields': ('placeid', 'relationshipdescription', 'partused',
                'customaryuse', 'barterresource', 'season', 'timing',
                ('january', 'february', 'march'), ('april', 'may', 'june'),
                ('july', 'august', 'september'), ('october', 'november',
                'december'), 'year', 'islocked'
            )
        }),
    )
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related places'

class ResourceResourceEventsInline(admin.TabularInline):
    model = ResourceResourceEvents
    fields = ('altresourceid', 'relationshipdescription')
    fk_name = 'resourceid'
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'related resources'

class ResourceAltIndigenousNameInline(admin.TabularInline):
    model = ResourceAltIndigenousName
    fields = ('resourceid', 'altindigenousname')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name_plural = 'Alternate Indigenous Name'

### MODEL ADMINS ###
class CitationsAdmin(admin.ModelAdmin):
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
                'preparedfor',
                'referencetext',
                'comments'
            )
        })
    )
    from TEKDB.settings import BASE_DIR
    add_form_template = '%s/TEKDB/templates/admin/CitationsForm.html' % BASE_DIR
    change_form_template = '%s/TEKDB/templates/admin/CitationsForm.html' % BASE_DIR
    inlines = [
        CitationplaceseventsInline,
        CitationresourceseventsInline,
        CitationmediaeventsInline,
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
        'enteredbyname', 'enteredbytribe', 'modifiedbyname',
        'modifiedbytribe'
    )

class MediaAdmin(admin.ModelAdmin):
    list_display = ('medianame','mediatype','modifiedbyname','modifiedbydate',
    'enteredbyname','enteredbydate')
    fieldsets = (
        (None, {
            'fields': (('medianame','mediatype'),'medialink','mediadescription')
        }),
    )
    inlines = [
        MediaplaceseventsInline,
        MediacitationeventsInline,
        MediaresourceseventsInline,
    ]
    search_fields = (
        'medianame', 'mediadescription', 'medialink',
        'mediatype__mediatype', 'mediatype__mediacategory',
        'enteredbyname', 'enteredbytribe', 'modifiedbyname',
        'modifiedbytribe'
    )

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('indigenousplacename','englishplacename','modifiedbyname',
    'modifiedbydate','enteredbyname','enteredbydate')
    fieldsets = (
        (None, {
            'fields':(
                ('indigenousplacename','indigenousplacenamemeaning'),
                'englishplacename',
                ('planningunitid','primaryhabitat'),
                'tribeid'
            )
        }),
    )
    inlines = [
        PlacesalternativenameInline,
        PlacesresourceeventsInline,
        PlacesmediaeventsInline,
        PlacescitationeventsInline,
        PlaceslocalityInline,
        # PlaceGISSelectionsInline,
    ]
    search_fields = (
        'englishplacename', 'indigenousplacename', 'indigenousplacenamemeaning',
        'planningunitid__planningunitname', 'primaryhabitat__habitat',
        'tribeid__tribeunit','tribeid__tribe','tribeid__federaltribe',
        'enteredbyname', 'enteredbytribe', 'modifiedbyname',
        'modifiedbytribe'
    )

class ResourcesAdmin(admin.ModelAdmin):
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
    )
    inlines = [
        # ResourcesActivityEventsInline,        #tied to place-resource
        ResourcesMediaEventsInline,
        ResourcesCitationEventsInline,
        ResourcesPlaceEventsInline,
        ResourceResourceEventsInline,
        ResourceAltIndigenousNameInline,
        # ResourceGISSelectionsInline,          #TODO: make this work
    ]
    search_fields = (
        'commonname', 'indigenousname', 'genus', 'species',
        'resourceclassificationgroup__resourceclassificationgroup',
        'enteredbyname', 'enteredbytribe', 'modifiedbyname',
        'modifiedbytribe'
    )

class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'firstname', 'lastname', 'affiliation',
        'accesslevel','title')
    fieldsets = (
        (None, {
            'fields':(
                'username', 'password', 'firstname', 'lastname',
                'affiliation', 'accesslevel', 'title'
            )
        }),
    )
    search_fields = (
        'username', 'firstname', 'lastname', 'affiliation',
        'title', 'accesslevel__accesslevel'
    )

admin.site.register(Resources, ResourcesAdmin)
admin.site.register(Places, PlacesAdmin)
# admin.site.register(Locality)
admin.site.register(Citations, CitationsAdmin)
admin.site.register(Media, MediaAdmin)
# admin.site.register(LocalityPlaceResourceEvent)
# admin.site.register(MediaCitationEvents)
# admin.site.register(PlacesCitationEvents)
# admin.site.register(PlacesMediaEvents)
# admin.site.register(PlacesResourceCitationEvents)
# admin.site.register(PlacesResourceEvents)
# admin.site.register(PlacesResourceMediaEvents)
# admin.site.register(ResourceActivityCitationEvents)
# admin.site.register(ResourceActivityMediaEvents)
# admin.site.register(ResourceResourceEvents)
# admin.site.register(ResourcesActivityEvents)
# admin.site.register(ResourcesCitationEvents)
# admin.site.register(ResourcesMediaEvents)
# admin.site.register(Users, UsersAdmin)
admin.site.register(Users, UserAdmin)
