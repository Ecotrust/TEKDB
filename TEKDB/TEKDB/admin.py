from django import forms
from django.contrib import admin

from .models import (
    Resources,
    Places,
    Locality,
    Citations,
    Media,
    Localityplaceresourceevent,
    Mediacitationevents,
    Placealtindigenousname,
    Placescitationevents,
    Placesmediaevents,
    Placesresourcecitationevents,
    Placesresourceevents,
    Placesresourcemediaevents,
    Resourceactivitycitationevents,
    Resourceactivitymediaevents,
    Resourceresourceevents,
    Resourcesactivityevents,
    Resourcescitationevents,
    Resourcesmediaevents,
    Users,
    People
)

### INLINES ###
#### CITATIONS ####
class CitationplaceseventsInline(admin.TabularInline):
    model = Placescitationevents
    fields = ('placeid', 'relationshipdescription', 'pages')
    extra = 1
    classes = ['collapse']

class CitationresourceseventsInline(admin.TabularInline):
    model = Resourcescitationevents
    fields = ('resourceid', 'relationshipdescription', 'pages')
    extra = 1
    classes = ['collapse']

class CitationmediaeventsInline(admin.TabularInline):
    model = Mediacitationevents
    fields = ('mediaid', 'relationshipdescription', 'pages')
    extra = 1
    classes = ['collapse']

#### MEDIA ####
class MediaplaceseventsInline(admin.TabularInline):
    model = Placesmediaevents
    fields = ('placeid','relationshipdescription','pages')
    extra = 1
    classes = ['collapse']

class MediacitationeventsInline(admin.TabularInline):
    model = Mediacitationevents
    fields = ('citationid', 'relationshipdescription', 'pages')
    extra = 1
    classes = ['collapse']

class MediaresourceseventsInline(admin.TabularInline):
    model = Resourcesmediaevents
    fields = ('resourceid', 'relationshipdescription', 'pages')
    extra = 1
    classes = ['collapse']

#### PLACES ####
class PlacesalternativenameInline(admin.TabularInline):
    model = Placealtindigenousname
    fields = ('altindigenousnameid', 'altindigenousname')
    extra = 1
    classes = ['collapse']
    verbose_name_plural = 'alternate indigenous names'

class PlacesresourceeventsInline(admin.StackedInline):
    model = Placesresourceevents
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
    model = Placesmediaevents
    fields = ('mediaid', 'relationshipdescription', 'pages')
    extra = 1
    classes = ['collapse']
    verbose_name_plural = 'related media'

class PlacescitationeventsInline(admin.TabularInline):
    model = Placescitationevents
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
# admin.site.register(Localityplaceresourceevent)
# admin.site.register(Mediacitationevents)
# admin.site.register(Placescitationevents)
# admin.site.register(Placesmediaevents)
# admin.site.register(Placesresourcecitationevents)
# admin.site.register(Placesresourceevents)
# admin.site.register(Placesresourcemediaevents)
# admin.site.register(Resourceactivitycitationevents)
# admin.site.register(Resourceactivitymediaevents)
# admin.site.register(Resourceresourceevents)
# admin.site.register(Resourcesactivityevents)
# admin.site.register(Resourcescitationevents)
# admin.site.register(Resourcesmediaevents)
admin.site.register(Users)
