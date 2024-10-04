from django import forms
from .models import MediaBulkUpload, Media
from .widgets import ThumbnailFileInput

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

# class MultipleFileField(forms.FileField):
#     widget = ThumbnailFileInput

class MediaBulkUploadForm(forms.ModelForm):
    files = MultipleFileField()
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = MediaBulkUpload
        fields = ['name', 'description', 'files', 'date']