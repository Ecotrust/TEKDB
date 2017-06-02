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

    def get_query_json(self):
        return {
            'name': str(self),
            'image': self.image(),
            'subtitle': self.subtitle(),
            'data': self.data(),
            'enteredbyname': self.enteredbyname,
            'enteredbydate': self.enteredbydate,
            'modifiedbyname': self.modifiedbyname,
            'modifiedbydate': self.modifiedbydate,
        }

    def save(self, *args, **kwargs):
        #TODO: set entered/modified by info now
        super(Queryable, self).save(*args, **kwargs)


class LookupPlanningUnit(models.Model):
    planningunitid = models.IntegerField(db_column='PlanningUnitID', primary_key=True)
    planningunitname = models.CharField(db_column='PlanningUnitName', max_length=100, blank=True, null=True, verbose_name='planning unit')

    class Meta:
        managed = MANAGED
        db_table = 'LookupPlanningUnit'

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
        return {
            'id': self.pk,
            'type': type,
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

    def __unicode__(self):
        return unicode('%s' % (self.habitat))

    def __str__(self):
        return self.habitat


class Places(Queryable):
    placeid = models.AutoField(db_column='PlaceID', primary_key=True)
    indigenousplacename = models.CharField(db_column='IndigenousPlaceName', max_length=255, blank=True, null=True, verbose_name='indigenous name')
    indigenousplacenamemeaning = models.CharField(db_column='IndigenousPlaceNameMeaning', max_length=255, blank=True, null=True, verbose_name='english translation')
    englishplacename = models.CharField(db_column='EnglishPlaceName', max_length=255, blank=True, null=True, verbose_name='english name')
    planningunitid = models.ForeignKey(LookupPlanningUnit, db_column='PlanningUnitID', blank=True, null=True, verbose_name='planning unit')
    primaryhabitat = models.ForeignKey(LookupHabitat, db_column='PrimaryHabitat', max_length=100, blank=True, null=True, verbose_name='primary habitat')
    tribeid = models.ForeignKey(LookupTribe, db_column='TribeID', blank=True, null=True, verbose_name='tribe')
    islocked = models.BooleanField(db_column='IsLocked', default=False, verbose_name='locked?')

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
        return '/static/explore/img/demo-map.png'

    def subtitle(self):
        return self.indigenousplacenamemeaning

    def data(self):
        return [
            {'key':'english place name', 'value': self.englishplacename},
            {'key':'indigenous place name', 'value': self.indigenousplacename},
            {'key':'indigenous place name meaning', 'value': self.indigenousplacenamemeaning},
            {'key':'planning unit', 'value': str(self.planningunitid)},
            {'key':'primary habitat', 'value': str(self.primaryhabitat)},
            {'key':'tribe', 'value': str(self.tribeid)}
        ]

    def get_response_format(self):
        type = 'places'
        return {
            'id': self.pk,
            'type': type,
            'name': str(self),
            'image': self.image(),
            'description': self.indigenousplacenamemeaning,
            'link': '/explore/%s/%d' % (type, self.pk)
        }

    def __unicode__(self):
        return unicode('%s' % (self.englishplacename))

    def __str__(self):
        return self.englishplacename


class LookupResourceGroup(models.Model):
    resourceclassificationgroup = models.CharField(db_column='ResourceClassificationGroup', primary_key=True, max_length=255, verbose_name='broad species group')

    class Meta:
        managed = MANAGED
        db_table = 'LookupResourceGroup'

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
        return '/static/explore/img/demo-resource.png'

    def subtitle(self):
        return self.species

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
        return {
            'id': self.pk,
            'type': type,
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

    def __unicode__(self):
        return unicode('%s' % (self.partused))

    def __str__(self):
        return self.partused


class LookupCustomaryUse(models.Model):
    usedfor = models.CharField(db_column='UsedFor', primary_key=True, max_length=255, verbose_name='used_for')

    class Meta:
        managed = MANAGED
        db_table = 'LookupCustomaryUse'

    def __unicode__(self):
        return unicode('%s' % (self.usedfor))

    def __str__(self):
        return self.usedfor


class LookupSeason(models.Model):
    season = models.CharField(db_column='Season', primary_key=True, max_length=255)

    class Meta:
        managed = MANAGED
        db_table = 'LookupSeason'

    def __unicode__(self):
        return unicode('%s' % (self.season))

    def __str__(self):
        return self.season


class LookupTiming(models.Model):
    timing = models.CharField(db_column='Timing', primary_key=True, max_length=255)

    class Meta:
        managed = MANAGED
        db_table = 'LookupTiming'

    def __unicode__(self):
        return unicode('%s' % (self.timing))

    def __str__(self):
        return self.timing


class PlacesResourceEvents(Queryable):
    placeresourceid = models.AutoField(db_column='PlaceResourceID', primary_key=True)
    placeid = models.ForeignKey(Places, models.DO_NOTHING, db_column='PlaceID', verbose_name='place')
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
        return unicode("%s %s" % (str(self.placeid), str(self.resourceid)))

    def __str__(self):
        return "%s %s" % (str(self.placeid), str(self.resourceid))

    def image(self):
        return '/static/explore/img/demo-activity.png'

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

    def get_response_format(self):
        type = 'Placesresourceevents'
        return {
            'id': self.pk,
            'type': type,
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

    def __unicode__(self):
        return unicode('%s' % (self.participants))

    def __str__(self):
        return self.participants


class LookupTechniques(models.Model):
    techniques = models.CharField(db_column='Techniques', primary_key=True, max_length=255)

    class Meta:
        managed = MANAGED
        db_table = 'LookupTechniques'

    def __unicode__(self):
        return unicode('%s' % (self.techniques))

    def __str__(self):
        return self.techniques


class LookupActivity(models.Model):
    activity = models.CharField(db_column='Activity', primary_key=True, max_length=255)

    class Meta:
        managed = MANAGED
        db_table = 'LookupActivity'

    def __unicode__(self):
        return unicode('%s' % (self.activity))

    def __str__(self):
        return self.activity


class ResourcesActivityEvents(Queryable):
    resourceactivityid = models.AutoField(db_column='ResourceActivityID', primary_key=True)
    placeresourceid = models.ForeignKey(PlacesResourceEvents, models.DO_NOTHING, db_column='PlaceResourceID', verbose_name='place resource')
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

    def __unicode__(self):
        return unicode("%s %s" % (str(self.placeresourceid), self.activityshortdescription))

    def __str__(self):
        return "%s %s" % (str(self.placeresourceid), self.activityshortdescription)

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
        return '/static/explore/img/demo-activity.png'

    def subtitle(self):
        return self.relationshipdescription

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
        return {
            'id': self.pk,
            'type': type,
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


class LookupReferenceType(models.Model):
    documenttype = models.CharField(db_column='DocumentType', primary_key=True, max_length=25, verbose_name='document type')

    class Meta:
        managed = MANAGED
        db_table = 'LookupReferenceType'

    def __unicode__(self):
        return unicode('%s' % (self.documenttype))

    def __str__(self):
        return self.documenttype


class LookupAuthorType(models.Model):
    authortype = models.CharField(db_column='AuthorType', primary_key=True, max_length=50, verbose_name='author type')

    class Meta:
        managed = MANAGED
        db_table = 'LookupAuthorType'

    def __unicode__(self):
        return unicode('%s' % (self.authortype))

    def __str__(self):
        return self.authortype


class Citations(Queryable):
    citationid = models.AutoField(db_column='CitationID', primary_key=True)
    referencetype = models.ForeignKey(LookupReferenceType, db_column='ReferenceType', max_length=255, verbose_name='reference type')
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
        return '/static/explore/img/demo-citation.png'

    def subtitle(self):
        return self.referencetext

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
        return {
            'id': self.pk,
            'type': type,
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
            return '[%s] %s (%d)' % (str(self.referencetype), interviewee, self.year)
        else:
            return '[%s] %s (%d)' % (str(self.referencetype), self.title, self.year)

    def __unicode__(self):
        return unicode('%s' % (str(self)))


class PlacesCitationEvents(Queryable):
    placeid = models.ForeignKey(Places, models.DO_NOTHING, db_column='PlaceID', primary_key=True, verbose_name='place')
    citationid = models.ForeignKey(Citations, db_column='CitationID', verbose_name='citation')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'PlacesCitationEvents'
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
        return '/static/explore/img/demo-activity.png'

    def subtitle(self):
        return self.relationshipdescription

    def data(self):
        return [
            {'key':'place', 'value': str(self.placeid)},
            {'key':'citation', 'value': str(self.citationid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}
        ]

    def get_response_format(self):
        type = 'Placescitationevents'
        return {
            'id': self.pk,
            'type': type,
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

    def __unicode__(self):
        return unicode("Back: %d, Front:%d" % (self.backendversion, self.frontendversion))

    def __str__(self):
        return "Back: %d, Front:%d" % (self.backendversion, self.frontendversion)


class LookupLocalityType(models.Model):
    localitytype = models.CharField(db_column='LocalityType', primary_key=True, max_length=255, verbose_name='locality type')

    class Meta:
        managed = MANAGED
        db_table = 'LookupLocalityType'

    def __unicode__(self):
        return unicode('%s' % (self.localitytype))

    def __str__(self):
        return self.localitytype


class Locality(models.Model):
    localityid = models.AutoField(db_column='LocalityID', primary_key=True)
    placeid = models.ForeignKey(Places, models.DO_NOTHING, db_column='PlaceID', blank=True, null=True, verbose_name='place')
    englishname = models.CharField(db_column='EnglishName', max_length=255, blank=True, null=True, verbose_name='english name')
    indigenousname = models.CharField(db_column='IndigenousName', max_length=255, blank=True, null=True, verbose_name='indigenous name')
    localitytype = models.ForeignKey(LookupLocalityType, db_column='LocalityType', max_length=255, blank=True, null=True, verbose_name='type')

    class Meta:
        managed = MANAGED
        db_table = 'Locality'
        verbose_name = 'Locality'
        verbose_name_plural = 'Localities'

    def __unicode__(self):
        return unicode('%s' % (self.englishname))

    def __str__(self):
        return self.englishname

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
        return '/static/explore/img/demo-map.png'

    def subtitle(self):
        return self.indigenousname

    def data(self):
        return [
            {'key':'english name', 'value': self.englishname},
            {'key':'indigenous name', 'value': self.indigenousname},
            {'key':'place', 'value': str(self.placeid)},
            {'key':'locality type', 'value': str(self.localitytype)}
        ]

    def get_response_format(self):
        type = 'locality'
        return {
            'id': self.pk,
            'type': type,
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

    def __unicode__(self):
        return unicode('%s' % (self.localitylabel))

    def __str__(self):
        return self.localitylabel


class LocalityPlaceResourceEvent(Queryable):
    placeresourceid = models.ForeignKey(PlacesResourceEvents, models.DO_NOTHING, db_column='PlaceResourceID', primary_key=True, verbose_name='place resource')
    localityid = models.ForeignKey(Locality, models.DO_NOTHING, db_column='LocalityID', verbose_name='locality')

    class Meta:
        managed = MANAGED
        db_table = 'LocalityPlaceResourceEvent'
        unique_together = (('placeresourceid', 'localityid'),)

    def __unicode__(self):
        return unicode("%s - %s" % (str(self.localityid), str(self.placeresoureid)))

    def __str__(self):
        return "%s - %s" % (str(self.localityid), str(self.placeresoureid))

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
        return '/static/explore/img/demo-activity.png'

    def subtitle(self):
        return ''

    def data(self):
        return [
            {'key':'place', 'value': str(self.placeresourceid.placeid)},
            {'key':'resource', 'value': str(self.placeresourceid.resourceid)},
            {'key':'locality', 'value': str(self.localityid)}
        ]

    def get_response_format(self):
        type = 'Placescitationevents'
        return {
            'id': self.pk,
            'type': type,
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

    def __unicode__(self):
        return unicode('%s' % (self.username))

    def __str__(self):
        return self.username


class Media(Queryable):
    mediaid = models.AutoField(db_column='MediaID', primary_key=True)
    mediatype = models.ForeignKey(LookupMediaType, db_column='MediaType', max_length=255, blank=True, null=True, verbose_name='type')
    medianame = models.CharField(db_column='MediaName', max_length=255, blank=True, null=True, verbose_name='name')
    mediadescription = models.TextField(db_column='MediaDescription', blank=True, null=True, verbose_name='description')
    medialink = models.CharField(db_column='MediaLink', max_length=255, blank=True, null=True, verbose_name='link')

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
        return '/static/explore/img/demo-media.png'

    def subtitle(self):
        return self.mediatype

    def data(self):
        return [
            {'key':'name', 'value': self.medianame},
            {'key':'media type', 'value': str(self.mediatype)},
            {'key':'media description', 'value': self.mediadescription},
            {'key':'link', 'value': self.medialink}
        ]

    def get_response_format(self):
        type = 'media'
        return {
            'id': self.pk,
            'type': type,
            'name': str(self),
            'image': self.image(),
            'description': self.mediadescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class MediaCitationEvents(Queryable):
    mediaid = models.ForeignKey(Media, models.DO_NOTHING, db_column='MediaID', primary_key=True, verbose_name='media')
    citationid = models.ForeignKey(Citations, models.DO_NOTHING, db_column='CitationID', verbose_name='citation')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'MediaCitationEvents'
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
        return '/static/explore/img/demo-activity.png'

    def subtitle(self):
        return self.relationshipdescription

    def data(self):
        return [
            {'key':'media', 'value': str(self.mediaid)},
            {'key':'citation', 'value': str(self.citationid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}
        ]

    def get_response_format(self):
        type = 'Mediacitationevents'
        return {
            'id': self.pk,
            'type': type,
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

    def __unicode__(self):
        return unicode('%s' % (self.placelabel))

    def __str__(self):
        return self.placelabel


class PlacesMediaEvents(Queryable):
    placeid = models.ForeignKey(Places, models.DO_NOTHING, db_column='PlaceID', primary_key=True, verbose_name='place')
    mediaid = models.ForeignKey(Media, models.DO_NOTHING, db_column='MediaID', verbose_name='media')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'PlacesMediaEvents'
        verbose_name = 'Place - Medium'
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
        return '/static/explore/img/demo-activity.png'

    def subtitle(self):
        return self.relationshipdescription

    def data(self):
        return [
            {'key':'place', 'value': str(self.placeid)},
            {'key':'media', 'value': str(self.mediaid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}
        ]

    def get_response_format(self):
        type = 'Placesmediaevents'
        return {
            'id': self.pk,
            'type': type,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class PlacesResourceCitationEvents(Queryable):
    placeresourceid = models.ForeignKey(PlacesResourceEvents, models.DO_NOTHING, db_column='PlaceResourceID', primary_key=True, verbose_name='place resource')
    citationid = models.ForeignKey(Citations, db_column='CitationID', verbose_name='citation')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'PlacesResourceCitationEvents'
        unique_together = (('placeresourceid', 'citationid'),)

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
        return '/static/explore/img/demo-activity.png'

    def subtitle(self):
        return self.relationshipdescription

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
        return {
            'id': self.pk,
            'type': type,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class PlacesResourceMediaEvents(Queryable):
    placeresourceid = models.ForeignKey(PlacesResourceEvents, models.DO_NOTHING, db_column='PlaceResourceID', primary_key=True, verbose_name='place - resource')
    mediaid = models.ForeignKey(Media, db_column='MediaID', verbose_name='media')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'PlacesResourceMediaEvents'
        unique_together = (('placeresourceid', 'mediaid'),)

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
        return '/static/explore/img/demo-activity.png'

    def subtitle(self):
        return self.relationshipdescription

    def data(self):
        return [
            {'key':'place', 'value': str(self.placeresourceid.placeid)},
            {'key':'resource', 'value': str(self.placeresourceid.resourceid)},
            {'key':'media', 'value': str(self.mediaid)},
            {'key':'relationship description', 'value': self.relationshipdescription}
        ]

    def get_response_format(self):
        type = 'Placesresourcemediaevents'
        return {
            'id': self.pk,
            'type': type,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class ResourceActivityCitationEvents(Queryable):
    resourceactivityid = models.ForeignKey(ResourcesActivityEvents, models.DO_NOTHING, db_column='ResourceActivityID', primary_key=True, verbose_name='resource activity')
    citationid = models.ForeignKey(Citations, db_column='CitationID', verbose_name='citation')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'ResourceActivityCitationEvents'
        unique_together = (('resourceactivityid', 'citationid'),)

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
        return '/static/explore/img/demo-activity.png'

    def subtitle(self):
        return self.relationshipdescription

    def data(self):
        return [
            {'key':'resource activity', 'value': str(self.resourceactivityid)},
            {'key':'citation', 'value': str(self.citationid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}

        ]

    def get_response_format(self):
        type = 'Resourceactivitycitationevents'
        return {
            'id': self.pk,
            'type': type,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class ResourceActivityMediaEvents(Queryable):
    resourceactivityid = models.ForeignKey(ResourcesActivityEvents, models.DO_NOTHING, db_column='ResourceActivityID', primary_key=True, verbose_name='resource activity')
    mediaid = models.ForeignKey(Media, db_column='MediaID', verbose_name='media')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'ResourceActivityMediaEvents'
        unique_together = (('resourceactivityid', 'mediaid'),)

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
        return '/static/explore/img/demo-activity.png'

    def subtitle(self):
        return self.relationshipdescription

    def data(self):
        return [
            {'key':'resource activity', 'value': str(self.resourceactivityid)},
            {'key':'media', 'value': str(self.mediaid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}
        ]

    def get_response_format(self):
        type = 'Resourceactivitymediaevents'
        return {
            'id': self.pk,
            'type': type,
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

    def __unicode__(self):
        return unicode('%s' % (self.altindigenousname))

    def __str__(self):
        return self.altindigenousname


class ResourceResourceEvents(Queryable):
    resourceid = models.ForeignKey(Resources, db_column='ResourceID', primary_key=True, related_name="resource_a")
    altresourceid = models.ForeignKey(Resources, db_column='AltResourceID', related_name="resource_b")
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')

    class Meta:
        managed = MANAGED
        db_table = 'ResourceResourceEvents'
        unique_together = (('resourceid', 'altresourceid'),)

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
        return '/static/explore/img/demo-activity.png'

    def subtitle(self):
        return self.relationshipdescription

    def data(self):
        return [
            {'key':'resource a', 'value': str(self.resourceid)},
            {'key':'resource b', 'value': str(self.altresourceid)},
            {'key':'relationship description', 'value': self.relationshipdescription}
        ]

    def get_response_format(self):
        type = 'Resourceresourceevents'
        return {
            'id': self.pk,
            'type': type,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class ResourcesCitationEvents(Queryable):
    resourceid = models.ForeignKey(Resources, models.DO_NOTHING, db_column='ResourceID', primary_key=True, verbose_name='resource')
    citationid = models.ForeignKey(Citations, models.DO_NOTHING, db_column='CitationID', verbose_name='citation')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'ResourcesCitationEvents'
        verbose_name = 'Resource - Citation'
        verbose_name_plural = 'Resources - Citations'
        unique_together = (('resourceid', 'citationid'),)

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
        return '/static/explore/img/demo-activity.png'

    def subtitle(self):
        return self.relationshipdescription

    def data(self):
        return [
            {'key':'resource', 'value': str(self.resourceid)},
            {'key':'citation', 'value': str(self.citationid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}
        ]

    def get_response_format(self):
        type = 'Resourcescitationevents'
        return {
            'id': self.pk,
            'type': type,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class ResourcesMediaEvents(Queryable):
    resourceid = models.ForeignKey(Resources, models.DO_NOTHING, db_column='ResourceID', primary_key=True, verbose_name='resource')
    mediaid = models.ForeignKey(Media, models.DO_NOTHING, db_column='MediaID', verbose_name='media')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'ResourcesMediaEvents'
        verbose_name = 'Resource - Medium'
        verbose_name_plural = 'Resources - Media'
        unique_together = (('resourceid', 'mediaid'),)

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
        return '/static/explore/img/demo-activity.png'

    def subtitle(self):
        return self.relationshipdescription

    def data(self):
        return [
            {'key':'resource', 'value': str(self.resourceid)},
            {'key':'media', 'value': str(self.mediaid)},
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}
        ]

    def get_response_format(self):
        type = 'Resourcesmediaevents'
        return {
            'id': self.pk,
            'type': type,
            'name': str(self),
            'image': self.image(),
            'description': self.relationshipdescription,
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class UserAccess(models.Model):
    accessid = models.AutoField(db_column='AccessID', primary_key=True)
    accesslevel = models.CharField(db_column='AccessLevel', max_length=255, blank=True, null=True, verbose_name='access level')

    class Meta:
        managed = MANAGED
        db_table = 'UserAccess'

    def __unicode__(self):
        return unicode('%s' % (self.accesslevel))

    def __str__(self):
        return self.accesslevel


class Users(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)
    username = models.CharField(db_column='UserName', max_length=20, verbose_name='username')
    password = models.CharField(db_column='Password', max_length=20)
    firstname = models.CharField(db_column='FirstName', max_length=255, verbose_name='first name')
    lastname = models.CharField(db_column='LastName', max_length=255, verbose_name='last name')
    affiliation = models.CharField(db_column='Affiliation', max_length=255)
    title = models.CharField(db_column='Title', max_length=255)
    accesslevel = models.ForeignKey(UserAccess, db_column='AccessLevel', verbose_name='access level')

    class Meta:
        managed = MANAGED
        db_table = 'Users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __unicode__(self):
        return unicode('%s' % (self.username))

    def __str__(self):
        return self.username
