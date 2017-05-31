from django import forms
from django.contrib import admin

from .models import Resources, Places, Locality, Citations, Media, Localityplaceresourceevent, Mediacitationevents, Placescitationevents, Placesmediaevents, Placesresourcecitationevents, Placesresourceevents, Placesresourcemediaevents, Resourceactivitycitationevents, Resourceactivitymediaevents, Resourceresourceevents, Resourcesactivityevents, Resourcescitationevents, Resourcesmediaevents, Users

# Citations referencetype select(Book, Edited Volume, Interview, Other)
# class CitationsForm(forms.ModelForm):
#     class Meta:
#         model = Citations

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


admin.site.register(Resources)
admin.site.register(Places)
admin.site.register(Locality)
admin.site.register(Citations, CitationsAdmin)
admin.site.register(Media)
admin.site.register(Localityplaceresourceevent)
admin.site.register(Mediacitationevents)
admin.site.register(Placescitationevents)
admin.site.register(Placesmediaevents)
admin.site.register(Placesresourcecitationevents)
admin.site.register(Placesresourceevents)
admin.site.register(Placesresourcemediaevents)
admin.site.register(Resourceactivitycitationevents)
admin.site.register(Resourceactivitymediaevents)
admin.site.register(Resourceresourceevents)
admin.site.register(Resourcesactivityevents)
admin.site.register(Resourcescitationevents)
admin.site.register(Resourcesmediaevents)
admin.site.register(Users)
