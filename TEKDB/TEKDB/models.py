# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from TEKDB import settings
from django.contrib.gis.db.models import GeometryField, GeoManager

MANAGED = True

class Queryable(models.Model):
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True, verbose_name='entered by name')
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True, verbose_name='entered by tribe')
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True, verbose_name='entered by title')
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True, auto_now_add=True, verbose_name='entered by date')
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True, verbose_name='modified by name')
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True, verbose_name='modified by title')
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True, verbose_name='modified by tribe')
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True, auto_now=True, verbose_name='modified by date')

    class Meta:
        abstract = True

    #Actually a dict, not true JSON.
    def get_query_json(self):
        return {
            'name': str(self),
            'image': self.image(),
            'subtitle': self.subtitle(),
            'data': self.data(),
            'link': self.link(),
            'enteredbyname': self.enteredbyname,
            'enteredbydate': self.enteredbydate,
            'modifiedbyname': self.modifiedbyname,
            'modifiedbydate': self.modifiedbydate,
        }

    def map(self):
        return None

    def get_record_dict(self):
        return {
            'name': str(self),
            'image': self.image(),
            'subtitle': self.subtitle(),
            'data': self.data(),
            'relationships': self.relationships(),
            'map': self.map(),
            'media': self.media(),
            # 'link': self.link(),
            'enteredbyname': self.enteredbyname,
            'enteredbydate': self.enteredbydate,
            'modifiedbyname': self.modifiedbyname,
            'modifiedbydate': self.modifiedbydate,
        }

    def media(self):
        return False

    def save(self, *args, **kwargs):
        #TODO: set entered/modified by info now
        super(Queryable, self).save(*args, **kwargs)


class LookupPlanningUnit(models.Model):
    planningunitid = models.AutoField(db_column='PlanningUnitID', primary_key=True)
    planningunitname = models.CharField(db_column='PlanningUnitName', max_length=100, blank=True, null=True, verbose_name='planning unit')

    class Meta:
        managed = MANAGED
        db_table = 'LookupPlanningUnit'
        app_label="Lookup"
        verbose_name="planning unit"
        verbose_name_plural="planning units"

    def __unicode__(self):
        return unicode("%s" % (self.planningunitname))

    def __str__(self):
        return self.planningunitname


class LookupTribe(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    tribeunit = models.CharField(db_column='TribeUnit', max_length=50, blank=True, null=True, verbose_name='tribe subunit')
    tribe = models.CharField(db_column='Tribe', max_length=100, blank=True, null=True, verbose_name='tribe')
    federaltribe = models.CharField(db_column='FederalTribe', max_length=100, blank=True, null=True, verbose_name='tribal government')

    class Meta:
        managed = MANAGED
        db_table = 'LookupTribe'
        app_label="Lookup"
        verbose_name="tribe"
        verbose_name_plural="tribes"

    def keyword_search(keyword):
        return LookupTribe.objects.filter(
            Q(tribeunit__icontains=keyword) |
            Q(tribe__icontains=keyword) |
            Q(federaltribe__icontains=keyword)
        )

    def __unicode__(self):
        return unicode("%s: %s, %s" % (self.tribe, self.tribeunit, self.federaltribe))

    def __str__(self):
        return "%s: %s, %s" % (self.tribe, self.tribeunit, self.federaltribe)

    def data(self):
        return [
            {'key':'tribe', 'value': self.tribe},
            {'key':'tribe subunit', 'value': self.tribeunit},
            {'key':'tribal government', 'value': self.federaltribe}
        ]

    def get_response_format(self):
        type = 'tribes'
        category_name = "Tribe"
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': None,
            'description': None,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class LookupHabitat(models.Model):
    habitat = models.CharField(db_column='Habitat', primary_key=True, max_length=100)

    class Meta:
        managed = MANAGED
        db_table = 'LookupHabitat'
        app_label="Lookup"
        verbose_name="habitat"
        verbose_name_plural="habitats"

    def __unicode__(self):
        return unicode('%s' % (self.habitat))

    def __str__(self):
        return self.habitat


class Places(Queryable):
    placeid = models.AutoField(db_column='PlaceID', primary_key=True)
    # PlaceID
    indigenousplacename = models.CharField(db_column='IndigenousPlaceName', max_length=255, blank=True, null=True, verbose_name='indigenous name')
    indigenousplacenamemeaning = models.CharField(db_column='IndigenousPlaceNameMeaning', max_length=255, blank=True, null=True, verbose_name='english translation')
    englishplacename = models.CharField(db_column='EnglishPlaceName', max_length=255, blank=True, null=True, verbose_name='english name')
    # PlaceLabel = models.CharField(max_length=255, blank=True, null=True, verbose_name='Place Label')
    planningunitid = models.ForeignKey(LookupPlanningUnit, db_column='PlanningUnitID', blank=True, null=True, verbose_name='planning unit')
    primaryhabitat = models.ForeignKey(LookupHabitat, db_column='PrimaryHabitat', max_length=100, blank=True, null=True, verbose_name='primary habitat')
    # FeatType = models.CharField(choices=FEATURE_TYPE_CHOICES)
    tribeid = models.ForeignKey(LookupTribe, db_column='TribeID', blank=True, null=True, verbose_name='tribe')
    islocked = models.BooleanField(db_column='IsLocked', default=False, verbose_name='locked?')
    ### Updated Geometry Fields ###
    objects = GeoManager()
    geometry = GeometryField(
        srid=3857,
        null=True, blank=True,
        verbose_name="Place Geometry",
        default=None
    )
    Source = models.CharField(max_length=255, blank=True, null=True, default=None, verbose_name='source')
    DigitizedBy = models.CharField(max_length=255, blank=True, null=True, default=None, verbose_name='digitized by')
    DigitizedDate = models.DateTimeField(blank=True, null=True, auto_now_add=False, default=None, verbose_name='digitized date')
    # PlaceDescription
    # SHAPE_Length
    # SHAPE_Area

    class Meta:
        managed = MANAGED
        db_table = 'Places'
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def keyword_search(keyword):
        planningunit_qs = LookupPlanningUnit.objects.filter(planningunitname__icontains=keyword)
        planningunit_loi = [planningunit.pk for planningunit in planningunit_qs]

        habitat_qs = LookupHabitat.objects.filter(habitat__icontains=keyword)
        habitat_loi = [habitat.pk for habitat in habitat_qs]

        tribe_qs = LookupTribe.keyword_search(keyword)
        tribe_loi = [tribe.pk for tribe in tribe_qs]

        return Places.objects.filter(
            Q(indigenousplacename__icontains=keyword) |
            Q(indigenousplacenamemeaning__icontains=keyword)|
            Q(englishplacename__icontains=keyword)|
            Q(planningunitid__in=planningunit_loi) |
            Q(primaryhabitat__in=habitat_loi) |
            Q(tribeid__in=tribe_loi)
        )

    def image(self):
        return settings.RECORD_ICONS['place']

    def subtitle(self):
        return self.indigenousplacenamemeaning

    def data(self):
        return [
            {'key':'indigenous place name', 'value': self.indigenousplacename},
            {'key':'english place name', 'value': self.englishplacename},
            {'key':'indigenous place name meaning', 'value': self.indigenousplacenamemeaning},
            {'key':'planning unit', 'value': str(self.planningunitid)},
            {'key':'primary habitat', 'value': str(self.primaryhabitat)},
            {'key':'tribe', 'value': str(self.tribeid)}
        ]

    def relationships(self):
        return [
            {'key':'Alternate Indigenous Names', 'value': [ainame.get_query_json() for ainame in  self.placealtindigenousname_set.all()]},
            {'key':'Resource Relationships', 'value': [res.get_query_json() for res in self.placesresourceevents_set.all()]},
            {'key':'Media Relationships', 'value': [media.get_query_json() for media in self.placesmediaevents_set.all()]},
            {'key':'Citation Relationships', 'value': [citation.get_query_json() for citation in self.placescitationevents_set.all()]},
            # {'key':'Localities', 'value': [media.get_query_json() for media in self.placesmediaevents_set.all()]},
        ]

    def map(self):
        try:
            geom = self.geometry.geojson
        except Exception:
            return False
        return geom

    def link(self):
        return '/explore/places/%d/' % self.pk

    def get_response_format(self):
        type = 'places'
        category_name = 'Place'
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.indigenousplacenamemeaning,
            'link': '/explore/%s/%d' % (type, self.pk)
        }

    def __unicode__(self):
        return unicode('%s (%s)' % (self.indigenousplacename, self.englishplacename))

    def __str__(self):
        return "%s (%s)" % (self.indigenousplacename, self.englishplacename)


class LookupResourceGroup(models.Model):
    resourceclassificationgroup = models.CharField(db_column='ResourceClassificationGroup', primary_key=True, max_length=255, verbose_name='broad species group')

    class Meta:
        managed = MANAGED
        db_table = 'LookupResourceGroup'
        app_label = 'Lookup'
        verbose_name="resource group"
        verbose_name_plural="resource groups"

    def __unicode__(self):
        return unicode('%s' % (self.resourceclassificationgroup))

    def __str__(self):
        return self.resourceclassificationgroup


class Resources(Queryable):
    resourceid = models.AutoField(db_column='ResourceID', primary_key=True)
    commonname = models.CharField(db_column='CommonName', max_length=255, blank=True, null=True, unique=True, verbose_name='common name')
    indigenousname = models.CharField(db_column='IndigenousName', max_length=255, blank=True, null=True, verbose_name='indigenous name')
    genus = models.CharField(db_column='Genus', max_length=255, blank=True, null=True, verbose_name='genus')
    species = models.CharField(db_column='Species', max_length=255, blank=True, null=True)
    specific = models.BooleanField(db_column='Specific', default=False)
    resourceclassificationgroup = models.ForeignKey(LookupResourceGroup, db_column='ResourceClassificationGroup', max_length=255, blank=True, null=True, verbose_name='broad species group')
    islocked = models.BooleanField(db_column='IsLocked', default=False, verbose_name='locked?')

    class Meta:
        managed = MANAGED
        db_table = 'Resources'
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'

    def __unicode__(self):
        return unicode('%s' % (self.commonname))

    def __str__(self):
        return self.commonname

    def keyword_search(keyword):
        group_qs = LookupResourceGroup.objects.filter(resourceclassificationgroup__icontains=keyword)
        group_loi = [group.pk for group in group_qs]

        return Resources.objects.filter(
            Q(commonname__icontains=keyword) |
            Q(indigenousname__icontains=keyword) |
            Q(genus__icontains=keyword) |
            Q(species__icontains=keyword) |
            Q(resourceclassificationgroup__in=group_loi)
        )

    def image(self):
        return settings.RECORD_ICONS['resource']

    def subtitle(self):
        return self.species

    def relationships(self):
        relationship_list = []
        placeresources = self.placesresourceevents_set.all()
        placeresourceidlist = [x.pk for x in placeresources]
        activities = [x.get_query_json() for x in ResourcesActivityEvents.objects.filter(placeresourceid__in=placeresourceidlist)]
        if len(activities) > 0:
            relationship_list.append({'key':'Activities', 'value': activities })
        media = [x.get_query_json() for x in self.resourcesmediaevents_set.all()]
        if len(media) > 0:
            relationship_list.append({'key':'Media', 'value':media })
        citations = [x.get_query_json() for x in self.resourcescitationevents_set.all()]
        if len(citations) > 0:
            relationship_list.append({'key':'Citations', 'value': citations})
        places = [x.get_query_json() for x in placeresources]
        if len(places) > 0:
            relationship_list.append({'key':'Places', 'value': places})
        # resources = [x.get_query_json() for x in self.resourceresourceevents_set.all()]
        # if len(resources) > 0:
        #     relationship_list.append({'key':'Resources', 'value': resources})
        return relationship_list

    def link(self):
        return '/explore/resources/%d/' % self.pk

    def data(self):
        return [
            {'key':'name', 'value': self.commonname},
            {'key':'indigenous name', 'value': self.indigenousname},
            {'key':'genus', 'value': self.genus},
            {'key':'species', 'value': self.species},
            {'key':'broad species group', 'value': str(self.resourceclassificationgroup)}
        ]

    def get_response_format(self):
        type = 'resources'
        category_name = 'Resource'
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.indigenousname,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class LookupPartUsed(models.Model):
    partused = models.CharField(db_column='PartUsed', primary_key=True, max_length=255, verbose_name='part used')

    class Meta:
        managed = MANAGED
        db_table = 'LookupPartUsed'
        app_label="Lookup"
        verbose_name="part used"
        verbose_name_plural="parts used"

    def __unicode__(self):
        return unicode('%s' % (self.partused))

    def __str__(self):
        return self.partused


class LookupCustomaryUse(models.Model):
    usedfor = models.CharField(db_column='UsedFor', primary_key=True, max_length=255, verbose_name='used_for')

    class Meta:
        managed = MANAGED
        db_table = 'LookupCustomaryUse'
        app_label="Lookup"
        verbose_name="customary use"
        verbose_name_plural="customary uses"

    def __unicode__(self):
        return unicode('%s' % (self.usedfor))

    def __str__(self):
        return self.usedfor


class LookupSeason(models.Model):
    season = models.CharField(db_column='Season', primary_key=True, max_length=255)

    class Meta:
        managed = MANAGED
        db_table = 'LookupSeason'
        app_label="Lookup"
        verbose_name="season"
        verbose_name_plural="seasons"

    def __unicode__(self):
        return unicode('%s' % (self.season))

    def __str__(self):
        return self.season


class LookupTiming(models.Model):
    timing = models.CharField(db_column='Timing', primary_key=True, max_length=255)

    class Meta:
        managed = MANAGED
        db_table = 'LookupTiming'
        app_label="Lookup"
        verbose_name="timing"
        verbose_name_plural="timings"

    def __unicode__(self):
        return unicode('%s' % (self.timing))

    def __str__(self):
        return self.timing


class PlacesResourceEvents(Queryable):
    placeresourceid = models.AutoField(db_column='PlaceResourceID', primary_key=True)
    placeid = models.ForeignKey(Places, db_column='PlaceID', verbose_name='place')
    resourceid = models.ForeignKey(Resources, db_column='ResourceID', verbose_name='resource')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    partused = models.ForeignKey(LookupPartUsed, db_column='PartUsed', max_length=255, blank=True, null=True, verbose_name='part used')
    customaryuse = models.ForeignKey(LookupCustomaryUse, db_column='CustomaryUse', max_length=255, blank=True, null=True, verbose_name='customary use')
    barterresource = models.BooleanField(db_column='BarterResource', verbose_name='barter resource?', default=False)
    season = models.ForeignKey(LookupSeason, db_column='Season', max_length=255, blank=True, null=True)
    timing = models.ForeignKey(LookupTiming, db_column='Timing', max_length=255, blank=True, null=True)
    january = models.BooleanField(db_column='January', default=False)
    february = models.BooleanField(db_column='February', default=False)
    march = models.BooleanField(db_column='March', default=False)
    april = models.BooleanField(db_column='April', default=False)
    may = models.BooleanField(db_column='May', default=False)
    june = models.BooleanField(db_column='June', default=False)
    july = models.BooleanField(db_column='July', default=False)
    august = models.BooleanField(db_column='August', default=False)
    september = models.BooleanField(db_column='September', default=False)
    october = models.BooleanField(db_column='October', default=False)
    november = models.BooleanField(db_column='November', default=False)
    december = models.BooleanField(db_column='December', default=False)
    year = models.IntegerField(db_column='Year', blank=True, null=True)
    islocked = models.BooleanField(db_column='IsLocked', verbose_name='locked?', default=False)

    class Meta:
        managed = MANAGED
        db_table = 'PlacesResourceEvents'
        app_label = 'Relationships'
        verbose_name = 'Place - Resource'
        verbose_name_plural = 'Places - Resources'

    def keyword_search(keyword):
        resource_qs = Resources.keyword_search(keyword)
        resource_loi = [resource.pk for resource in resource_qs]

        place_qs = Places.keyword_search(keyword)
        place_loi = [place.pk for place in place_qs]

        part_qs = LookupPartUsed.objects.filter(partused__icontains=keyword)
        part_loi = [part.partused for part in part_qs]

        use_qs = LookupCustomaryUse.objects.filter(usedfor__icontains=keyword)
        use_loi = [use.usedfor for use in use_qs]

        season_qs = LookupSeason.objects.filter(season__icontains=keyword)
        season_loi = [season.season for season in season_qs]

        timing_qs = LookupTiming.objects.filter(timing__icontains=keyword)
        timing_loi = [timing.timing for timing in timing_qs]

        return PlacesResourceEvents.objects.filter(
            Q(resourceid__in=resource_loi) |
            Q(placeid__in=place_loi) |
            Q(relationshipdescription__icontains=keyword) |
            Q(partused__in=part_loi) |
            Q(customaryuse__in=use_loi) |
            Q(season__in=season_loi) |
            Q(timing__in=timing_loi)
        )

    def __unicode__(self):
        return unicode("%s at %s" % (str(self.resourceid), str(self.placeid)))

    def __str__(self):
        return "%s at %s" % (str(self.resourceid), str(self.placeid))

    def image(self):
        return settings.RECORD_ICONS['activity']

    def subtitle(self):
        return self.relationshipdescription

    def data(self):
        if self.barterresource:
            barter = 'Yes'
        else:
            barter = 'No'

        months_list = [
            x for x in [
                'january', 'february', 'march', 'april', 'may', 'june', 'july',
                'august', 'september', 'october', 'november', 'december'
            ] if self.__getattribute__(x)
        ]
        if len(months_list) > 0:
            months = ', '.join(months_list)
        else:
            months = 'None'

        return [
            {'key':'place', 'value': str(self.placeid)},
            {'key':'resource', 'value': str(self.resourceid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'part used', 'value': str(self.partused)},
            {'key':'customary use', 'value': str(self.customaryuse)},
            {'key':'used for barter', 'value': barter},
            {'key':'season', 'value': str(self.season)},
            {'key':'timing', 'value': str(self.timing)},
            {'key':'months', 'value': months},
            {'key':'year', 'value': str(self.timing)},
        ]

    def link(self):
        return '/explore/placesresourceevents/%s' % self.pk

    def relationships(self):
        relationship_list = []
        relationship_list.append({'key':'Place', 'value': [self.placeid.get_query_json()]})
        relationship_list.append({'key':'Resource', 'value': [self.resourceid.get_query_json()]})
        activities = [x.get_query_json() for x in self.resourcesactivityevents_set.all()]
        if len(activities) > 0:
            relationship_list.append({'key':'Activities', 'value': activities})
        return relationship_list

    def get_response_format(self):
        type = 'Placesresourceevents'
        category_name = 'Place - Resource'
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class LookupParticipants(models.Model):
    participants = models.CharField(db_column='Participants', primary_key=True, max_length=255)

    class Meta:
        managed = MANAGED
        db_table = 'LookupParticipants'
        app_label = "Lookup"
        verbose_name = "participant"
        verbose_name_plural = "participants"

    def __unicode__(self):
        return unicode('%s' % (self.participants))

    def __str__(self):
        return self.participants


class LookupTechniques(models.Model):
    techniques = models.CharField(db_column='Techniques', primary_key=True, max_length=255)

    class Meta:
        managed = MANAGED
        db_table = 'LookupTechniques'
        app_label = "Lookup"
        verbose_name = "technique"
        verbose_name_plural = "techniques"

    def __unicode__(self):
        return unicode('%s' % (self.techniques))

    def __str__(self):
        return self.techniques


class LookupActivity(models.Model):
    activity = models.CharField(db_column='Activity', primary_key=True, max_length=255)

    class Meta:
        managed = MANAGED
        db_table = 'LookupActivity'
        app_label = 'Lookup'
        verbose_name = 'activity'
        verbose_name_plural = 'activities'

    def __unicode__(self):
        return unicode('%s' % (self.activity))

    def __str__(self):
        return self.activity


class ResourcesActivityEvents(Queryable):
    resourceactivityid = models.AutoField(db_column='ResourceActivityID', primary_key=True)
    placeresourceid = models.ForeignKey(PlacesResourceEvents, db_column='PlaceResourceID', verbose_name='place resource')
    relationshipdescription = models.TextField(db_column='RelationshipDescription', blank=True, null=True, verbose_name='relationship description')
    partused = models.ForeignKey(LookupPartUsed, db_column='PartUsed', max_length=255, blank=True, null=True, verbose_name='part used')
    activityshortdescription = models.ForeignKey(LookupActivity, db_column='ActivityShortDescription', max_length=255, blank=True, null=True, verbose_name='activity type')
    activitylongdescription = models.TextField(db_column='ActivityLongDescription', blank=True, null=True, verbose_name='full activity description')
    participants = models.ForeignKey(LookupParticipants, db_column='Participants', max_length=50, blank=True, null=True)
    technique = models.ForeignKey(LookupTechniques, db_column='Technique', max_length=255, blank=True, null=True)
    gear = models.CharField(db_column='Gear', max_length=255, blank=True, null=True)
    customaryuse = models.CharField(db_column='CustomaryUse', max_length=255, blank=True, null=True, verbose_name='customary use')
    timing = models.ForeignKey(LookupTiming, db_column='Timing', max_length=255, blank=True, null=True)
    timingdescription = models.CharField(db_column='TimingDescription', max_length=255, blank=True, null=True, verbose_name='timing description')
    islocked = models.BooleanField(db_column='IsLocked', default=False, verbose_name='locked?')

    class Meta:
        managed = MANAGED
        db_table = 'ResourcesActivityEvents'
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __unicode__(self):
        return unicode("%s: %s" % (str(self.placeresourceid), self.activityshortdescription))

    def __str__(self):
        return "%s: %s" % (str(self.placeresourceid), self.activityshortdescription)

    def keyword_search(keyword):
        placeresource_qs = PlacesResourceEvents.keyword_search(keyword)
        placeresource_loi = [placeresource.pk for placeresource in placeresource_qs]

        part_qs = LookupPartUsed.objects.filter(partused__icontains=keyword)
        part_loi = [part.partused for part in part_qs]

        activity_qs = LookupActivity.objects.filter(activity__icontains=keyword)
        activity_loi = [activity.activity for activity in activity_qs]

        participant_qs = LookupParticipants.objects.filter(participants__icontains=keyword)
        participant_loi = [participant.participants for participant in participant_qs]

        technique_qs = LookupTechniques.objects.filter(techniques__icontains=keyword)
        technique_loi = [technique.techniques for technique in technique_qs]

        use_qs = LookupCustomaryUse.objects.filter(usedfor__icontains=keyword)
        use_loi = [use.usedfor for use in use_qs]

        timing_qs = LookupTiming.objects.filter(timing__icontains=keyword)
        timing_loi = [timing.timing for timing in timing_qs]

        return ResourcesActivityEvents.objects.filter(
            Q(placeresourceid__in=placeresource_loi) |
            Q(relationshipdescription__icontains=keyword) |
            Q(partused__in=part_loi) |
            Q(activityshortdescription__in=activity_loi) |
            Q(activitylongdescription__icontains=keyword) |
            Q(participants__in=participant_loi) |
            Q(technique__in=technique_loi) |
            Q(gear__icontains=keyword) |
            Q(customaryuse__in=use_loi) |
            Q(timing__in=timing_loi) |
            Q(timingdescription__icontains=keyword)
        )

    def image(self):
        return settings.RECORD_ICONS['activity']

    def subtitle(self):
        return self.relationshipdescription

    def link(self):
        return '/explore/resourcesactivityevents/%d/' % self.pk

    def relationships(self):
        relationship_list = []
        relationship_list.append({'key':'Place-Resource Relationship', 'value': [self.placeresourceid.get_query_json()]})
        citations = [x.get_query_json() for x in self.resourceactivitycitationevents_set.all()]
        if len(citations) > 0:
            relationship_list.append({'key':'Citation Relationships', 'value': citations})
        media = [x.get_query_json() for x in self.resourceactivitymediaevents_set.all()]
        if len(media) > 0:
            relationship_list.append({'key':'Media Relationships', 'value': media})
        return relationship_list

    def data(self):
        return [
            {'key':'place', 'value': str(self.placeresourceid.placeid)},
            {'key':'resource', 'value': str(self.placeresourceid.resourceid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'part used', 'value': str(self.partused)},
            {'key':'activity type', 'value': str(self.activityshortdescription)},
            {'key':'full description', 'value': self.activitylongdescription},
            {'key':'participants', 'value': str(self.participants)},
            {'key':'technique', 'value': str(self.technique)},
            {'key':'gear', 'value': self.gear},
            {'key':'customary use', 'value': str(self.customaryuse)},
            {'key':'timing', 'value': str(self.timing)},
            {'key':'timing description', 'value': self.timingdescription}
        ]

    def get_response_format(self):
        type = 'Resourcesactivityevents'
        category_name = 'Activity'
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class People(models.Model):
    personid = models.AutoField(db_column='PersonID', primary_key=True)
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True, verbose_name='first name')
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True, verbose_name='last name')
    yearborn = models.IntegerField(db_column='YearBorn', blank=True, null=True, verbose_name='year born')
    village = models.CharField(db_column='Village', max_length=255, blank=True, null=True)
    relationshiptootherpeople = models.TextField(db_column='RelationshipToOtherPeople', blank=True, null=True, verbose_name='relationship to other people')

    class Meta:
        managed = MANAGED
        db_table = 'People'
        app_label = "Lookup"
        verbose_name = "person"
        verbose_name_plural = "people"

    def keyword_search(keyword):
        return People.objects.filter(
            Q(firstname__icontains=keyword) |
            Q(lastname__icontains=keyword) |
            Q(village__icontains=keyword) |
            Q(relationshiptootherpeople__icontains=keyword)
        )

    def __unicode__(self):
        return unicode("%s %s" % (self.firstname, self.lastname))

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)

    def image(self):
        #TODO: Better icon or no icon
        return '/static/explore/img/activity.png'

    def data(self):
        return [
            {'key':'first name', 'value': self.firstname},
            {'key':'last name', 'value': self.lastname},
            {'key':'year born', 'value': str(self.yearborn)},
            {'key':'village', 'value': self.village},
            {'key':'relationship to others', 'value': self.relationshiptootherpeople}
        ]

    def link(self):
        return '/explore/people/%s' % self.pk

    def relationships(self):
        relationship_list = []
        interviewee_citations = [x.get_query_json() for x in self.interviewee.all()]
        interviewer_citations = [x.get_query_json() for x in self.interviewer.all()]
        # citations = list(set(interviewee_citations) | set(interviewer_citations))
        if len(interviewee_citations) > 0:
            relationship_list.append({'key': 'Citations as interviewee', 'value': interviewee_citations})
        if len(interviewer_citations) > 0:
            relationship_list.append({'key': 'Citations as interviewer', 'value': interviewer_citations})
        return relationship_list

    #Actually a dict, not true JSON.
    def get_query_json(self):
        return {
            'name': str(self),
            'image': self.image(),
            'subtitle': self.village,
            'data': self.data(),
            'link': self.link()
        }

    def get_record_dict(self):
        return {
            'name': str(self),
            'image': self.image(),
            'subtitle': self.village,
            'data': self.data(),
            'relationships': self.relationships(),
            'map': False,
            # 'link': self.link(),
        }


class LookupReferenceType(models.Model):
    documenttype = models.CharField(db_column='DocumentType', primary_key=True, max_length=25, verbose_name='document type')

    class Meta:
        managed = MANAGED
        db_table = 'LookupReferenceType'
        app_label = "Lookup"
        verbose_name="reference type"
        verbose_name_plural="reference types"

    def __unicode__(self):
        return unicode('%s' % (self.documenttype))

    def __str__(self):
        return self.documenttype


class LookupAuthorType(models.Model):
    authortype = models.CharField(db_column='AuthorType', primary_key=True, max_length=50, verbose_name='author type')

    class Meta:
        managed = MANAGED
        db_table = 'LookupAuthorType'
        app_label = 'Lookup'
        verbose_name = 'author type'
        verbose_name_plural = 'author types'


    def __unicode__(self):
        return unicode('%s' % (self.authortype))

    def __str__(self):
        return self.authortype


class Citations(Queryable):
    citationid = models.AutoField(db_column='CitationID', primary_key=True)
    referencetype = models.ForeignKey(LookupReferenceType, db_column='ReferenceType', max_length=255, verbose_name='reference type', help_text="Select a reference type to continue")
    referencetext = models.CharField(db_column='ReferenceText', max_length=50, blank=True, null=True, verbose_name='description')
    authortype = models.ForeignKey(LookupAuthorType, db_column='AuthorType', max_length=255, blank=True, null=True, verbose_name='author type')
    authorprimary = models.CharField(db_column='AuthorPrimary', max_length=255, blank=True, null=True, verbose_name='primary author')
    authorsecondary = models.CharField(db_column='AuthorSecondary', max_length=255, blank=True, null=True, verbose_name='secondary author')
    intervieweeid = models.ForeignKey(People, db_column='IntervieweeID', related_name='interviewee', blank=True, null=True, verbose_name='interviewee')
    interviewerid = models.ForeignKey(People, db_column='InterviewerID', related_name='interviewer', blank=True, null=True, verbose_name='interviewer')
    placeofinterview = models.CharField(db_column='PlaceofInterview', max_length=255, blank=True, null=True, verbose_name='place of interview')
    year = models.IntegerField(db_column='Year', blank=True, null=True)
    title = models.TextField(db_column='Title', blank=True, null=True)
    seriestitle = models.CharField(db_column='SeriesTitle', max_length=255, blank=True, null=True, verbose_name='series title')
    seriesvolume = models.CharField(db_column='SeriesVolume', max_length=50, blank=True, null=True, verbose_name='series volume')
    serieseditor = models.CharField(db_column='SeriesEditor', max_length=255, blank=True, null=True, verbose_name='series editor')
    publisher = models.CharField(db_column='Publisher', max_length=100, blank=True, null=True)
    publishercity = models.CharField(db_column='PublisherCity', max_length=255, blank=True, null=True, verbose_name='city')
    preparedfor = models.CharField(db_column='PreparedFor', max_length=100, blank=True, null=True, verbose_name='prepared_for')
    comments = models.TextField(db_column='Comments', blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'Citations'
        verbose_name = 'Citation'
        verbose_name_plural = 'Citations'

    def keyword_search(keyword):
        reference_qs = LookupReferenceType.objects.filter(documenttype__icontains=keyword)
        reference_loi = [reference.documenttype for reference in reference_qs]

        authortype_qs = LookupAuthorType.objects.filter(authortype__icontains=keyword)
        authortype_loi = [authortype.authortype for authortype in authortype_qs]

        people_qs = People.keyword_search(keyword)
        people_loi = [person.pk for person in people_qs]

        return Citations.objects.filter(
            Q(referencetype__in=reference_loi) |
            Q(referencetext__icontains=keyword) |
            Q(authortype__in=authortype_loi) |
            Q(authorprimary__icontains=keyword) |
            Q(authorsecondary__icontains=keyword) |
            Q(intervieweeid__in=people_loi) |
            Q(interviewerid__in=people_loi) |
            Q(placeofinterview__icontains=keyword) |
            Q(title__icontains=keyword) |
            Q(seriestitle__icontains=keyword) |
            Q(seriesvolume__icontains=keyword) |
            Q(serieseditor__icontains=keyword) |
            Q(publisher__icontains=keyword) |
            Q(publishercity__icontains=keyword) |
            Q(preparedfor__icontains=keyword) |
            Q(comments__icontains=keyword)
        )

    def image(self):
        return settings.RECORD_ICONS['citation']

    def subtitle(self):
        return self.referencetext

    def link(self):
        return '/explore/citations/%d/' % self.pk

    def relationships(self):
        relationship_list = []
        if self.referencetype.documenttype == 'Interview':
            people = []
            if not self.intervieweeid == None:
                people.append(self.intervieweeid.get_query_json())
            if not self.interviewerid == None:
                people.append(self.interviewerid.get_query_json())
            if len(people) > 0:
                relationship_list.append({'key':'People', 'value': people})
        places = [x.get_query_json() for x in self.placescitationevents_set.all()]
        if len(places) > 0:
            relationship_list.append({'key': 'Place Relationships', 'value': places})
        resources = [x.get_query_json() for x in self.resourcescitationevents_set.all()]
        if len(resources) > 0:
            relationship_list.append({'key': 'Resource Relationships', 'value': resources})
        media = [x.get_query_json() for x in self.mediacitationevents_set.all()]
        if len(media) > 0:
            relationship_list.append({'key': 'Media Relationships', 'value': media})
        activities = [x.get_query_json() for x in self.resourceactivitycitationevents_set.all()]
        if len(activities) > 0:
            relationship_list.append({'key': 'Activity Relationships', 'value': activities})

        return relationship_list

    def data(self):
        #TODO: Return different results for different reference types
        return [
            {'key':'reference type', 'value': str(self.referencetype)},
            {'key':'description', 'value': self.referencetext},
            {'key':'title', 'value': self.title},
            {'key':'author type', 'value': str(self.authortype)},
            {'key':'primary author', 'value': self.authorprimary},
            {'key':'secondary author', 'value': self.authorsecondary},
            {'key':'year', 'value': self.year},
            {'key':'series volume', 'value': self.seriesvolume},
            {'key':'series title', 'value': self.seriestitle},
            {'key':'series editor', 'value': self.serieseditor},
            {'key':'interviewee', 'value': str(self.intervieweeid)},
            {'key':'interviewer', 'value': str(self.interviewerid)},
            {'key':'place of interview', 'value': self.placeofinterview},
            {'key':'prepared for', 'value': self.preparedfor},
            {'key':'publisher', 'value': self.publisher},
            {'key':'publisher city', 'value': self.publishercity},
            {'key':'comments', 'value': self.comments},
        ]

    def get_response_format(self):
        type = 'citations'
        category_name = 'Citation'
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.referencetext,
            'link': '/explore/%s/%d' % (type, self.pk)
        }

    def __str__(self):
        if str(self.referencetype) == 'Interview':
            try:
                interviewee = People.objects.get(pk=self.intervieweeid.pk)
            except Exception as e:
                interviewee = 'Unknown Interviewee'
            # return '[%s] %s (%d) - %d' % (str(self.referencetype), interviewee, self.year, self.pk)
            return '[%s] %s (%s)' % (str(self.referencetype), str(interviewee), str(self.year))
        else:
            return '[%s] %s (%s)' % (str(self.referencetype), str(self.title), str(self.year))

    def __unicode__(self):
        return unicode('%s' % (str(self)))


class PlacesCitationEvents(Queryable):
    placeid = models.ForeignKey(Places, db_column='PlaceID', primary_key=False, verbose_name='place')
    citationid = models.ForeignKey(Citations, db_column='CitationID', verbose_name='citation')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'PlacesCitationEvents'
        app_label = "Relationships"
        verbose_name = 'Place - Citation'
        verbose_name_plural = 'Places - Citations'
        unique_together = (('placeid', 'citationid'),)

    def __unicode__(self):
        return unicode("%s %s" % (str(self.placeid), str(self.citationid)))

    def __str__(self):
        return "%s %s" % (str(self.placeid), str(self.citationid))

    def keyword_search(keyword):
        place_qs = Places.keyword_search(keyword)
        place_loi = [place.pk for place in place_qs]

        citation_qs = Citations.keyword_search(keyword)
        citation_loi = [citation.pk for citation in citation_qs]

        return PlacesCitationEvents.objects.filter(
            Q(citationid__in=citation_loi) |
            Q(placeid__in=place_loi) |
            Q(relationshipdescription__icontains=keyword)
        )

    def image(self):
        return settings.RECORD_ICONS['activity']

    def subtitle(self):
        return self.relationshipdescription

    def link(self):
        return '/explore/placescitationevents/%d/' % self.pk

    def relationships(self):
        relationship_list = []
        relationship_list.append({'key': 'Place', 'value': [self.placeid.get_query_json()]})
        relationship_list.append({'key': 'Citation', 'value': [self.citationid.get_query_json()]})
        return relationship_list

    def data(self):
        return [
            {'key':'place', 'value': str(self.placeid)},
            {'key':'citation', 'value': str(self.citationid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}
        ]

    def get_response_format(self):
        type = 'Placescitationevents'
        category_name = 'Place - Citation'
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


# Appears to be the version of AccessDB(s). Export gave 1 entry: [1,1,1]
class CurrentVersion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    backendversion = models.IntegerField(db_column='BackendVersion', blank=True, null=True, verbose_name='backend version')
    frontendversion = models.IntegerField(db_column='FrontendVersion', blank=True, null=True, verbose_name='frontend version')

    class Meta:
        managed = MANAGED
        db_table = 'CurrentVersion'
        app_label = 'Lookup'
        verbose_name = 'current version'
        verbose_name_plural = 'current versions'

    def __unicode__(self):
        return unicode("Back: %d, Front:%d" % (self.backendversion, self.frontendversion))

    def __str__(self):
        return "Back: %d, Front:%d" % (self.backendversion, self.frontendversion)


class LookupLocalityType(models.Model):
    localitytype = models.CharField(db_column='LocalityType', primary_key=True, max_length=255, verbose_name='locality type')

    class Meta:
        managed = MANAGED
        db_table = 'LookupLocalityType'
        app_label = "Lookup"
        verbose_name = "locality type"
        verbose_name_plural = "locality types"

    def __unicode__(self):
        return unicode('%s' % (self.localitytype))

    def __str__(self):
        return self.localitytype


class Locality(Queryable):
    localityid = models.AutoField(db_column='LocalityID', primary_key=True)
    placeid = models.ForeignKey(Places, db_column='PlaceID', blank=True, null=True, verbose_name='place')
    englishname = models.CharField(db_column='EnglishName', max_length=255, blank=True, null=True, verbose_name='english name')
    indigenousname = models.CharField(db_column='IndigenousName', max_length=255, blank=True, null=True, verbose_name='indigenous name')
    localitytype = models.ForeignKey(LookupLocalityType, db_column='LocalityType', max_length=255, blank=True, null=True, verbose_name='type')
    ### Updated Geometry Fields ###
    objects = GeoManager()
    geometry = GeometryField(
        srid=3857,
        null=True, blank=True,
        verbose_name="Place Geometry",
        default=None
    )
    Source = models.CharField(max_length=255, blank=True, null=True, default=None, verbose_name='source')
    DigitizedBy = models.CharField(max_length=255, blank=True, null=True, default=None, verbose_name='digitized by')
    DigitizedDate = models.DateTimeField(blank=True, null=True, auto_now_add=False, default=None, verbose_name='digitized date')

    class Meta:
        managed = MANAGED
        db_table = 'Locality'
        verbose_name = 'Locality'
        verbose_name_plural = 'Localities'

    def __unicode__(self):
        if self.englishname:
            return unicode('%s' % (self.englishname))
        else:
            return unicode('Locality in %s' % (self.placeid.englishplacename))

    def __str__(self):
        if self.englishname:
            return self.englishname
        else:
            return ('Locality in %s' % (self.placeid.englishplacename))

    def keyword_search(keyword):
        place_qs = Places.keyword_search(keyword)
        place_loi = [place.pk for place in place_qs]

        locality_qs = LookupLocalityType.objects.filter(localitytype__icontains=keyword)
        locality_loi = [locality.localitytype for locality in locality_qs]

        return Locality.objects.filter(
            Q(placeid__in=place_loi) |
            Q(englishname__icontains=keyword) |
            Q(indigenousname__icontains=keyword) |
            Q(localitytype__in=locality_loi)
        )

    def image(self):
        return settings.RECORD_ICONS['place']

    def subtitle(self):
        return self.indigenousname

    def link(self):
        return '/explore/locality/%d/' % self.pk

    def relationships(self):
        relationship_list = []
        relationship_list.append({'key': 'Place', 'value':[self.placeid.get_query_json()]})
        placeresources = [x.get_query_json() for x in self.localityplaceresourceevents_set.all()]
        if len(placeresources) > 0:
            relationship_list.append({'key': 'Place-resource Relationships', 'value': placeresources})
        gisselections = [x.get_query_json() for x in self.localitygisselections_set.all()]
        if len(gisselections) > 0:
            relationship_list.append({'key': 'GIS Selections', 'value': gisselections})
        return relationship_list

    def map(self):
        try:
            geom = self.geometry.geojson
        except Exception:
            return False
        return geom

    def data(self):
        return [
            {'key':'english name', 'value': self.englishname},
            {'key':'indigenous name', 'value': self.indigenousname},
            {'key':'place', 'value': str(self.placeid)},
            {'key':'locality type', 'value': str(self.localitytype)}
        ]

    def get_response_format(self):
        type = 'locality'
        category_name = "Locality"
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.indigenousname,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class LocalityGISSelections(models.Model):
    localityid = models.ForeignKey(Locality, db_column='LocalityID', blank=True, null=True, verbose_name='locality')
    localitylabel = models.CharField(db_column='LocalityLabel', max_length=255, blank=True, null=True, verbose_name='locality label')
    sourcefc = models.CharField(db_column='SourceFC', max_length=255, blank=True, null=True, verbose_name='source fc')

    class Meta:
        managed = MANAGED
        db_table = 'LocalityGISSelections'
        app_label = 'Relationships'
        verbose_name_plural = 'Locality GIS Selections'

    def __unicode__(self):
        return unicode('%s' % (self.localitylabel))

    def __str__(self):
        return self.localitylabel


class LocalityPlaceResourceEvent(Queryable):
    placeresourceid = models.ForeignKey(PlacesResourceEvents, db_column='PlaceResourceID', primary_key=False, verbose_name='place resource')
    localityid = models.ForeignKey(Locality, db_column='LocalityID', verbose_name='locality')

    class Meta:
        managed = MANAGED
        db_table = 'LocalityPlaceResourceEvent'
        unique_together = (('placeresourceid', 'localityid'),)
        app_label = 'Relationships'
        verbose_name_plural = 'Localities - Place-Resources'

    def __unicode__(self):
        return unicode("%s - %s" % (str(self.localityid), str(self.placeresourceid)))

    def __str__(self):
        return "%s - %s" % (str(self.localityid), str(self.placeresourceid))

    def keyword_search(keyword):
        locality_qs = Locality.keyword_search(keyword)
        locality_loi = [locality.pk for locality in locality_qs]

        placeresource_qs = PlacesResourceEvents.keyword_search(keyword)
        placeresource_loi = [placeresource.pk for placeresource in placeresource_qs]

        return LocalityPlaceResourceEvent.objects.filter(
            Q(placeresourceid__in=placeresource_loi) |
            Q(localityid__in=locality_loi)
        )

    def image(self):
        return settings.RECORD_ICONS['activity']

    def subtitle(self):
        return ''

    def link(self):
        return '/explore/localityplaceresourceevent/%d/' % self.pk

    def relationships(self):
        relationship_list = []
        relationship_list.append({'key': 'Place-Resource', 'value': [self.placeresourceid.get_query_json()]})
        relationship_list.append({'key': 'Locality', 'value': [self.localityid.get_query_json()]})
        return relationship_list

    def data(self):
        return [
            {'key':'place', 'value': str(self.placeresourceid.placeid)},
            {'key':'resource', 'value': str(self.placeresourceid.resourceid)},
            {'key':'locality', 'value': str(self.localityid)}
        ]

    def get_response_format(self):
        type = 'Placescitationevents'
        category_name = "Place - Citation"
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': 'locality place resource event',
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class LookupMediaType(models.Model):
    mediatype = models.CharField(db_column='MediaType', primary_key=True, max_length=255, verbose_name='type')
    mediacategory = models.CharField(db_column='MediaCategory', max_length=255, blank=True, null=True, verbose_name='category')

    class Meta:
        managed = MANAGED
        db_table = 'LookupMediaType'
        app_label = 'Lookup'
        verbose_name="media type"
        verbose_name_plural="media types"

    def __unicode__(self):
        return unicode('%s' % (self.mediatype))

    def __str__(self):
        return self.mediatype

    def keyword_search(keyword):
        return LookupMediaType.objects.filter(
            Q(mediatype__icontains=keyword),
            Q(mediacategory__icontains=keyword),
        )


class LookupUserInfo(models.Model):
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True, verbose_name='username')
    usingcustomusername = models.BooleanField(db_column='UsingCustomUsername', default=False, verbose_name='using custom username')
    usertitle = models.CharField(db_column='UserTitle', max_length=100, blank=True, null=True, verbose_name='title')
    useraffiliation = models.CharField(db_column='UserAffiliation', max_length=100, blank=True, null=True, verbose_name='affiliation')

    class Meta:
        managed = MANAGED
        db_table = 'LookupUserInfo'
        app_label = 'Lookup'
        verbose_name = 'user info'
        verbose_name_plural = 'user info'

    def __unicode__(self):
        return unicode('%s' % (self.username))

    def __str__(self):
        return self.username


class Media(Queryable):
    mediaid = models.AutoField(db_column='MediaID', primary_key=True)
    mediatype = models.ForeignKey(LookupMediaType, db_column='MediaType', max_length=255, blank=True, null=True, verbose_name='type')
    medianame = models.CharField(db_column='MediaName', max_length=255, blank=True, null=True, verbose_name='name')
    mediadescription = models.TextField(db_column='MediaDescription', blank=True, null=True, verbose_name='description')
    medialink = models.CharField(db_column='MediaLink', max_length=255, blank=True, null=True, verbose_name='historic location')
    mediafile = models.FileField(db_column='MediaFile', max_length=255, blank=True, null=True, verbose_name='file')

    class Meta:
        managed = MANAGED
        db_table = 'Media'
        verbose_name = 'Medium'
        verbose_name_plural = 'Media'

    def __unicode__(self):
        return unicode('%s' % (self.medianame))

    def __str__(self):
        return self.medianame

    def keyword_search(keyword):
        type_qs = LookupMediaType.keyword_search(keyword)
        type_loi = [mtype.pk for mtype in type_qs]

        return Media.objects.filter(
            Q(mediatype__in=type_loi) |
            Q(medianame__icontains=keyword)|
            Q(mediadescription__icontains=keyword) |
            Q(medialink__icontains=keyword)
        )

    def image(self):
        return settings.RECORD_ICONS['media']

    def subtitle(self):
        return self.mediatype

    def link(self):
        return '/explore/media/%d/' % self.pk

    def relationships(self):
        relationship_list = []
        places = [x.get_query_json() for x in self.placesmediaevents_set.all()]
        if len(places) > 0:
            relationship_list.append({'key': 'Place Relationships', 'value': places})
        resources = [x.get_query_json() for x in self.resourcesmediaevents_set.all()]
        if len(resources) > 0:
            relationship_list.append({'key': 'Resource Relationships', 'value': resources})
        citations = [x.get_query_json() for x in self.mediacitationevents_set.all()]
        if len(citations) > 0:
            relationship_list.append({'key': 'Citation Relationships', 'value': citations})
        activities = [x.get_query_json() for x in self.resourceactivitymediaevents_set.all()]
        if len(activities) > 0:
            relationship_list.append({'key': 'Activity Relationships', 'value': activities})
        placeresources = [x.get_query_json() for x in self.placesresourcemediaevents_set.all()]
        if len(placeresources) > 0:
            relationship_list.append({'key': 'Place-Resource Relationships', 'value': placeresources})
        return relationship_list

    def media(self):
        if not self.medialink == None or not self.mediafile == None:
            return {
                'file': str(self.mediafile),
                'type': str(self.mediatype),
            }
        else:
            return False

    def data(self):
        from TEKDB.settings import MEDIA_URL
        if self.mediafile == None:
            mediafile = 'None'
        else:
            mediafile = "<a class='record-link' href='%s%s'>%s</a>" % (MEDIA_URL, str(self.mediafile), str(self.mediafile))

        return [
            {'key':'name', 'value': self.medianame},
            {'key':'media type', 'value': str(self.mediatype)},
            {'key':'media description', 'value': self.mediadescription},
            # {'key':'link', 'value': self.medialink},
            {'key':'file', 'value': mediafile},
        ]

    def get_response_format(self):
        type = 'media'
        category_name = 'Media'
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.mediadescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }

    __original_file = None

    def __init__(self, *args, **kwargs):
        super(Media, self).__init__(*args, **kwargs)
        self.__original_file = self.mediafile

    def save(self, *args, **kwargs):
        import os
        # Detect if mediafile field changed
        if self.mediafile != self.__original_file:
            if self.medialink:
                # remove the old media file
                os.remove(self.medialink)
            if self.mediafile:
                # change medialink to track current media file
                self.medialink = self.mediafile.path
            else:
                self.medialink = None
        super(Media, self).save(*args, **kwargs)


class MediaCitationEvents(Queryable):
    mediaid = models.ForeignKey(Media, db_column='MediaID', primary_key=False, verbose_name='media')
    citationid = models.ForeignKey(Citations, db_column='CitationID', verbose_name='citation')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'MediaCitationEvents'
        app_label = 'Relationships'
        verbose_name = 'Medium - Citation'
        verbose_name_plural = 'Media - Citations'
        unique_together = (('mediaid', 'citationid'),)

    def __unicode__(self):
        return unicode("%s %s" % (str(self.mediaid), str(self.citationid)))

    def __str__(self):
        return "%s %s" % (str(self.mediaid), str(self.citationid))

    def keyword_search(keyword):
        media_qs = Media.keyword_search(keyword)
        media_loi = [media.pk for media in media_qs]

        citation_qs = Citations.keyword_search(keyword)
        citation_loi = [citation.pk for citation in citation_qs]

        return MediaCitationEvents.objects.filter(
            Q(citationid__in=citation_loi) |
            Q(mediaid__in=media_loi) |
            Q(relationshipdescription__icontains=keyword)
        )

    def image(self):
        return settings.RECORD_ICONS['activity']

    def subtitle(self):
        return self.relationshipdescription

    def link(self):
        return '/explore/mediacitationevents/%d/' % self.pk

    def relationships(self):
        relationship_list = []
        relationship_list.append({'key':'Media','value':[self.mediaid.get_query_json()]})
        relationship_list.append({'key':'Citation','value':[self.citationid.get_query_json()]})
        return relationship_list

    def data(self):
        return [
            {'key':'media', 'value': str(self.mediaid)},
            {'key':'citation', 'value': str(self.citationid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}
        ]

    def get_response_format(self):
        type = 'Mediacitationevents'
        category_name = 'Media - Citation'
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class PlaceAltIndigenousName(models.Model):
    altindigenousnameid = models.AutoField(db_column='AltIndigenousNameID', primary_key=True)
    placeid = models.ForeignKey(Places, db_column='PlaceID', blank=True, null=True, verbose_name='place')
    altindigenousname = models.CharField(db_column='AltIndigenousName', max_length=255, blank=True, null=True, verbose_name='alternate indigenous name')

    class Meta:
        managed = MANAGED
        db_table = 'PlaceAltIndigenousName'
        verbose_name = 'Place - Indigenous Name'
        verbose_name_plural = 'Places - Indigenous Names'
        app_label = 'Relationships'

    def get_query_json(self):
        return {
            'name': str(self),
            'link': False
        }

    def __unicode__(self):
        return unicode('%s' % (self.altindigenousname))

    def __str__(self):
        return self.altindigenousname


class PlaceGISSelections(models.Model):
    placeid = models.ForeignKey(Places, db_column='PlaceID', blank=True, null=True, verbose_name='place')
    placelabel = models.CharField(db_column='PlaceLabel', max_length=255, blank=True, null=True, verbose_name='label')
    sourcefc = models.CharField(db_column='SourceFC', max_length=255, blank=True, null=True, verbose_name='source fc')

    class Meta:
        managed = MANAGED
        db_table = 'PlaceGISSelections'
        app_label = 'Relationships'
        verbose_name_plural = 'Place GIS Selections'

    def __unicode__(self):
        return unicode('%s' % (self.placelabel))

    def __str__(self):
        return self.placelabel


class PlacesMediaEvents(Queryable):
    placeid = models.ForeignKey(Places, db_column='PlaceID', primary_key=False, verbose_name='place')
    mediaid = models.ForeignKey(Media, db_column='MediaID', verbose_name='media')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'PlacesMediaEvents'
        verbose_name = 'Place - Medium'
        app_label = 'Relationships'
        verbose_name_plural = 'Places - Media'
        unique_together = (('placeid', 'mediaid'),)

    def __unicode__(self):
        return unicode("%s %s" % (str(self.placeid), str(self.mediaid)))

    def __str__(self):
        return "%s %s" % (str(self.placeid), str(self.mediaid))

    def keyword_search(keyword):
        place_qs = Places.keyword_search(keyword)
        place_loi = [place.pk for place in place_qs]

        media_qs = Media.keyword_search(keyword)
        media_loi = [media.pk for media in media_qs]

        return PlacesMediaEvents.objects.filter(
            Q(placeid__in=place_loi) |
            Q(mediaid__in=media_loi) |
            Q(relationshipdescription__icontains=keyword)
        )

    def image(self):
        return settings.RECORD_ICONS['activity']

    def subtitle(self):
        return self.relationshipdescription

    def link(self):
        return '/explore/placesmediaevents/%s' % self.pk

    def relationships(self):
        relationship_list = []
        relationship_list.append({'key':'Place', 'value':[self.placeid.get_query_json()]})
        relationship_list.append({'key':'Media', 'value':[self.mediaid.get_query_json()]})
        return relationship_list

    def data(self):
        return [
            {'key':'place', 'value': str(self.placeid)},
            {'key':'media', 'value': str(self.mediaid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}
        ]

    def get_response_format(self):
        type = 'Placesmediaevents'
        category_name = "Place - Media"
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class PlacesResourceCitationEvents(Queryable):
    placeresourceid = models.ForeignKey(PlacesResourceEvents, db_column='PlaceResourceID', primary_key=False, verbose_name='place resource')
    citationid = models.ForeignKey(Citations, db_column='CitationID', verbose_name='citation')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'PlacesResourceCitationEvents'
        unique_together = (('placeresourceid', 'citationid'),)
        app_label = 'Relationships'
        verbose_name_plural = 'Place-Resources - Citations'

    def __unicode__(self):
        return unicode("%s %s" % (str(self.placeresourceid), str(self.citationid)))

    def __str__(self):
        return "%s %s" % (str(self.placeresourceid), str(self.citationid))

    def keyword_search(keyword):
        placeresource_qs = PlacesResourceEvents.keyword_search(keyword)
        placeresource_loi = [placeresource.pk for placeresource in placeresource_qs]

        citation_qs = Citations.keyword_search(keyword)
        citation_loi = [citation.pk for citation in citation_qs]

        return PlacesResourceCitationEvents.objects.filter(
            Q(citationid__in=citation_loi) |
            Q(placeresourceid__in=placeresource_loi) |
            Q(relationshipdescription__icontains=keyword)
        )

    def image(self):
        return settings.RECORD_ICONS['activity']

    def subtitle(self):
        return self.relationshipdescription

    def link(self):
        return '/explore/placesresourcecitationevents/%d/' % self.pk

    def relationships(self):
        relationship_list = []
        relationship_list.append({'key':'Place-Resource', 'value':[self.placeresourceid.get_query_json()]})
        relationship_list.append({'key':'Citation', 'value':[self.citationid.get_query_json()]})
        return relationship_list

    def data(self):
        return [
            {'key':'place', 'value': str(self.placeresourceid.placeid)},
            {'key':'resource', 'value': str(self.placeresourceid.resourceid)},
            {'key':'citation', 'value': str(self.citationid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}
        ]

    def get_response_format(self):
        type = 'Placesresourcecitationevents'
        category_name = 'Place/Resource - Citation'
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class PlacesResourceMediaEvents(Queryable):
    placeresourceid = models.ForeignKey(PlacesResourceEvents, db_column='PlaceResourceID', primary_key=False, verbose_name='place - resource')
    mediaid = models.ForeignKey(Media, db_column='MediaID', verbose_name='media')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'PlacesResourceMediaEvents'
        unique_together = (('placeresourceid', 'mediaid'),)
        app_label = "Relationships"
        verbose_name_plural = "Place-Resources - Media"

    def __unicode__(self):
        return unicode("%s %s" % (str(self.placeresourceid), str(self.mediaid)))

    def __str__(self):
        return "%s %s" % (str(self.placeresourceid), str(self.mediaid))

    def keyword_search(keyword):
        placeresource_qs = PlacesResourceEvents.keyword_search(keyword)
        placeresource_loi = [placeresource.pk for placeresource in placeresource_qs]

        media_qs = Media.keyword_search(keyword)
        media_loi = [media.pk for media in media_qs]

        return PlacesResourceMediaEvents.objects.filter(
            Q(placeresourceid__in=placeresource_loi) |
            Q(mediaid__in=media_loi) |
            Q(relationshipdescription__icontains=keyword)
        )

    def image(self):
        return settings.RECORD_ICONS['activity']

    def subtitle(self):
        return self.relationshipdescription

    def link(self):
        return '/explore/placesresourcemediaevents/%d/' % self.pk

    def relationships(self):
        relationship_list = []
        relationship_list.append({'key':'Place-Resource', 'value':[self.placeresourceid.get_query_json()]})
        relationship_list.append({'key':'Media', 'value':[self.mediaid.get_query_json()]})
        return relationship_list

    def data(self):
        return [
            {'key':'place', 'value': str(self.placeresourceid.placeid)},
            {'key':'resource', 'value': str(self.placeresourceid.resourceid)},
            {'key':'media', 'value': str(self.mediaid)},
            {'key':'relationship description', 'value': self.relationshipdescription}
        ]

    def get_response_format(self):
        type = 'Placesresourcemediaevents'
        category_name = "Place/Resource - Media"
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class ResourceActivityCitationEvents(Queryable):
    resourceactivityid = models.ForeignKey(ResourcesActivityEvents, db_column='ResourceActivityID', primary_key=False, verbose_name='resource activity')
    citationid = models.ForeignKey(Citations, db_column='CitationID', verbose_name='citation')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'ResourceActivityCitationEvents'
        unique_together = (('resourceactivityid', 'citationid'),)
        app_label = 'Relationships'
        verbose_name_plural = 'Activity - Citations'

    def __unicode__(self):
        return unicode("%s %s" % (str(self.resourceactivityid), str(self.citationid)))

    def __str__(self):
        return "%s %s" % (str(self.resourceactivityid), str(self.citationid))

    def keyword_search(keyword):
        resourceactivity_qs = ResourcesActivityEvents.keyword_search(keyword)
        resourceactivity_loi = [resourceactivity.pk for resourceactivity in resourceactivity_qs]

        citation_qs = Citations.keyword_search(keyword)
        citation_loi = [citation.pk for citation in citation_qs]

        return ResourceActivityCitationEvents.objects.filter(
            Q(citationid__in=citation_loi) |
            Q(resourceactivityid__in=resourceactivity_loi) |
            Q(relationshipdescription__icontains=keyword)
        )

    def image(self):
        return settings.RECORD_ICONS['activity']

    def subtitle(self):
        return self.relationshipdescription

    def link(self):
        return '/explore/resourceactivitycitationevents/%d/' % self.pk

    def relationships(self):
        relationship_list = []
        relationship_list.append({'key':'Activity', 'value':[self.resourceactivityid.get_query_json()]})
        relationship_list.append({'key':'Citation', 'value':[self.citationid.get_query_json()]})
        return relationship_list

    def data(self):
        return [
            {'key':'resource activity', 'value': str(self.resourceactivityid)},
            {'key':'citation', 'value': str(self.citationid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}

        ]

    def get_response_format(self):
        type = 'Resourceactivitycitationevents'
        category_name = 'Activity - Citation'
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class ResourceActivityMediaEvents(Queryable):
    resourceactivityid = models.ForeignKey(ResourcesActivityEvents, db_column='ResourceActivityID', primary_key=False, verbose_name='resource activity')
    mediaid = models.ForeignKey(Media, db_column='MediaID', verbose_name='media')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'ResourceActivityMediaEvents'
        unique_together = (('resourceactivityid', 'mediaid'),)
        app_label = 'Relationships'
        verbose_name_plural = 'Activity - Media'

    def __unicode__(self):
        return unicode("%s %s" % (str(self.resourceactivityid), str(self.mediaid)))

    def __str__(self):
        return "%s %s" % (str(self.resourceactivityid), str(self.mediaid))

    def keyword_search(keyword):
        resourceactivity_qs = ResourcesActivityEvents.keyword_search(keyword)
        resourceactivity_loi = [resourceactivity.pk for resourceactivity in resourceactivity_qs]

        media_qs = Media.keyword_search(keyword)
        media_loi = [media.pk for media in media_qs]

        return ResourceActivityMediaEvents.objects.filter(
            Q(resourceactivityid__in=resourceactivity_loi) |
            Q(mediaid__in=media_loi) |
            Q(relationshipdescription__icontains=keyword)
        )

    def name(self):
        return 'resource activity media'

    def image(self):
        return settings.RECORD_ICONS['activity']

    def subtitle(self):
        return self.relationshipdescription

    def link(self):
        return '/explore/resourceactivitymediaevents/%d/' % self.pk

    def relationships(self):
        relationship_list = []
        relationship_list.append({'key':'Activity', 'value':[self.resourceactivityid.get_query_json()]})
        relationship_list.append({'key':'Media', 'value':[self.mediaid.get_query_json()]})
        return relationship_list

    def data(self):
        return [
            {'key':'resource activity', 'value': str(self.resourceactivityid)},
            {'key':'media', 'value': str(self.mediaid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}
        ]

    def get_response_format(self):
        type = 'Resourceactivitymediaevents'
        category_name = 'Activity - Media'
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class ResourceAltIndigenousName(models.Model):
    altindigenousnameid = models.AutoField(db_column='AltIndigenousNameID', primary_key=True)
    resourceid = models.ForeignKey(Resources, db_column='ResourceID', blank=True, null=True, verbose_name='resource')
    altindigenousname = models.CharField(db_column='AltIndigenousName', max_length=255, blank=True, null=True, verbose_name='alt indigenous name')

    class Meta:
        managed = MANAGED
        db_table = 'ResourceAltIndigenousName'
        app_label = 'Relationships'
        verbose_name_plural = 'Resource Alternative Indigenous Names'

    def __unicode__(self):
        return unicode('%s' % (self.altindigenousname))

    def __str__(self):
        return self.altindigenousname


class ResourceResourceEvents(Queryable):
    resourceid = models.ForeignKey(Resources, db_column='ResourceID', primary_key=False, related_name="resource_a")
    altresourceid = models.ForeignKey(Resources, db_column='AltResourceID', related_name="resource_b")
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')

    class Meta:
        managed = MANAGED
        db_table = 'ResourceResourceEvents'
        unique_together = (('resourceid', 'altresourceid'),)
        app_label = 'Relationships'
        verbose_name_plural = 'Resources - Resources'

    def __unicode__(self):
        return unicode("%s %s" % (str(self.resourceid), str(self.altresourceid)))

    def __str__(self):
        return "%s %s" % (str(self.resourceid), str(self.altresourceid))

    def keyword_search(keyword):
        resource_qs = Resources.keyword_search(keyword)
        resource_loi = [resource.pk for resource in resource_qs]

        return ResourceResourceEvents.objects.filter(
            Q(resourceid__in=resource_loi) |
            Q(altresourceid__in=resource_loi) |
            Q(relationshipdescription__icontains=keyword)
        )

    def image(self):
        return settings.RECORD_ICONS['activity']

    def subtitle(self):
        return self.relationshipdescription

    def link(self):
        return '/explore/resourceresourceevents/%d/' % self.pk

    def relationships(self):
        relationship_list = []
        relationship_list.append({'key':'Resource', 'value':[self.resourceid.get_query_json()]})
        relationship_list.append({'key':'Alternate Resource', 'value':[self.altresourceid.get_query_json()]})
        return relationship_list

    def data(self):
        return [
            {'key':'resource a', 'value': str(self.resourceid)},
            {'key':'resource b', 'value': str(self.altresourceid)},
            {'key':'relationship description', 'value': self.relationshipdescription}
        ]

    def get_response_format(self):
        type = 'Resourceresourceevents'
        category_name = "Resource - Resource"
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }

    # Need to create two-sided pairs for these relationships to show up correctly in the admin - this could fuzz-up the querying, though
    def save(self, *args, **kwargs):
        super(ResourceResourceEvents, self).save(*args, **kwargs)
        relatedResources = ResourceResourceEvents.objects.filter(resourceid=self.altresourceid, altresourceid=self.resourceid)
        if len(relatedResources) == 1:
            relatedResources[0].relationshipdescription=self.relationshipdescription
            super(ResourceResourceEvents, relatedResources[0]).save()
        else:
            ResourceResourceEvents.objects.create(resourceid=self.altresourceid, altresourceid=self.resourceid, relationshipdescription=self.relationshipdescription)

    def delete(self, *args, **kwargs):
        super(ResourceResourceEvents, self).delete(*args, **kwargs)
        try:
            pair = ResourceResourceEvents.objects.get(resourceid=self.altresourceid, altresourceid=self.resourceid)
            pair.delete()
        except Exception as e:
            pass

class ResourcesCitationEvents(Queryable):
    resourceid = models.ForeignKey(Resources, db_column='ResourceID', primary_key=False, verbose_name='resource')
    citationid = models.ForeignKey(Citations, db_column='CitationID', verbose_name='citation')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'ResourcesCitationEvents'
        verbose_name = 'Resource - Citation'
        verbose_name_plural = 'Resources - Citations'
        unique_together = (('resourceid', 'citationid'),)
        app_label = 'Relationships'

    def __unicode__(self):
        return unicode("%s %s" % (str(self.resourceid), str(self.citationid)))

    def __str__(self):
        return "%s %s" % (str(self.resourceid), str(self.citationid))

    def keyword_search(keyword):
        resource_qs = Resources.keyword_search(keyword)
        resource_loi = [resource.pk for resource in resource_qs]

        citation_qs = Citations.keyword_search(keyword)
        citation_loi = [citation.pk for citation in citation_qs]

        return ResourcesCitationEvents.objects.filter(
            Q(citationid__in=citation_loi) |
            Q(resourceid__in=resource_loi) |
            Q(relationshipdescription__icontains=keyword)
        )

    def image(self):
        return settings.RECORD_ICONS['activity']

    def subtitle(self):
        return self.relationshipdescription

    def link(self):
        return '/explore/resourcescitationevents/%d/' % self.pk

    def relationships(self):
        relationship_list = []
        relationship_list.append({'key':'Resource', 'value':[self.resourceid.get_query_json()]})
        relationship_list.append({'key':'Citation', 'value':[self.citationid.get_query_json()]})
        return relationship_list

    def data(self):
        return [
            {'key':'resource', 'value': str(self.resourceid)},
            {'key':'citation', 'value': str(self.citationid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}
        ]

    def get_response_format(self):
        type = 'Resourcescitationevents'
        category_name = "Resource - Citation"
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class ResourcesMediaEvents(Queryable):
    resourceid = models.ForeignKey(Resources, db_column='ResourceID', primary_key=False, verbose_name='resource')
    mediaid = models.ForeignKey(Media, db_column='MediaID', verbose_name='media')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'ResourcesMediaEvents'
        verbose_name = 'Resource - Medium'
        verbose_name_plural = 'Resources - Media'
        unique_together = (('resourceid', 'mediaid'),)
        app_label = 'Relationships'

    def __unicode__(self):
        return unicode("%s %s" % (str(self.resourceid), str(self.mediaid)))

    def __str__(self):
        return "%s %s" % (str(self.resourceid), str(self.mediaid))

    def keyword_search(keyword):
        resource_qs = Resources.keyword_search(keyword)
        resource_loi = [resource.pk for resource in resource_qs]

        media_qs = Media.keyword_search(keyword)
        media_loi = [media.pk for media in media_qs]

        return ResourcesMediaEvents.objects.filter(
            Q(mediaid__in=media_loi) |
            Q(resourceid__in=resource_loi) |
            Q(relationshipdescription__icontains=keyword)
        )

    def image(self):
        return settings.RECORD_ICONS['activity']

    def subtitle(self):
        return self.relationshipdescription

    def link(self):
        return '/explore/resourcesmediaevents/%d/' % self.pk

    def relationships(self):
        relationship_list = []
        relationship_list.append({'key':'Resource', 'value':[self.resourceid.get_query_json()]})
        relationship_list.append({'key':'Media', 'value':[self.mediaid.get_query_json()]})
        return relationship_list

    def data(self):
        return [
            {'key':'resource', 'value': str(self.resourceid)},
            {'key':'media', 'value': str(self.mediaid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}
        ]

    def get_response_format(self):
        type = 'Resourcesmediaevents'
        category_name = "Resource - Media"
        return {
            'id': self.pk,
            'type': type,
            'category_name': category_name,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }

from django.contrib.auth.models import Group

class UserAccess(models.Model):
    group = models.OneToOneField(Group)
    accessid = models.AutoField(db_column='AccessID', primary_key=True)
    accesslevel = models.CharField(db_column='AccessLevel', max_length=255, blank=True, null=True, verbose_name='access level')

    class Meta:
        managed = MANAGED
        db_table = 'UserAccess'
        app_label = 'Accounts'
        verbose_name = 'user access'
        verbose_name_plural = 'user access'

    def __unicode__(self):
        return unicode('%s' % (self.accesslevel))

    def __str__(self):
        return self.accesslevel


class Users(AbstractUser):
    userid = models.AutoField(db_column='UserID', primary_key=True)
    username = models.CharField(db_column='UserName', max_length=20, verbose_name='username', unique=True)
    password = models.CharField(_('password'), max_length=128, db_column='Password')
    first_name = models.CharField(db_column='FirstName', max_length=255, verbose_name='first name')
    last_name = models.CharField(db_column='LastName', max_length=255, verbose_name='last name')
    affiliation = models.CharField(db_column='Affiliation', max_length=255)
    title = models.CharField(db_column='Title', max_length=255)
    accesslevel = models.ForeignKey(UserAccess, db_column='AccessLevel', verbose_name='access level', null=True, blank=True)
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    email = models.EmailField(_('email address'), blank=True, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    class Meta:
        managed = MANAGED
        db_table = 'Users'
        app_label = 'Accounts'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __unicode__(self):
        return unicode('%s' % (self.username))

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.userid:
            super(Users, self).save(*args, **kwargs)

        if self.accesslevel:
            self.groups.set([self.accesslevel.group])
        else:
            self.groups.set([])
        if self.accesslevel and len(self.accesslevel.group.permissions.all()) > 0:
            self.is_staff = True
        else:
            self.is_staff = False
        if self.accesslevel and self.accesslevel.accesslevel == 'Administrator':
            self.is_superuser = True
        else:
            self.is_superuser = False
        super(Users, self).save(*args, **kwargs)
