from django import forms
from django.db.models.functions import Lower
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.gis.admin import OSMGeoAdmin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from dal import autocomplete
from mimetypes import guess_type
from django.templatetags.static import static

# from moderation.admin import ModerationAdmin
import nested_admin
from tinymce.widgets import TinyMCE
from reversion.admin import VersionAdmin

from .forms import MediaBulkUploadForm
from .models import (
    ResourcesActivityEvents,
    Media,
    Citations,
    Places,
    LookupMediaType,
    LookupParticipants,
    LookupTechniques,
    People,
    LookupReferenceType,
    LookupPlanningUnit,
    LookupHabitat,
    LookupTribe,
    PlacesResourceEvents,
    MediaCitationEvents,
    PlacesCitationEvents,
    PlacesMediaEvents,
    PlacesResourceCitationEvents,
    PlacesResourceMediaEvents,
    ResourceActivityMediaEvents,
    ResourceActivityCitationEvents,
    ResourceResourceEvents,
    ResourcesCitationEvents,
    ResourcesMediaEvents,
    PlaceAltIndigenousName,
    ResourceAltIndigenousName,
    LocalityPlaceResourceEvent,
    LocalityGISSelections,
    MediaBulkUpload,
    LookupPartUsed,
    LookupSeason,
    LookupTiming,
    LookupActivity,
    LookupResourceGroup,
    Resources,
    LookupCustomaryUse,
    LookupAuthorType,
    UserAccess,
    LookupUserInfo,
    Users,
)

from TEKDB.settings import ADMIN_SITE_HEADER
from TEKDB.settings import BASE_DIR
from TEKDB.widgets import OpenLayers6Widget

admin.site.site_header = ADMIN_SITE_HEADER


#############
### FORMS ###
#############
class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        # widgets = {
        #     'medialink':forms.FileInput
        # }
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(MediaForm, self).__init__(*args, **kwargs)
        self.fields["mediatype"].queryset = LookupMediaType.objects.order_by(
            Lower("mediatype")
        )


class ResourcesActivityEventsForm(forms.ModelForm):
    class Meta:
        model = ResourcesActivityEvents
        widgets = {
            "placeresourceid": autocomplete.ModelSelect2(url="select2_fk_placeresource")
        }
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ResourcesActivityEventsForm, self).__init__(*args, **kwargs)
        self.fields["participants"].queryset = LookupParticipants.objects.order_by(
            Lower("participants")
        )
        self.fields["technique"].queryset = LookupTechniques.objects.order_by(
            Lower("techniques")
        )
        self.fields[
            "activityshortdescription"
        ].queryset = LookupActivity.objects.order_by(Lower("activity"))


class CitationsForm(forms.ModelForm):
    class Meta:
        model = Citations
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CitationsForm, self).__init__(*args, **kwargs)
        self.fields["referencetype"].queryset = LookupReferenceType.objects.order_by(
            Lower("documenttype")
        )
        # self.fields['authortype'].queryset = LookupAuthorType.objects.order_by(Lower('authortype'))
        self.fields["intervieweeid"].queryset = People.objects.order_by(
            Lower("firstname"), Lower("lastname")
        )
        self.fields["interviewerid"].queryset = People.objects.order_by(
            Lower("firstname"), Lower("lastname")
        )


class PlacesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlacesForm, self).__init__(*args, **kwargs)
        self.fields["planningunitid"].queryset = LookupPlanningUnit.objects.order_by(
            Lower("planningunitname")
        )
        self.fields["primaryhabitat"].queryset = LookupHabitat.objects.order_by(
            Lower("habitat")
        )
        self.fields["tribeid"].queryset = LookupTribe.objects.order_by(Lower("tribe"))

    class Meta:
        model = Places
        widgets = {
            "geometry": OpenLayers6Widget(),
        }
        fields = "__all__"


class ResourcesForm(forms.ModelForm):
    class Meta:
        model = Resources
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ResourcesForm, self).__init__(*args, **kwargs)
        self.fields[
            "resourceclassificationgroup"
        ].queryset = LookupResourceGroup.objects.order_by(
            Lower("resourceclassificationgroup")
        )


class PlacesResourceEventForm(forms.ModelForm):
    class Meta:
        model = PlacesResourceEvents
        widgets = {
            "placeid": autocomplete.ModelSelect2(url="select2_fk_place"),
            "resourceid": autocomplete.ModelSelect2(url="select2_fk_resource"),
            "relationshipdescription": TinyMCE,
        }
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PlacesResourceEventForm, self).__init__(*args, **kwargs)
        self.fields["partused"].queryset = LookupPartUsed.objects.order_by(
            Lower("partused")
        )
        self.fields["season"].queryset = LookupSeason.objects.order_by(Lower("season"))
        self.fields["timing"].queryset = LookupTiming.objects.order_by(Lower("timing"))


class MediaCitationEventsForm(forms.ModelForm):
    class Meta:
        model = MediaCitationEvents
        widgets = {
            "mediaid": autocomplete.ModelSelect2(url="select2_fk_media"),
            "citationid": autocomplete.ModelSelect2(url="select2_fk_citation"),
            "relationshipdescription": TinyMCE,
        }
        fields = "__all__"


class PlacesCitationEventsForm(forms.ModelForm):
    class Meta:
        model = PlacesCitationEvents
        widgets = {
            "placeid": autocomplete.ModelSelect2(url="select2_fk_place"),
            "citationid": autocomplete.ModelSelect2(url="select2_fk_citation"),
            "relationshipdescription": TinyMCE,
        }
        fields = "__all__"


class PlacesMediaEventsForm(forms.ModelForm):
    class Meta:
        model = PlacesMediaEvents
        widgets = {
            "placeid": autocomplete.ModelSelect2(url="select2_fk_place"),
            "mediaid": autocomplete.ModelSelect2(url="select2_fk_media"),
            "relationshipdescription": TinyMCE,
        }
        fields = "__all__"


class PlacesResourceCitationEventsForm(forms.ModelForm):
    class Meta:
        model = PlacesResourceCitationEvents
        widgets = {
            "placeresourceid": autocomplete.ModelSelect2(
                url="select2_fk_placeresource"
            ),
            "citationid": autocomplete.ModelSelect2(url="select2_fk_citation"),
            "relationshipdescription": TinyMCE(),
        }
        fields = "__all__"


class PlacesResourceMediaEventsForm(forms.ModelForm):
    class Meta:
        model = PlacesResourceMediaEvents
        widgets = {
            "placeresourceid": autocomplete.ModelSelect2(
                url="select2_fk_placeresource"
            ),
            "mediaid": autocomplete.ModelSelect2(url="select2_fk_media"),
            "relationshipdescription": TinyMCE,
        }
        fields = "__all__"


class ResourceActivityMediaEventsForm(forms.ModelForm):
    class Meta:
        model = ResourceActivityMediaEvents
        widgets = {
            "resourceactivityid": autocomplete.ModelSelect2(
                url="select2_fk_resourceactivity"
            ),
            "mediaid": autocomplete.ModelSelect2(url="select2_fk_media"),
            "relationshipdescription": TinyMCE,
        }
        fields = "__all__"


class ResourceActivityCitationEventsForm(forms.ModelForm):
    class Meta:
        model = ResourceActivityCitationEvents
        widgets = {
            "resourceactivityid": autocomplete.ModelSelect2(
                url="select2_fk_resourceactivity"
            ),
            "citationid": autocomplete.ModelSelect2(url="select2_fk_citation"),
            "relationshipdescription": TinyMCE,
        }
        fields = "__all__"


class ResourceResourceEventsForm(forms.ModelForm):
    class Meta:
        model = ResourceResourceEvents
        widgets = {
            "resourceid": autocomplete.ModelSelect2(url="select2_fk_resource"),
            "altresourceid": autocomplete.ModelSelect2(url="select2_fk_resource"),
            "relationshipdescription": TinyMCE,
        }
        fields = "__all__"


class ResourcesCitationEventsForm(forms.ModelForm):
    class Meta:
        model = ResourcesCitationEvents
        widgets = {
            "resourceid": autocomplete.ModelSelect2(url="select2_fk_resource"),
            "citationid": autocomplete.ModelSelect2(url="select2_fk_citation"),
            "relationshipdescription": TinyMCE,
        }
        fields = "__all__"


class ResourcesMediaEventsForm(forms.ModelForm):
    class Meta:
        model = ResourcesMediaEvents
        widgets = {
            "resourceid": autocomplete.ModelSelect2(url="select2_fk_resource"),
            "mediaid": autocomplete.ModelSelect2(url="select2_fk_media"),
            "relationshipdescription": TinyMCE,
        }
        fields = "__all__"


class PlaceAltIndigenousNameForm(forms.ModelForm):
    class Meta:
        model = PlaceAltIndigenousName
        widgets = {"placeid": autocomplete.ModelSelect2(url="select2_fk_place")}
        fields = "__all__"


class ResourceAltIndigenousNameForm(forms.ModelForm):
    class Meta:
        model = ResourceAltIndigenousName
        widgets = {
            "resourceid": autocomplete.ModelSelect2(url="select2_fk_resource"),
        }
        fields = "__all__"


###############
### INLINES ###
###############


#### ACTIVITIES ####
class NestedResourcesactivitymediaeventsInline(nested_admin.NestedTabularInline):
    model = ResourceActivityMediaEvents
    fields = ("mediaid", "relationshipdescription", "pages")
    extra = 0
    classes = ["collapse", "open"]
    verbose_name_plural = "Related Media"


class NestedResourcesactivitycitationeventsInline(nested_admin.NestedTabularInline):
    model = ResourceActivityCitationEvents
    fields = ("citationid", "relationshipdescription", "pages")
    extra = 0
    classes = ["collapse", "open"]
    verbose_name_plural = "Related Bibliographic Sources"


#### PLACESRESOURCES ####
class NestedPlacesresourcecitationeventsInline(nested_admin.NestedTabularInline):
    model = PlacesResourceCitationEvents
    fields = ("citationid", "relationshipdescription", "pages")
    extra = 0
    classes = ["collapse", "open"]
    verbose_name_plural = "related Bibliographic Sources"
    form = PlacesResourceCitationEventsForm


class NestedPlacesresourcemediaeventsInline(nested_admin.NestedTabularInline):
    model = PlacesResourceMediaEvents
    fields = ("mediaid", "relationshipdescription", "pages")
    extra = 0
    classes = ["collapse", "open"]
    verbose_name_plural = "related media"
    form = PlacesResourceMediaEventsForm


class NestedPlaceresourcelocalityeventInline(nested_admin.NestedTabularInline):
    model = LocalityPlaceResourceEvent
    fields = ("localityid",)
    extra = 0
    classes = ["collapse", "open"]
    verbose_name_plural = "related localities"


class NestedPlacesresourceactivityeventInline(nested_admin.NestedStackedInline):
    model = ResourcesActivityEvents
    fieldsets = (
        (
            "",
            {
                "fields": (
                    ("participants", "technique", "relationshipdescription"),
                    (
                        "activityshortdescription",
                        "activitylongdescription",
                    ),
                )
            },
        ),
    )
    extra = 0
    classes = ["collapse", "open"]
    verbose_name_plural = "related Activities"
    inlines = [
        NestedResourcesactivitycitationeventsInline,
        NestedResourcesactivitymediaeventsInline,
    ]


#### LOCALITIES ####
class LocalityplaceresourceeventInline(admin.TabularInline):
    model = LocalityPlaceResourceEvent
    fields = ("placeresourceid",)
    extra = 0
    classes = ["collapse", "open"]
    verbose_name_plural = "related place-resources"


class LocalityGISSelectionsInline(admin.TabularInline):
    model = LocalityGISSelections
    fields = ("localitylabel", "sourcefc")
    extra = 0
    classes = ["collapse", "open"]
    verbose_name_plural = "Locality GIS Selections"


####################
### MODEL ADMINS ###
####################
#### PROXY MODELS ####
# class RecordAdminProxy(VersionAdmin, ModerationAdmin):
class RecordAdminProxy(VersionAdmin):
    readonly_fields = (
        "enteredbyname",
        "enteredbytribe",
        "enteredbytitle",
        "enteredbydate",
        "modifiedbyname",
        "modifiedbytribe",
        "modifiedbytitle",
        "modifiedbydate",
    )

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if hasattr(instance, "enteredbyname"):
            if instance.enteredbyname is None:
                instance.enteredbyname = request.user.username
                instance.enteredbytribe = request.user.affiliation
                instance.enteredbytitle = request.user.title
            instance.modifiedbyname = request.user.username
            instance.modifiedbytribe = request.user.affiliation
            instance.modifiedbytitle = request.user.title
        instance.save()
        return instance

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if hasattr(instance, "enteredbyname"):
                if instance.enteredbyname is None:
                    instance.enteredbyname = request.user.username
                    instance.enteredbytribe = request.user.affiliation
                    instance.enteredbytitle = request.user.title
                instance.modifiedbyname = request.user.username
                instance.modifiedbytribe = request.user.affiliation
                instance.modifiedbytitle = request.user.title
            instance.save()


class NestedRecordAdminProxy(nested_admin.NestedModelAdmin):
    readonly_fields = (
        "enteredbyname",
        "enteredbytribe",
        "enteredbytitle",
        "enteredbydate",
        "modifiedbyname",
        "modifiedbytribe",
        "modifiedbytitle",
        "modifiedbydate",
    )

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if hasattr(instance, "enteredbyname"):
            if instance.enteredbyname is None:
                instance.enteredbyname = request.user.username
                instance.enteredbytribe = request.user.affiliation
                instance.enteredbytitle = request.user.title
            instance.modifiedbyname = request.user.username
            instance.modifiedbytribe = request.user.affiliation
            instance.modifiedbytitle = request.user.title
        instance.save()
        return instance

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if hasattr(instance, "enteredbyname"):
                if instance.enteredbyname is None:
                    instance.enteredbyname = request.user.username
                    instance.enteredbytribe = request.user.affiliation
                    instance.enteredbytitle = request.user.title
                instance.modifiedbyname = request.user.username
                instance.modifiedbytribe = request.user.affiliation
                instance.modifiedbytitle = request.user.title
            instance.save()

    @admin.display()
    def needs_Review(self, obj):
        if obj.needsReview:
            return format_html(
                '<img src="/static/admin/img/icon-alert.svg" />', obj.needsReview
            )
        else:
            return format_html("<span></span>", obj.needsReview)


#### RECORD MODELS ####
# class RecordModelAdmin(VersionAdmin, ModerationAdmin):
class RecordModelAdmin(VersionAdmin):
    record_form = "%s/TEKDB/templates/admin/RecordForm.html" % BASE_DIR
    add_form_template = record_form
    change_form_template = record_form

    @admin.display()
    def needs_Review(self, obj):
        if obj.needsReview:
            return format_html(
                '<img src="/static/admin/img/icon-alert.svg" />', obj.needsReview
            )
        else:
            return format_html("<span></span>", obj.needsReview)

    def change_view(self, request, object_id, form_url="", extra_context={}):
        object_instance = self.model.objects.get(pk=object_id)

        extra_context["related_objects"] = object_instance.get_related_objects(
            object_id
        )
        return super(RecordModelAdmin, self).change_view(
            request, object_id, form_url, extra_context=extra_context
        )


@admin.register(Citations)
class CitationsAdmin(RecordAdminProxy, RecordModelAdmin):
    list_display = (
        "referencetype",
        "title_text",
        "description_text",
        "needs_Review",
        "modifiedbyname",
        "modifiedbydate",
        "enteredbyname",
        "enteredbydate",
    )
    fieldsets = (
        (None, {"classes": ("citation-ref-type",), "fields": ("referencetype",)}),
        (
            "Bibliographic Source",
            {
                "classes": ("citation-form-fieldset",),
                "fields": (
                    "title",
                    "referencetext",
                    ("authorprimary", "authorsecondary"),
                    ("intervieweeid", "interviewerid"),
                    "date",
                    "year",
                    ("publisher", "publishercity"),
                    "seriestitle",
                    ("seriesvolume", "serieseditor"),
                    "placeofinterview",
                    ("journal", "journalpages"),
                    "preparedfor",
                    # 'rawcitation',
                    "comments",
                ),
            },
        ),
        ("Review", {"fields": ("needsReview", "researchComments")}),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )

    add_form_template = "%s/TEKDB/templates/admin/CitationsForm.html" % BASE_DIR
    change_form_template = "%s/TEKDB/templates/admin/CitationsForm.html" % BASE_DIR
    search_fields = (
        "referencetype__documenttype",
        "intervieweeid__firstname",
        "intervieweeid__lastname",
        "interviewerid__lastname",
        "interviewerid__firstname",
        "authortype__authortype",
        "interviewerid__village",
        "intervieweeid__village",
        "interviewerid__relationshiptootherpeople",
        "intervieweeid__relationshiptootherpeople",
        "referencetext",
        "authorprimary",
        "authorsecondary",
        "placeofinterview",
        "title",
        "seriestitle",
        "seriesvolume",
        "serieseditor",
        "publisher",
        "publishercity",
        "preparedfor",
        "rawcitation",
        "comments",
        "journal",
        "enteredbyname",
        "enteredbytribe",
        "modifiedbyname",
        "modifiedbytribe",
    )
    form = CitationsForm


#   * Bulk Media Upload Admin
@admin.register(MediaBulkUpload)
class MediaBulkUploadAdmin(admin.ModelAdmin):
    form = MediaBulkUploadForm

    list_display = ("mediabulkname", "mediabulkdate", "enteredbyname", "enteredbydate")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        places = form.cleaned_data.get("places")
        resources = form.cleaned_data.get("resources")
        citations = form.cleaned_data.get("citations")
        activities = form.cleaned_data.get("activities")
        placesresources = form.cleaned_data.get("placesresources")

        for file in request.FILES.getlist("files"):
            mime_type, _ = guess_type(file.name)
            # if mime_type:
            file_mime_type = mime_type.split("/")[0]
            media_type_instance = LookupMediaType.objects.filter(
                mediatype__startswith=file_mime_type
            ).first()
            if media_type_instance:
                mediatype = media_type_instance
            else:
                media_type_instance = LookupMediaType.objects.filter(
                    mediatype__startswith="other"
                ).first()
                mediatype = media_type_instance
            filename = file.name.split(".")[0]

            media_instance = Media(
                medianame=filename,
                mediadescription=f'Part of the "{obj.mediabulkname}" Media Bulk Upload that was uploaded on {obj.mediabulkdate}',
                mediafile=file,
                mediatype=mediatype,
            )
            media_instance.save()
            obj.mediabulkupload.add(media_instance)

            # Add relationships
            if places:
                for place in places:
                    PlacesMediaEvents.objects.create(
                        placeid=place, mediaid=media_instance
                    )
            if resources:
                for resource in resources:
                    ResourcesMediaEvents.objects.create(
                        resourceid=resource, mediaid=media_instance
                    )
            if citations:
                for citation in citations:
                    MediaCitationEvents.objects.create(
                        citationid=citation, mediaid=media_instance
                    )
            if activities:
                for activity in activities:
                    ResourceActivityMediaEvents.objects.create(
                        resourceactivityid=activity, mediaid=media_instance
                    )
            if placesresources:
                for placeresource in placesresources:
                    PlacesResourceMediaEvents.objects.create(
                        placeresourceid=placeresource, mediaid=media_instance
                    )

    @admin.display(description="Thumbnails")
    def thumbnail_gallery(self, obj):
        thumbnails = []
        for media in obj.mediabulkupload.all():
            # Guess the MIME type of the file
            mime_type, _ = guess_type(media.mediafile.url)

            file_name = media.mediafile.name

            if mime_type:
                if mime_type.startswith("image"):
                    thumbnails.append(
                        format_html(
                            '<div style="display:inline-block; text-align:center; margin: 10px;">'
                            '<img src="{}" width="100" height="100" />'
                            '<br /><span style="display:block; width: 100px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">{}</span>'
                            "</div>",
                            media.mediafile.url,
                            file_name,
                        )
                    )
                elif mime_type.startswith("video"):
                    thumbnails.append(
                        format_html(
                            '<div style="display:inline-block; text-align:center; margin: 10px;">'
                            '<video width="100" height="100" controls>'
                            '<source src="{}" type="{}">'
                            "Your browser does not support the video tag."
                            "</video>"
                            '<br /><span style="display:block; width: 100px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">{}</span>'
                            "</div>",
                            media.mediafile.url,
                            mime_type,
                            file_name,
                        )
                    )
                elif mime_type.startswith("audio"):
                    generic_audio_icon = static("assets/audio-x-generic.svg")
                    thumbnails.append(
                        format_html(
                            '<div style="display:inline-block; text-align:center; margin: 10px;">'
                            '<img src="{}" width="100" height="100" alt="Audio File" />'
                            '<br /><span style="display:block; width: 100px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">{}</span>'
                            "</div>",
                            generic_audio_icon,
                            file_name,
                        )
                    )
                elif (
                    mime_type.startswith("text")
                    or "application/msword" in mime_type
                    or "application/vnd" in mime_type
                ):
                    generic_doc_icon = static("assets/doc-text.svg")
                    thumbnails.append(
                        format_html(
                            '<div style="display:inline-block; text-align:center; margin: 10px;">'
                            '<img src="{}" width="100" height="100" alt="Document File" />'
                            '<br /><span style="display:block; width: 100px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">{}</span>'
                            "</div>",
                            generic_doc_icon,
                            file_name,
                        )
                    )
                else:
                    # For unknown or other file types, show a generic file image
                    generic_file_icon = static("assets/unknown-mail.png")
                    thumbnails.append(
                        format_html(
                            '<div style="display:inline-block; text-align:center; margin: 10px;">'
                            '<img src="{}" width="100" height="100" alt="File" />'
                            '<br /><span style="display:block; width: 100px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">{}</span>'
                            "</div>",
                            generic_file_icon,
                            file_name,
                        )
                    )
            else:
                # In case the MIME type could not be determined, use a generic file icon
                generic_file_icon = static("assets/unknown-mail.png")
                thumbnails.append(
                    format_html(
                        '<div style="display:inline-block; text-align:center; margin: 10px;">'
                        '<img src="{}" width="100" height="100" alt="File" />'
                        '<br /><span style="display:block; width: 100px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">{}</span>'
                        "</div>",
                        generic_file_icon,
                        file_name,
                    )
                )

        return format_html("".join(thumbnails))

    def get_readonly_fields(self, request, obj=None):
        if obj:  # If the object already exists
            return [field.name for field in self.model._meta.fields]
        else:
            return self.readonly_fields

    def has_change_permission(self, request, obj=None):
        if obj:  # If the object already exists
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True

    readonly_fields = (
        "thumbnail_gallery",
        "enteredbyname",
        "enteredbytribe",
        "enteredbytitle",
        "enteredbydate",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "mediabulkname",
                    "mediabulkdescription",
                    "files",
                    "mediabulkdate",
                    "places",
                    "resources",
                    "citations",
                    "activities",
                    "placesresources",
                    "thumbnail_gallery",
                )
            },
        ),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    )
                )
            },
        ),
    )


@admin.register(Media)
class MediaAdmin(RecordAdminProxy, RecordModelAdmin):
    readonly_fields = (
        "medialink",
        "enteredbyname",
        "enteredbytribe",
        "enteredbytitle",
        "enteredbydate",
        "modifiedbyname",
        "modifiedbytribe",
        "modifiedbytitle",
        "modifiedbydate",
        "mediabulkupload",
    )
    list_display = (
        "medianame",
        "mediatype",
        "needs_Review",
        "modifiedbyname",
        "modifiedbydate",
        "enteredbyname",
        "enteredbydate",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("medianame", "mediatype", "limitedaccess"),
                    "mediafile",
                    "medialink",
                    "mediadescription",
                    "mediabulkupload",
                )
            },
        ),
        ("Review", {"fields": ("needsReview", "researchComments")}),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )
    from TEKDB.settings import BASE_DIR

    add_form_template = "%s/TEKDB/templates/admin/MediaForm.html" % BASE_DIR
    change_form_template = "%s/TEKDB/templates/admin/MediaForm.html" % BASE_DIR
    search_fields = (
        "medianame",
        "mediadescription",
        "medialink",
        "mediatype__mediatype",
        "mediatype__mediacategory",
        "enteredbyname",
        "enteredbytribe",
        "modifiedbyname",
        "modifiedbytribe",
    )
    form = MediaForm


# class PlacesAdmin(NestedRecordAdminProxy, OSMGeoAdmin, RecordModelAdmin):
@admin.register(Places)
class PlacesAdmin(NestedRecordAdminProxy, RecordModelAdmin):
    list_display = (
        "indigenousplacename",
        "englishplacename",
        "needs_Review",
        "modifiedbyname",
        "modifiedbydate",
        "enteredbyname",
        "enteredbydate",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("indigenousplacename", "indigenousplacenamemeaning"),
                    "englishplacename",
                    ("planningunitid", "primaryhabitat"),
                    "tribeid",
                    "geometry",
                )
            },
        ),
        ("Review", {"fields": ("needsReview", "researchComments")}),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                    ("Source", "DigitizedBy", "DigitizedDate"),
                )
            },
        ),
    )

    search_fields = (
        "englishplacename",
        "indigenousplacename",
        "indigenousplacenamemeaning",
        "planningunitid__planningunitname",
        "primaryhabitat__habitat",
        "tribeid__tribeunit",
        "tribeid__tribe",
        "tribeid__federaltribe",
        "enteredbyname",
        "enteredbytribe",
        "modifiedbyname",
        "modifiedbytribe",
    )

    form = PlacesForm

    change_list_template = "admin/TEKDB/places/change_list.html"

    def changelist_view(self, request, extra_context=None):
        from .views import getPlacesGeoJSON

        extra_context = extra_context or {}
        extra_context["results_geojson"] = getPlacesGeoJSON(request)
        return super(PlacesAdmin, self).changelist_view(
            request, extra_context=extra_context
        )


@admin.register(Resources)
class ResourcesAdmin(NestedRecordAdminProxy, RecordModelAdmin):
    list_display = (
        "commonname",
        "indigenousname",
        "needs_Review",
        "modifiedbyname",
        "modifiedbydate",
        "enteredbyname",
        "enteredbydate",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("commonname", "indigenousname"),
                    ("genus", "species"),
                    "resourceclassificationgroup",
                )
            },
        ),
        ("Review", {"fields": ("needsReview", "researchComments")}),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )
    search_fields = (
        "commonname",
        "indigenousname",
        "genus",
        "species",
        "resourceclassificationgroup__resourceclassificationgroup",
        "enteredbyname",
        "enteredbytribe",
        "modifiedbyname",
        "modifiedbytribe",
    )
    ordering = ("commonname",)
    form = ResourcesForm


@admin.register(ResourcesActivityEvents)
class ResourcesActivityEventsAdmin(RecordAdminProxy, RecordModelAdmin):
    list_display = (
        "placeresourceid",
        "excerpt_text",
        "needs_Review",
        "modifiedbyname",
        "modifiedbydate",
        "enteredbyname",
        "enteredbydate",
    )
    fieldsets = (
        (None, {"fields": ("placeresourceid",)}),
        (
            "Activity",
            {
                "fields": (
                    ("participants", "technique"),
                    "relationshipdescription",
                    ("partused", "activityshortdescription"),
                    "activitylongdescription",
                    "gear",
                    "customaryuse",
                    "timing",
                    "timingdescription",
                )
            },
        ),
        ("Review", {"fields": ("needsReview", "researchComments")}),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )
    search_fields = (
        "placeresourceid__resourceid__commonname",
        "placeresourceid__placeid__englishplacename",
        "placeresourceid__placeid__indigenousplacename",
        "relationshipdescription",
        "activityshortdescription__activity",
        "activitylongdescription",
        "participants__participants",
        "technique__techniques",
        # 'customaryuse__usedfor', 'gear', 'timing__timing', 'timingdescription',
        #'partused__partused',
        "enteredbyname",
        "enteredbytribe",
        "enteredbytitle",
        "modifiedbyname",
        "modifiedbytribe",
        "modifiedbytitle",
    )
    form = ResourcesActivityEventsForm


class LocalityAdmin(RecordAdminProxy, OSMGeoAdmin):
    list_display = (
        "placeid",
        "englishname",
        "indigenousname",
        "modifiedbyname",
        "modifiedbydate",
        "enteredbyname",
        "enteredbydate",
    )
    fieldsets = (
        (None, {"fields": ("placeid", "englishname", "indigenousname", "geometry")}),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                    ("Source", "DigitizedBy", "DigitizedDate"),
                )
            },
        ),
    )
    search_fields = (
        "placeid__indigenousplacename",
        "placeid__englishplacename",
        "englishname",
        "indigenousname",
        "enteredbyname",
        "enteredbytribe",
        "enteredbytitle",
        "modifiedbyname",
        "modifiedbytribe",
        "modifiedbytitle",
    )
    inlines = [
        LocalityplaceresourceeventInline,
        LocalityGISSelectionsInline,
    ]


#### RELATIONSHIP MODELS ####
@admin.register(PlacesResourceEvents)
class PlacesResourceEventsAdmin(NestedRecordAdminProxy):
    list_display = (
        "placeid",
        "resourceid",
        "needs_Review",
        "partused",
        "season",
        "enteredbyname",
        "enteredbydate",
        "modifiedbyname",
        "modifiedbydate",
    )
    fieldsets = (
        (
            "",
            {
                "fields": (
                    ("placeid", "resourceid"),
                    "relationshipdescription",
                    ("partused", "barterresource"),
                    ("season", "timing"),
                    ("january", "february", "march", "april", "may", "june"),
                    ("july", "august", "september", "october", "november", "december"),
                    "year",
                )
            },
        ),
        ("Review", {"fields": ("needsReview", "researchComments")}),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )
    form = PlacesResourceEventForm
    inlines = [
        NestedPlacesresourcecitationeventsInline,
        NestedPlacesresourcemediaeventsInline,
        # NestedPlaceresourcelocalityeventInline,
        NestedPlacesresourceactivityeventInline,
    ]


@admin.register(MediaCitationEvents)
class MediaCitationEventsAdmin(RecordAdminProxy):
    list_display = (
        "mediaid",
        "citationid",
        "enteredbyname",
        "enteredbydate",
        "modifiedbyname",
        "modifiedbydate",
    )
    fieldsets = (
        (
            "",
            {"fields": (("mediaid", "citationid"), "relationshipdescription", "pages")},
        ),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )
    form = MediaCitationEventsForm


@admin.register(PlacesCitationEvents)
class PlacesCitationEventsAdmin(RecordAdminProxy):
    list_display = (
        "placeid",
        "citationid",
        "enteredbyname",
        "enteredbydate",
        "modifiedbyname",
        "modifiedbydate",
    )
    fieldsets = (
        (
            "",
            {"fields": (("placeid", "citationid"), "relationshipdescription", "pages")},
        ),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )
    form = PlacesCitationEventsForm


@admin.register(PlacesMediaEvents)
class PlacesMediaEventsAdmin(RecordAdminProxy):
    list_display = (
        "placeid",
        "mediaid",
        "enteredbyname",
        "enteredbydate",
        "modifiedbyname",
        "modifiedbydate",
    )
    fieldsets = (
        ("", {"fields": (("placeid", "mediaid"), "relationshipdescription", "pages")}),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )
    form = PlacesMediaEventsForm


@admin.register(PlaceAltIndigenousName)
class PlaceAltIndigenousNameAdmin(VersionAdmin):
    fieldsets = (
        (
            "",
            {
                "fields": (("placeid", "altindigenousname"),),
            },
        ),
    )
    form = PlaceAltIndigenousNameForm


@admin.register(PlacesResourceCitationEvents)
class PlacesResourceCitationEventsAdmin(RecordAdminProxy):
    list_display = (
        "placeresourceid",
        "citationid",
        "enteredbyname",
        "enteredbydate",
        "modifiedbyname",
        "modifiedbydate",
    )
    fieldsets = (
        (
            "",
            {
                "fields": (
                    ("placeresourceid", "citationid"),
                    "relationshipdescription",
                    "pages",
                )
            },
        ),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )
    form = PlacesResourceCitationEventsForm


@admin.register(PlacesResourceMediaEvents)
class PlacesResourceMediaEventsAdmin(RecordAdminProxy):
    list_display = (
        "placeresourceid",
        "mediaid",
        "enteredbyname",
        "enteredbydate",
        "modifiedbyname",
        "modifiedbydate",
    )
    fieldsets = (
        (
            "",
            {
                "fields": (
                    ("placeresourceid", "mediaid"),
                    "relationshipdescription",
                    "pages",
                )
            },
        ),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )
    form = PlacesResourceMediaEventsForm


@admin.register(ResourceActivityCitationEvents)
class ResourceActivityCitationEventsAdmin(RecordAdminProxy):
    list_display = (
        "resourceactivityid",
        "citationid",
        "enteredbyname",
        "enteredbydate",
        "modifiedbyname",
        "modifiedbydate",
    )
    fieldsets = (
        (
            "",
            {
                "fields": (
                    ("resourceactivityid", "citationid"),
                    "relationshipdescription",
                    "pages",
                )
            },
        ),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )
    form = ResourceActivityCitationEventsForm


@admin.register(ResourceActivityMediaEvents)
class ResourceActivityMediaEventsAdmin(RecordAdminProxy):
    list_display = (
        "resourceactivityid",
        "mediaid",
        "enteredbyname",
        "enteredbydate",
        "modifiedbyname",
        "modifiedbydate",
    )
    fieldsets = (
        (
            "",
            {
                "fields": (
                    ("resourceactivityid", "mediaid"),
                    "relationshipdescription",
                    "pages",
                )
            },
        ),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )
    form = ResourceActivityMediaEventsForm


@admin.register(ResourceResourceEvents)
class ResourceResourceEventsAdmin(RecordAdminProxy):
    list_display = (
        "resourceid",
        "altresourceid",
        "enteredbyname",
        "enteredbydate",
        "modifiedbyname",
        "modifiedbydate",
    )
    fieldsets = (
        ("", {"fields": (("resourceid", "altresourceid"), "relationshipdescription")}),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )
    form = ResourceResourceEventsForm


@admin.register(ResourcesCitationEvents)
class ResourcesCitationEventsAdmin(RecordAdminProxy):
    list_display = (
        "resourceid",
        "citationid",
        "enteredbyname",
        "enteredbydate",
        "modifiedbyname",
        "modifiedbydate",
    )
    fieldsets = (
        (
            "",
            {
                "fields": (
                    ("resourceid", "citationid"),
                    "relationshipdescription",
                    "pages",
                )
            },
        ),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )
    form = ResourcesCitationEventsForm


@admin.register(ResourcesMediaEvents)
class ResourcesMediaEventsAdmin(RecordAdminProxy):
    list_display = (
        "resourceid",
        "mediaid",
        "enteredbyname",
        "enteredbydate",
        "modifiedbyname",
        "modifiedbydate",
    )
    fieldsets = (
        (
            "",
            {"fields": (("resourceid", "mediaid"), "relationshipdescription", "pages")},
        ),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )
    form = ResourcesMediaEventsForm


@admin.register(ResourceAltIndigenousName)
class ResourceAltIndigenousNameAdmin(VersionAdmin):
    fieldsets = (
        (
            "",
            {
                "fields": (("resourceid", "altindigenousname"),),
            },
        ),
    )
    form = ResourceAltIndigenousNameForm


class LocalityPlaceResourceEventAdmin(RecordAdminProxy):
    list_display = (
        "localityid",
        "placeresourceid",
        "enteredbyname",
        "enteredbydate",
        "modifiedbyname",
        "modifiedbydate",
    )
    fieldsets = (
        ("", {"fields": (("localityid", "placeresourceid"),)}),
        (
            "History",
            {
                "fields": (
                    (
                        "enteredbyname",
                        "enteredbytitle",
                        "enteredbytribe",
                        "enteredbydate",
                    ),
                    (
                        "modifiedbyname",
                        "modifiedbytitle",
                        "modifiedbytribe",
                        "modifiedbydate",
                    ),
                )
            },
        ),
    )


#####################
#### AUTH MODELS ####
#####################
@admin.register(Users)
class UsersAdmin(UserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "affiliation",
        "accesslevel",
        "title",
        "last_login",
        "date_joined",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "affiliation",
                    "title",
                )
            },
        ),
        (_("Permissions"), {"fields": ("accesslevel",)}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    search_fields = (
        "username",
        "first_name",
        "last_name",
        "affiliation",
        "emailtitle",
        "accesslevel__accesslevel",
    )


# admin.site.register(Locality, LocalityAdmin)
# admin.site.register(LocalityGISSelections)
# admin.site.register(LocalityPlaceResourceEvent, LocalityPlaceResourceEventAdmin)
admin.site.register(LookupActivity)
admin.site.register(LookupCustomaryUse)
admin.site.register(LookupHabitat)
# admin.site.register(LookupLocalityType)
admin.site.register(LookupMediaType)
admin.site.register(LookupParticipants)
admin.site.register(LookupPartUsed)
admin.site.register(LookupPlanningUnit)
admin.site.register(LookupReferenceType)
admin.site.register(LookupResourceGroup)
admin.site.register(LookupSeason)
admin.site.register(LookupTechniques)
admin.site.register(LookupTiming)
admin.site.register(LookupTribe)
admin.site.register(People)
# admin.site.register(PlaceGISSelections)
admin.site.register(UserAccess)

###Cruft
admin.site.register(LookupAuthorType)
admin.site.register(LookupUserInfo)
# admin.site.register(CurrentVersion)
