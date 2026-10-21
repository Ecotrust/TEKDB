from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django_resumable_async_upload.fields import FormResumableMultipleFileField
from django_resumable_async_upload.widgets import ResumableAdminWidget
from .models import (
    MediaBulkUpload,
    Places,
    Resources,
    Citations,
    ResourcesActivityEvents,
    PlacesResourceEvents,
    Media,
)


class MediaBulkUploadForm(forms.ModelForm):
    files = FormResumableMultipleFileField(
        required=False,
        # not passing max_files here because FormResumableFileField defaults to undefined (unlimited),
        # which is what we want for bulk upload.
        widget=ResumableAdminWidget(attrs={"model": Media, "field_name": "mediafile"}),
    )
    places = forms.ModelMultipleChoiceField(
        queryset=Places.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("Places", is_stacked=False),
    )
    resources = forms.ModelMultipleChoiceField(
        queryset=Resources.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("Resources", is_stacked=False),
    )
    citations = forms.ModelMultipleChoiceField(
        queryset=Citations.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("Citations", is_stacked=False),
    )
    activities = forms.ModelMultipleChoiceField(
        queryset=ResourcesActivityEvents.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("Activities", is_stacked=False),
    )
    placesresources = forms.ModelMultipleChoiceField(
        queryset=PlacesResourceEvents.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("Places Resources", is_stacked=False),
    )

    class Meta:
        model = MediaBulkUpload
        fields = [
            "mediabulkname",
            "mediabulkdescription",
            "mediabulkdate",
            "files",
            "places",
            "resources",
            "citations",
            "activities",
            "placesresources",
        ]
