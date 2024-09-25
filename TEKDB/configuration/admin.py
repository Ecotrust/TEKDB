from django.contrib import admin
from django.forms import ModelForm
from TEKDB.widgets import OpenLayers6Widget, OpenLayers6PolygonWidget
from reversion.admin import VersionAdmin

from configuration.models import Configuration


class ConfigurationForm(ModelForm):
    class Meta:
        model = Configuration
        widgets = {
            # 'geometry': OpenLayers6Widget(),
            'geometry': OpenLayers6PolygonWidget(),
        }
        fields = '__all__'

class ConfigurationAdmin(VersionAdmin):
    list_display = ('preferred_initialism_or_pk','max_results_returned')
    fieldsets = (
        ('Site Header', {
            'fields':(
                'preferredInitialism',
                ('logo', 'logo_override'),
                'preferredInitialismPlacement',
            )
        }),
        ('Home Page', {
            'fields': (
                ('homepage_font_color','homepage_left_background','homepage_right_background'),
                ('homepage_image','homepage_image_attribution',)
            )
        }),
        ('Search Results', {
            'fields': (
                'max_results_returned',
            )
        }),
        ('Map Defaults', {
            'fields': (
                'geometry',
            )
        }),
    )

    form = ConfigurationForm
    
    # Limit to only ONE configuration record, as laid out here: https://stackoverflow.com/a/25088487/706797 by radtek
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)

    def preferred_initialism_or_pk(self, obj):
        return obj.pk if not obj.preferredInitialism else obj.preferredInitialism


admin.site.register(Configuration, ConfigurationAdmin)