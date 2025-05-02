from django.contrib import admin
from django import forms
from .models import MediaBulkUpload, Media, Places, Resources, Citations, ResourcesActivityEvents, PlacesResourceMediaEvents
from .widgets import ThumbnailFileInput


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", ThumbnailFileInput)
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

class MediaBulkUploadForm(forms.ModelForm):
    files = MultipleFileField()
    places = forms.ModelMultipleChoiceField(
        queryset=Places.objects.all(), 
        required=False,
        widget=admin.widgets.FilteredSelectMultiple("Places", is_stacked=False)
    )
    resources = forms.ModelMultipleChoiceField(
        queryset=Resources.objects.all(), 
        required=False,
        widget=admin.widgets.FilteredSelectMultiple("Resources", is_stacked=False)
    )
    citations = forms.ModelMultipleChoiceField(
        queryset=Citations.objects.all(), 
        required=False,
        widget=admin.widgets.FilteredSelectMultiple("Citations", is_stacked=False)
    )
    activities = forms.ModelMultipleChoiceField(
        queryset=ResourcesActivityEvents.objects.all(), 
        required=False,
        widget=admin.widgets.FilteredSelectMultiple("Activities", is_stacked=False)
    )
    placeresources = forms.ModelMultipleChoiceField(
        queryset=PlacesResourceMediaEvents.objects.all(), 
        required=False,
        widget=admin.widgets.FilteredSelectMultiple("Place Resources", is_stacked=False)
    )

    class Meta:
        model = MediaBulkUpload
        fields = ['mediabulkname', 'mediabulkdescription', 'mediabulkdate', 'files', 'mediabulkdate', 'places', 'resources', 'citations', 'activities', 'placeresources']