# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Citations(models.Model):
    citationid = models.IntegerField(db_column='CitationID', primary_key=True)  # Field name made lowercase.
    referencetype = models.CharField(db_column='ReferenceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    referencetext = models.CharField(db_column='ReferenceText', max_length=50, blank=True, null=True)  # Field name made lowercase.
    authortype = models.CharField(db_column='AuthorType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    authorprimary = models.CharField(db_column='AuthorPrimary', max_length=255, blank=True, null=True)  # Field name made lowercase.
    authorsecondary = models.CharField(db_column='AuthorSecondary', max_length=255, blank=True, null=True)  # Field name made lowercase.
    intervieweeid = models.IntegerField(db_column='IntervieweeID', blank=True, null=True)  # Field name made lowercase.
    interviewerid = models.IntegerField(db_column='InterviewerID', blank=True, null=True)  # Field name made lowercase.
    placeofinterview = models.CharField(db_column='PlaceofInterview', max_length=255, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    seriestitle = models.CharField(db_column='SeriesTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seriesvolume = models.CharField(db_column='SeriesVolume', max_length=50, blank=True, null=True)  # Field name made lowercase.
    serieseditor = models.CharField(db_column='SeriesEditor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='Publisher', max_length=100, blank=True, null=True)  # Field name made lowercase.
    publishercity = models.CharField(db_column='PublisherCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    preparedfor = models.CharField(db_column='PreparedFor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citations'


class Currentversion(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    backendversion = models.IntegerField(db_column='BackendVersion', blank=True, null=True)  # Field name made lowercase.
    frontendversion = models.IntegerField(db_column='FrontendVersion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currentversion'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Locality(models.Model):
    localityid = models.IntegerField(db_column='LocalityID', primary_key=True)  # Field name made lowercase.
    placeid = models.IntegerField(db_column='PlaceID', blank=True, null=True)  # Field name made lowercase.
    englishname = models.CharField(db_column='EnglishName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    indigenousname = models.CharField(db_column='IndigenousName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    localitytype = models.CharField(db_column='LocalityType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'locality'


class Localitygisselections(models.Model):
    localityid = models.IntegerField(db_column='LocalityID', blank=True, null=True)  # Field name made lowercase.
    localitylabel = models.CharField(db_column='LocalityLabel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcefc = models.CharField(db_column='SourceFC', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localitygisselections'


class Localityplaceresourceevent(models.Model):
    placeresourceid = models.IntegerField(db_column='PlaceResourceID')  # Field name made lowercase.
    localityid = models.IntegerField(db_column='LocalityID')  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localityplaceresourceevent'
        unique_together = (('placeresourceid', 'localityid'),)


class Lookupactivity(models.Model):
    activity = models.CharField(db_column='Activity', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookupactivity'


class Lookupauthortype(models.Model):
    authortype = models.CharField(db_column='AuthorType', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookupauthortype'


class Lookupcustomaryuse(models.Model):
    usedfor = models.CharField(db_column='UsedFor', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookupcustomaryuse'


class Lookuphabitat(models.Model):
    habitat = models.CharField(db_column='Habitat', primary_key=True, max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookuphabitat'


class Lookuplocalitytype(models.Model):
    localitytype = models.CharField(db_column='LocalityType', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookuplocalitytype'


class Lookupmediatype(models.Model):
    mediatype = models.CharField(db_column='MediaType', primary_key=True, max_length=255)  # Field name made lowercase.
    mediacategory = models.CharField(db_column='MediaCategory', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookupmediatype'


class Lookupparticipants(models.Model):
    participants = models.CharField(db_column='Participants', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookupparticipants'


class Lookuppartused(models.Model):
    partused = models.CharField(db_column='PartUsed', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookuppartused'


class Lookupplanningunit(models.Model):
    planningunitid = models.IntegerField(db_column='PlanningUnitID', primary_key=True)  # Field name made lowercase.
    planningunitname = models.CharField(db_column='PlanningUnitName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookupplanningunit'


class Lookupreferencetype(models.Model):
    documenttype = models.CharField(db_column='DocumentType', primary_key=True, max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookupreferencetype'


class Lookupresourcegroup(models.Model):
    resourceclassificationgroup = models.CharField(db_column='ResourceClassificationGroup', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookupresourcegroup'


class Lookupseason(models.Model):
    season = models.CharField(db_column='Season', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookupseason'


class Lookuptechniques(models.Model):
    techniques = models.CharField(db_column='Techniques', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookuptechniques'


class Lookuptiming(models.Model):
    timing = models.CharField(db_column='Timing', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookuptiming'


class Lookuptribe(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tribeunit = models.CharField(db_column='TribeUnit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tribe = models.CharField(db_column='Tribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    federaltribe = models.CharField(db_column='FederalTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookuptribe'


class Lookupuserinfo(models.Model):
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usingcustomusername = models.IntegerField(db_column='UsingCustomUsername')  # Field name made lowercase.
    usertitle = models.CharField(db_column='UserTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    useraffiliation = models.CharField(db_column='UserAffiliation', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookupuserinfo'


class Media(models.Model):
    mediaid = models.IntegerField(db_column='MediaID', primary_key=True)  # Field name made lowercase.
    mediatype = models.CharField(db_column='MediaType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    medianame = models.CharField(db_column='MediaName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mediadescription = models.TextField(db_column='MediaDescription', blank=True, null=True)  # Field name made lowercase.
    medialink = models.CharField(db_column='MediaLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'media'


class Mediacitationevents(models.Model):
    mediaid = models.IntegerField(db_column='MediaID')  # Field name made lowercase.
    citationid = models.IntegerField(db_column='CitationID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mediacitationevents'
        unique_together = (('mediaid', 'citationid'),)


class People(models.Model):
    personid = models.IntegerField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearborn = models.IntegerField(db_column='YearBorn', blank=True, null=True)  # Field name made lowercase.
    village = models.CharField(db_column='Village', max_length=255, blank=True, null=True)  # Field name made lowercase.
    relationshiptootherpeople = models.TextField(db_column='RelationshipToOtherPeople', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'people'


class Placealtindigenousname(models.Model):
    altindigenousnameid = models.IntegerField(db_column='AltIndigenousNameID', primary_key=True)  # Field name made lowercase.
    placeid = models.IntegerField(db_column='PlaceID', blank=True, null=True)  # Field name made lowercase.
    altindigenousname = models.CharField(db_column='AltIndigenousName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'placealtindigenousname'


class Placegisselections(models.Model):
    placeid = models.IntegerField(db_column='PlaceID', blank=True, null=True)  # Field name made lowercase.
    placelabel = models.CharField(db_column='PlaceLabel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcefc = models.CharField(db_column='SourceFC', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'placegisselections'


class Places(models.Model):
    placeid = models.IntegerField(db_column='PlaceID', primary_key=True)  # Field name made lowercase.
    indigenousplacename = models.CharField(db_column='IndigenousPlaceName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    indigenousplacenamemeaning = models.CharField(db_column='IndigenousPlaceNameMeaning', max_length=255, blank=True, null=True)  # Field name made lowercase.
    englishplacename = models.CharField(db_column='EnglishPlaceName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    planningunitid = models.IntegerField(db_column='PlanningUnitID', blank=True, null=True)  # Field name made lowercase.
    primaryhabitat = models.CharField(db_column='PrimaryHabitat', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tribeid = models.IntegerField(db_column='TribeID', blank=True, null=True)  # Field name made lowercase.
    islocked = models.IntegerField(db_column='IsLocked')  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'places'


class Placescitationevents(models.Model):
    placeid = models.IntegerField(db_column='PlaceID')  # Field name made lowercase.
    citationid = models.IntegerField(db_column='CitationID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'placescitationevents'
        unique_together = (('placeid', 'citationid'),)


class Placesmediaevents(models.Model):
    placeid = models.IntegerField(db_column='PlaceID')  # Field name made lowercase.
    mediaid = models.IntegerField(db_column='MediaID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'placesmediaevents'
        unique_together = (('placeid', 'mediaid'),)


class Placesresourcecitationevents(models.Model):
    placeresourceid = models.IntegerField(db_column='PlaceResourceID')  # Field name made lowercase.
    citationid = models.IntegerField(db_column='CitationID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'placesresourcecitationevents'
        unique_together = (('placeresourceid', 'citationid'),)


class Placesresourceevents(models.Model):
    placeresourceid = models.IntegerField(db_column='PlaceResourceID', primary_key=True)  # Field name made lowercase.
    placeid = models.IntegerField(db_column='PlaceID', blank=True, null=True)  # Field name made lowercase.
    resourceid = models.IntegerField(db_column='ResourceID', blank=True, null=True)  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    partused = models.CharField(db_column='PartUsed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customaryuse = models.CharField(db_column='CustomaryUse', max_length=255, blank=True, null=True)  # Field name made lowercase.
    barterresource = models.IntegerField(db_column='BarterResource')  # Field name made lowercase.
    season = models.CharField(db_column='Season', max_length=255, blank=True, null=True)  # Field name made lowercase.
    timing = models.CharField(db_column='Timing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    january = models.IntegerField(db_column='January')  # Field name made lowercase.
    february = models.IntegerField(db_column='February')  # Field name made lowercase.
    march = models.IntegerField(db_column='March')  # Field name made lowercase.
    april = models.IntegerField(db_column='April')  # Field name made lowercase.
    may = models.IntegerField(db_column='May')  # Field name made lowercase.
    june = models.IntegerField(db_column='June')  # Field name made lowercase.
    july = models.IntegerField(db_column='July')  # Field name made lowercase.
    august = models.IntegerField(db_column='August')  # Field name made lowercase.
    september = models.IntegerField(db_column='September')  # Field name made lowercase.
    october = models.IntegerField(db_column='October')  # Field name made lowercase.
    november = models.IntegerField(db_column='November')  # Field name made lowercase.
    december = models.IntegerField(db_column='December')  # Field name made lowercase.
    year = models.SmallIntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    islocked = models.IntegerField(db_column='IsLocked')  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'placesresourceevents'


class Placesresourcemediaevents(models.Model):
    placeresourceid = models.IntegerField(db_column='PlaceResourceID')  # Field name made lowercase.
    mediaid = models.IntegerField(db_column='MediaID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'placesresourcemediaevents'
        unique_together = (('placeresourceid', 'mediaid'),)


class Resourceactivitycitationevents(models.Model):
    resourceactivityid = models.IntegerField(db_column='ResourceActivityID')  # Field name made lowercase.
    citationid = models.IntegerField(db_column='CitationID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resourceactivitycitationevents'
        unique_together = (('resourceactivityid', 'citationid'),)


class Resourceactivitymediaevents(models.Model):
    resourceactivityid = models.IntegerField(db_column='ResourceActivityID')  # Field name made lowercase.
    mediaid = models.IntegerField(db_column='MediaID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resourceactivitymediaevents'
        unique_together = (('resourceactivityid', 'mediaid'),)


class Resourcealtindigenousname(models.Model):
    altindigenousnameid = models.IntegerField(db_column='AltIndigenousNameID', primary_key=True)  # Field name made lowercase.
    resourceid = models.IntegerField(db_column='ResourceID', blank=True, null=True)  # Field name made lowercase.
    altindigenousname = models.CharField(db_column='AltIndigenousName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resourcealtindigenousname'


class Resourceresourceevents(models.Model):
    resourceid = models.IntegerField(db_column='ResourceID')  # Field name made lowercase.
    altresourceid = models.IntegerField(db_column='AltResourceID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resourceresourceevents'
        unique_together = (('resourceid', 'altresourceid'),)


class Resources(models.Model):
    resourceid = models.IntegerField(db_column='ResourceID', primary_key=True)  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    indigenousname = models.CharField(db_column='IndigenousName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    genus = models.CharField(db_column='Genus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    species = models.CharField(db_column='Species', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specific = models.IntegerField(db_column='Specific')  # Field name made lowercase.
    resourceclassificationgroup = models.CharField(db_column='ResourceClassificationGroup', max_length=255, blank=True, null=True)  # Field name made lowercase.
    islocked = models.IntegerField(db_column='IsLocked')  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resources'


class Resourcesactivityevents(models.Model):
    resourceactivityid = models.IntegerField(db_column='ResourceActivityID', primary_key=True)  # Field name made lowercase.
    placeresourceid = models.IntegerField(db_column='PlaceResourceID', blank=True, null=True)  # Field name made lowercase.
    relationshipdescription = models.TextField(db_column='RelationshipDescription', blank=True, null=True)  # Field name made lowercase.
    partused = models.CharField(db_column='PartUsed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    activityshortdescription = models.CharField(db_column='ActivityShortDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    activitylongdescription = models.TextField(db_column='ActivityLongDescription', blank=True, null=True)  # Field name made lowercase.
    participants = models.CharField(db_column='Participants', max_length=50, blank=True, null=True)  # Field name made lowercase.
    technique = models.CharField(db_column='Technique', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gear = models.CharField(db_column='Gear', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customaryuse = models.CharField(db_column='CustomaryUse', max_length=255, blank=True, null=True)  # Field name made lowercase.
    timing = models.CharField(db_column='Timing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    timingdescription = models.CharField(db_column='TimingDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    islocked = models.IntegerField(db_column='IsLocked')  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resourcesactivityevents'


class Resourcescitationevents(models.Model):
    resourceid = models.IntegerField(db_column='ResourceID')  # Field name made lowercase.
    citationid = models.IntegerField(db_column='CitationID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resourcescitationevents'
        unique_together = (('resourceid', 'citationid'),)


class Resourcesmediaevents(models.Model):
    resourceid = models.IntegerField(db_column='ResourceID')  # Field name made lowercase.
    mediaid = models.IntegerField(db_column='MediaID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resourcesmediaevents'
        unique_together = (('resourceid', 'mediaid'),)


class Useraccess(models.Model):
    accessid = models.IntegerField(db_column='AccessID', primary_key=True)  # Field name made lowercase.
    accesslevel = models.CharField(db_column='AccessLevel', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'useraccess'


class Users(models.Model):
    userid = models.IntegerField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    affiliation = models.CharField(db_column='Affiliation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accesslevel = models.IntegerField(db_column='AccessLevel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
