from django import forms
from django.contrib import admin

from .models import (
    Resources,
    Places,
    Locality,
    Citations,
    Media,
    LocalityPlaceResourceEvent,
    MediaCitationEvents,
    PlaceAltIndigenousName,
    PlacesCitationEvents,
    PlacesMediaEvents,
    PlacesResourceCitationEvents,
    PlacesResourceEvents,
    PlacesResourceMediaEvents,
    ResourceActivityCitationEvents,
    ResourceActivityMediaEvents,
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
    extra = 1
    classes = ['collapse']

class CitationresourceseventsInline(admin.TabularInline):
    model = ResourcesCitationEvents
    fields = ('resourceid', 'relationshipdescription', 'pages')
    extra = 1
    classes = ['collapse']

class CitationmediaeventsInline(admin.TabularInline):
    model = MediaCitationEvents
    fields = ('mediaid', 'relationshipdescription', 'pages')
    extra = 1
    classes = ['collapse']

#### MEDIA ####
class MediaplaceseventsInline(admin.TabularInline):
    model = PlacesMediaEvents
    fields = ('placeid','relationshipdescription','pages')
    extra = 1
    classes = ['collapse']

class MediacitationeventsInline(admin.TabularInline):
    model = MediaCitationEvents
    fields = ('citationid', 'relationshipdescription', 'pages')
    extra = 1
    classes = ['collapse']

class MediaresourceseventsInline(admin.TabularInline):
    model = ResourcesMediaEvents
    fields = ('resourceid', 'relationshipdescription', 'pages')
    extra = 1
    classes = ['collapse']

#### PLACES ####
class PlacesalternativenameInline(admin.TabularInline):
    model = PlaceAltIndigenousName
    fields = ('altindigenousnameid', 'altindigenousname')
    extra = 1
    classes = ['collapse']
    verbose_name_plural = 'alternate indigenous names'

class PlacesresourceeventsInline(admin.StackedInline):
    model = PlacesResourceEvents
    fieldsets = (
        ('', {
            'fields': ('resourceid', 'relationshipdescription', 'partused',
                'customaryuse', 'barterresource', 'season',
                # 'timing',
                ('january', 'february', 'march'), ('april', 'may', 'june'),
                ('july', 'august', 'september'), ('october', 'november',
                'december'), 'year', 'islocked'
            )
        }),
    )
    extra = 1
    classes = ['collapse']
    verbose_name_plural = 'related resources'

class PlaceslocalityInline(admin.TabularInline):
    model = Locality
    fields = ('indigenousname', 'englishname', 'localitytype')
    extra = 1
    classes = ['collapse']

class PlacesmediaeventsInline(admin.TabularInline):
    model = PlacesMediaEvents
    fields = ('mediaid', 'relationshipdescription', 'pages')
    extra = 1
    classes = ['collapse']
    verbose_name_plural = 'related media'

class PlacescitationeventsInline(admin.TabularInline):
    model = PlacesCitationEvents
    fields = ('citationid', 'relationshipdescription', 'pages')
    extra = 1
    classes = ['collapse']
    max_num = 9999
    verbose_name_plural = 'related citations'

### MODEL ADMINS ###
class CitationsAdmin(admin.ModelAdmin):
    list_display = ('referencetype','title','referencetext','modifiedbydate','enteredbydate')
    # form = CitationsForm
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

class MediaAdmin(admin.ModelAdmin):
    list_display = ('medianame','mediatype','modifiedbydate','enteredbydate')
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

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('indigenousplacename','englishplacename','modifiedbydate','enteredbydate')
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
    ]

admin.site.register(Resources)
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
admin.site.register(Users)
