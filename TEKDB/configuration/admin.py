from django.contrib import admin
from django.forms import ModelForm
from TEKDB.widgets import OpenLayers6Widget

# Register your models here.
from configuration.models import Configuration


class ConfigurationForm(ModelForm):
    class Meta:
        model = Configuration
        widgets = {
            'geometry': OpenLayers6Widget(),
        }
        fields = '__all__'

class ConfigurationAdmin(admin.ModelAdmin):
    form = ConfigurationForm

admin.site.register(Configuration, ConfigurationAdmin)