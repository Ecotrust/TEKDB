from django.contrib import admin
from django.forms import ModelForm
from TEKDB.widgets import OpenLayers6Widget
from reversion.admin import VersionAdmin

from configuration.models import Configuration


class ConfigurationForm(ModelForm):
    class Meta:
        model = Configuration
        widgets = {
            'geometry': OpenLayers6Widget(),
        }
        fields = '__all__'

class ConfigurationAdmin(VersionAdmin):
    form = ConfigurationForm
    
    # Limit to only ONE configuration record, as laid out here: https://stackoverflow.com/a/25088487/706797 by radtek
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)

admin.site.register(Configuration, ConfigurationAdmin)