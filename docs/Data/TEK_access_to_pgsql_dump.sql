--set schema 'tek';
--
-- DUMP FILE
--
-- Database is ported from MS Access
--------------------------------------------------------------------
-- Created using "MS Access to PostgreSQL" form http://www.bullzip.com
-- Program Version 5.5.280
--
-- OPTIONS:
--   sourcefilename=E:/GIS/projects/TEK_Tolowa_2017/MTKED/backend/db/ethnographic_elements_be.accdb
--   sourceusername=
--   sourcepassword=
--   sourcesystemdatabase=
--   destinationserver=
--   destinationdatabase=tek
--   maintenancedb=postgres
--   dropdatabase=0
--   createtables=1
--   unicode=1
--   autocommit=1
--   transferdefaultvalues=1
--   transferindexes=1
--   transferautonumbers=1
--   transferrecords=1
--   columnlist=1
--   tableprefix=
--   negativeboolean=0
--   ignorelargeblobs=0
--   memotype=TEXT
--   datetimetype=TIMESTAMP
--

CREATE DATABASE "tek";

-- NOTICE: At this place you need to connect to the new database and run the rest of the statements.

--
-- Table structure for table 'Citations'
--

DROP TABLE IF EXISTS "Citations";

CREATE TABLE "Citations" (
  "CitationID" SERIAL NOT NULL, 
  "ReferenceType" VARCHAR(255), 
  "ReferenceText" VARCHAR(50), 
  "AuthorType" VARCHAR(255), 
  "AuthorPrimary" VARCHAR(255), 
  "AuthorSecondary" VARCHAR(255), 
  "IntervieweeID" INTEGER, 
  "InterviewerID" INTEGER, 
  "PlaceofInterview" VARCHAR(255), 
  "Year" INTEGER, 
  "Title" TEXT, 
  "SeriesTitle" VARCHAR(255), 
  "SeriesVolume" VARCHAR(50), 
  "SeriesEditor" VARCHAR(255), 
  "Publisher" VARCHAR(100), 
  "PublisherCity" VARCHAR(255), 
  "PreparedFor" VARCHAR(100), 
  "Comments" TEXT, 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("CitationID")
);

--
-- Dumping data for table 'Citations'
--

-- 0 records

SELECT setval('"Citations_CitationID_seq"', MAX("CitationID")) FROM "Citations";

CREATE INDEX "Citations_CitationsCitationID" ON "Citations" ("CitationID");

CREATE INDEX "Citations_InteviewerID" ON "Citations" ("InterviewerID");

--
-- Table structure for table 'CurrentVersion'
--

DROP TABLE IF EXISTS "CurrentVersion";

CREATE TABLE "CurrentVersion" (
  "ID" SERIAL NOT NULL, 
  "BackendVersion" INTEGER, 
  "FrontendVersion" INTEGER, 
  PRIMARY KEY ("ID")
);

--
-- Dumping data for table 'CurrentVersion'
--

INSERT INTO "CurrentVersion" ("ID", "BackendVersion", "FrontendVersion") VALUES (1, 1, 1);
-- 1 records

SELECT setval('"CurrentVersion_ID_seq"', MAX("ID")) FROM "CurrentVersion";

--
-- Table structure for table 'Locality'
--

DROP TABLE IF EXISTS "Locality";

CREATE TABLE "Locality" (
  "LocalityID" SERIAL NOT NULL, 
  "PlaceID" INTEGER, 
  "EnglishName" VARCHAR(255), 
  "IndigenousName" VARCHAR(255), 
  "LocalityType" VARCHAR(255), 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("LocalityID")
);

--
-- Dumping data for table 'Locality'
--

-- 0 records

SELECT setval('"Locality_LocalityID_seq"', MAX("LocalityID")) FROM "Locality";

CREATE INDEX "Locality_LocalityID" ON "Locality" ("LocalityID");

CREATE INDEX "Locality_PlaceID" ON "Locality" ("PlaceID");

--
-- Table structure for table 'LocalityGISSelections'
--

DROP TABLE IF EXISTS "LocalityGISSelections";

CREATE TABLE "LocalityGISSelections" (
  "LocalityID" INTEGER, 
  "LocalityLabel" VARCHAR(255), 
  "SourceFC" VARCHAR(255)
);

--
-- Dumping data for table 'LocalityGISSelections'
--

-- 0 records

--
-- Table structure for table 'LocalityPlaceResourceEvent'
--

DROP TABLE IF EXISTS "LocalityPlaceResourceEvent";

CREATE TABLE "LocalityPlaceResourceEvent" (
  "PlaceResourceID" INTEGER NOT NULL, 
  "LocalityID" INTEGER NOT NULL, 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("PlaceResourceID", "LocalityID")
);

--
-- Dumping data for table 'LocalityPlaceResourceEvent'
--

-- 0 records

CREATE INDEX "LocalityPlaceResourceEvent_LocalityID" ON "LocalityPlaceResourceEvent" ("LocalityID");

CREATE INDEX "LocalityPlaceResourceEvent_PlaceResourceID" ON "LocalityPlaceResourceEvent" ("PlaceResourceID");

--
-- Table structure for table 'LookupActivity'
--

DROP TABLE IF EXISTS "LookupActivity";

CREATE TABLE "LookupActivity" (
  "Activity" VARCHAR(255) NOT NULL, 
  PRIMARY KEY ("Activity")
);

--
-- Dumping data for table 'LookupActivity'
--

INSERT INTO "LookupActivity" ("Activity") VALUES (E'Cemetery');
INSERT INTO "LookupActivity" ("Activity") VALUES (E'Customary Fishing and Gathering from Shore');
INSERT INTO "LookupActivity" ("Activity") VALUES (E'Customary Fishing and Gathering Offshore');
INSERT INTO "LookupActivity" ("Activity") VALUES (E'Customary Hunting from Shore');
INSERT INTO "LookupActivity" ("Activity") VALUES (E'Customary Hunting Offshore');
INSERT INTO "LookupActivity" ("Activity") VALUES (E'Processing');
INSERT INTO "LookupActivity" ("Activity") VALUES (E'Related to Ceremony');
INSERT INTO "LookupActivity" ("Activity") VALUES (E'Related to Song');
INSERT INTO "LookupActivity" ("Activity") VALUES (E'Related to Story');
INSERT INTO "LookupActivity" ("Activity") VALUES (E'Residence/Village');
INSERT INTO "LookupActivity" ("Activity") VALUES (E'Training');
-- 11 records

--
-- Table structure for table 'LookupAuthorType'
--

DROP TABLE IF EXISTS "LookupAuthorType";

CREATE TABLE "LookupAuthorType" (
  "AuthorType" VARCHAR(50) NOT NULL, 
  PRIMARY KEY ("AuthorType")
);

--
-- Dumping data for table 'LookupAuthorType'
--

INSERT INTO "LookupAuthorType" ("AuthorType") VALUES (E'Author');
INSERT INTO "LookupAuthorType" ("AuthorType") VALUES (E'Corporate Author');
INSERT INTO "LookupAuthorType" ("AuthorType") VALUES (E'Editor');
-- 3 records

--
-- Table structure for table 'LookupCustomaryUse'
--

DROP TABLE IF EXISTS "LookupCustomaryUse";

CREATE TABLE "LookupCustomaryUse" (
  "UsedFor" VARCHAR(255) NOT NULL, 
  PRIMARY KEY ("UsedFor")
);

--
-- Dumping data for table 'LookupCustomaryUse'
--

INSERT INTO "LookupCustomaryUse" ("UsedFor") VALUES (E'Barter');
INSERT INTO "LookupCustomaryUse" ("UsedFor") VALUES (E'Ceremony');
INSERT INTO "LookupCustomaryUse" ("UsedFor") VALUES (E'Food');
INSERT INTO "LookupCustomaryUse" ("UsedFor") VALUES (E'Regalia');
INSERT INTO "LookupCustomaryUse" ("UsedFor") VALUES (E'Song');
INSERT INTO "LookupCustomaryUse" ("UsedFor") VALUES (E'Story');
INSERT INTO "LookupCustomaryUse" ("UsedFor") VALUES (E'Tool');
-- 7 records

--
-- Table structure for table 'LookupHabitat'
--

DROP TABLE IF EXISTS "LookupHabitat";

CREATE TABLE "LookupHabitat" (
  "Habitat" VARCHAR(100) NOT NULL, 
  PRIMARY KEY ("Habitat")
);

--
-- Dumping data for table 'LookupHabitat'
--

INSERT INTO "LookupHabitat" ("Habitat") VALUES (E'Coastal Marsh');
INSERT INTO "LookupHabitat" ("Habitat") VALUES (E'Deep Canyon');
INSERT INTO "LookupHabitat" ("Habitat") VALUES (E'Estuary');
INSERT INTO "LookupHabitat" ("Habitat") VALUES (E'Hard-bottom >100m');
INSERT INTO "LookupHabitat" ("Habitat") VALUES (E'Hard-bottom 0-100m');
INSERT INTO "LookupHabitat" ("Habitat") VALUES (E'Offshore Reefs');
INSERT INTO "LookupHabitat" ("Habitat") VALUES (E'Offshore Rock');
INSERT INTO "LookupHabitat" ("Habitat") VALUES (E'Rocky Intertidal');
INSERT INTO "LookupHabitat" ("Habitat") VALUES (E'Sandy Beach');
INSERT INTO "LookupHabitat" ("Habitat") VALUES (E'Soft-bottom >100m');
INSERT INTO "LookupHabitat" ("Habitat") VALUES (E'Soft-bottom 0-100m');
INSERT INTO "LookupHabitat" ("Habitat") VALUES (E'Tidal Flats');
-- 12 records

CREATE INDEX "LookupHabitat_LookupHabitatID" ON "LookupHabitat" ("Habitat");

--
-- Table structure for table 'LookupLocalityType'
--

DROP TABLE IF EXISTS "LookupLocalityType";

CREATE TABLE "LookupLocalityType" (
  "LocalityType" VARCHAR(255) NOT NULL, 
  PRIMARY KEY ("LocalityType")
);

--
-- Dumping data for table 'LookupLocalityType'
--

INSERT INTO "LookupLocalityType" ("LocalityType") VALUES (E'bay');
INSERT INTO "LookupLocalityType" ("LocalityType") VALUES (E'beach');
INSERT INTO "LookupLocalityType" ("LocalityType") VALUES (E'creek');
INSERT INTO "LookupLocalityType" ("LocalityType") VALUES (E'estuary');
INSERT INTO "LookupLocalityType" ("LocalityType") VALUES (E'intertidal');
INSERT INTO "LookupLocalityType" ("LocalityType") VALUES (E'lagoon');
INSERT INTO "LookupLocalityType" ("LocalityType") VALUES (E'mainstem river');
INSERT INTO "LookupLocalityType" ("LocalityType") VALUES (E'offshore rocks');
INSERT INTO "LookupLocalityType" ("LocalityType") VALUES (E'open ocean');
INSERT INTO "LookupLocalityType" ("LocalityType") VALUES (E'river eddy');
INSERT INTO "LookupLocalityType" ("LocalityType") VALUES (E'river mouth');
INSERT INTO "LookupLocalityType" ("LocalityType") VALUES (E'side channel river');
INSERT INTO "LookupLocalityType" ("LocalityType") VALUES (E'subtidal');
-- 13 records

--
-- Table structure for table 'LookupMediaType'
--

DROP TABLE IF EXISTS "LookupMediaType";

CREATE TABLE "LookupMediaType" (
  "MediaType" VARCHAR(255) NOT NULL, 
  "MediaCategory" VARCHAR(255), 
  PRIMARY KEY ("MediaType")
);

--
-- Dumping data for table 'LookupMediaType'
--

INSERT INTO "LookupMediaType" ("MediaType", "MediaCategory") VALUES (E'audio', NULL);
INSERT INTO "LookupMediaType" ("MediaType", "MediaCategory") VALUES (E'image', NULL);
INSERT INTO "LookupMediaType" ("MediaType", "MediaCategory") VALUES (E'other', NULL);
INSERT INTO "LookupMediaType" ("MediaType", "MediaCategory") VALUES (E'PDF', NULL);
INSERT INTO "LookupMediaType" ("MediaType", "MediaCategory") VALUES (E'video', NULL);
-- 5 records

--
-- Table structure for table 'LookupParticipants'
--

DROP TABLE IF EXISTS "LookupParticipants";

CREATE TABLE "LookupParticipants" (
  "Participants" VARCHAR(255) NOT NULL, 
  PRIMARY KEY ("Participants")
);

--
-- Dumping data for table 'LookupParticipants'
--

INSERT INTO "LookupParticipants" ("Participants") VALUES (E'Children');
INSERT INTO "LookupParticipants" ("Participants") VALUES (E'Children-boys');
INSERT INTO "LookupParticipants" ("Participants") VALUES (E'Children-girls');
INSERT INTO "LookupParticipants" ("Participants") VALUES (E'Everyone');
INSERT INTO "LookupParticipants" ("Participants") VALUES (E'Men');
INSERT INTO "LookupParticipants" ("Participants") VALUES (E'Other beings');
INSERT INTO "LookupParticipants" ("Participants") VALUES (E'Women');
-- 7 records

--
-- Table structure for table 'LookupPartUsed'
--

DROP TABLE IF EXISTS "LookupPartUsed";

CREATE TABLE "LookupPartUsed" (
  "PartUsed" VARCHAR(255) NOT NULL, 
  PRIMARY KEY ("PartUsed")
);

--
-- Dumping data for table 'LookupPartUsed'
--

INSERT INTO "LookupPartUsed" ("PartUsed") VALUES (E'Antler');
INSERT INTO "LookupPartUsed" ("PartUsed") VALUES (E'Bone');
INSERT INTO "LookupPartUsed" ("PartUsed") VALUES (E'Egg');
INSERT INTO "LookupPartUsed" ("PartUsed") VALUES (E'Feather');
INSERT INTO "LookupPartUsed" ("PartUsed") VALUES (E'Flower');
INSERT INTO "LookupPartUsed" ("PartUsed") VALUES (E'Meat');
INSERT INTO "LookupPartUsed" ("PartUsed") VALUES (E'Shell');
INSERT INTO "LookupPartUsed" ("PartUsed") VALUES (E'Tooth');
INSERT INTO "LookupPartUsed" ("PartUsed") VALUES (E'Whisker');
-- 9 records

--
-- Table structure for table 'LookupPlanningUnit'
--

DROP TABLE IF EXISTS "LookupPlanningUnit";

CREATE TABLE "LookupPlanningUnit" (
  "PlanningUnitID" INTEGER NOT NULL, 
  "PlanningUnitName" VARCHAR(100), 
  PRIMARY KEY ("PlanningUnitID")
);

--
-- Dumping data for table 'LookupPlanningUnit'
--

INSERT INTO "LookupPlanningUnit" ("PlanningUnitID", "PlanningUnitName") VALUES (0, E'Undefined');
INSERT INTO "LookupPlanningUnit" ("PlanningUnitID", "PlanningUnitName") VALUES (1, E'Southern');
INSERT INTO "LookupPlanningUnit" ("PlanningUnitID", "PlanningUnitName") VALUES (2, E'Northern');
INSERT INTO "LookupPlanningUnit" ("PlanningUnitID", "PlanningUnitName") VALUES (3, E'Middle');
-- 4 records

CREATE INDEX "LookupPlanningUnit_PlanningUnitID" ON "LookupPlanningUnit" ("PlanningUnitID");

--
-- Table structure for table 'LookupReferenceType'
--

DROP TABLE IF EXISTS "LookupReferenceType";

CREATE TABLE "LookupReferenceType" (
  "DocumentType" VARCHAR(25) NOT NULL, 
  PRIMARY KEY ("DocumentType")
);

--
-- Dumping data for table 'LookupReferenceType'
--

INSERT INTO "LookupReferenceType" ("DocumentType") VALUES (E'Book');
INSERT INTO "LookupReferenceType" ("DocumentType") VALUES (E'Other');
INSERT INTO "LookupReferenceType" ("DocumentType") VALUES (E'Edited Volume');
INSERT INTO "LookupReferenceType" ("DocumentType") VALUES (E'Interview');
-- 4 records

--
-- Table structure for table 'LookupResourceGroup'
--

DROP TABLE IF EXISTS "LookupResourceGroup";

CREATE TABLE "LookupResourceGroup" (
  "ResourceClassificationGroup" VARCHAR(255) NOT NULL, 
  PRIMARY KEY ("ResourceClassificationGroup")
);

--
-- Dumping data for table 'LookupResourceGroup'
--

INSERT INTO "LookupResourceGroup" ("ResourceClassificationGroup") VALUES (E'anadromous finfish');
INSERT INTO "LookupResourceGroup" ("ResourceClassificationGroup") VALUES (E'bird');
INSERT INTO "LookupResourceGroup" ("ResourceClassificationGroup") VALUES (E'coastal watershed mammal');
INSERT INTO "LookupResourceGroup" ("ResourceClassificationGroup") VALUES (E'crustacean');
INSERT INTO "LookupResourceGroup" ("ResourceClassificationGroup") VALUES (E'fern & relative');
INSERT INTO "LookupResourceGroup" ("ResourceClassificationGroup") VALUES (E'flowering plant');
INSERT INTO "LookupResourceGroup" ("ResourceClassificationGroup") VALUES (E'invertebrate');
INSERT INTO "LookupResourceGroup" ("ResourceClassificationGroup") VALUES (E'marine finfish');
INSERT INTO "LookupResourceGroup" ("ResourceClassificationGroup") VALUES (E'marine mammal');
INSERT INTO "LookupResourceGroup" ("ResourceClassificationGroup") VALUES (E'mollusk');
INSERT INTO "LookupResourceGroup" ("ResourceClassificationGroup") VALUES (E'seaweed/algae');
INSERT INTO "LookupResourceGroup" ("ResourceClassificationGroup") VALUES (E'tree');
-- 12 records

--
-- Table structure for table 'LookupSeason'
--

DROP TABLE IF EXISTS "LookupSeason";

CREATE TABLE "LookupSeason" (
  "Season" VARCHAR(255) NOT NULL, 
  PRIMARY KEY ("Season")
);

--
-- Dumping data for table 'LookupSeason'
--

INSERT INTO "LookupSeason" ("Season") VALUES (E'All');
INSERT INTO "LookupSeason" ("Season") VALUES (E'Fall');
INSERT INTO "LookupSeason" ("Season") VALUES (E'Fall/Winter');
INSERT INTO "LookupSeason" ("Season") VALUES (E'Spring');
INSERT INTO "LookupSeason" ("Season") VALUES (E'Spring/Summer');
INSERT INTO "LookupSeason" ("Season") VALUES (E'Summer');
INSERT INTO "LookupSeason" ("Season") VALUES (E'Summer/Fall');
INSERT INTO "LookupSeason" ("Season") VALUES (E'Winter');
INSERT INTO "LookupSeason" ("Season") VALUES (E'Winter/Spring');
-- 9 records

--
-- Table structure for table 'LookupTechniques'
--

DROP TABLE IF EXISTS "LookupTechniques";

CREATE TABLE "LookupTechniques" (
  "Techniques" VARCHAR(255) NOT NULL, 
  PRIMARY KEY ("Techniques")
);

--
-- Dumping data for table 'LookupTechniques'
--

INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'A-frame net');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'canoe');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'club');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'conical basket');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'dip net');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'eel basket');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'eel hook');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'gaff hook');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'gill net');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'hand fishing');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'hand gathered');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'harpoon');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'hook and line');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'net');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'poison');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'seine');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'snare');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'spears with detachable points');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'spears without detachable points');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'V-frame scoop net');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'V-shaped/converging weir');
INSERT INTO "LookupTechniques" ("Techniques") VALUES (E'weir/fish dam');
-- 22 records

--
-- Table structure for table 'LookupTiming'
--

DROP TABLE IF EXISTS "LookupTiming";

CREATE TABLE "LookupTiming" (
  "Timing" VARCHAR(255) NOT NULL, 
  PRIMARY KEY ("Timing")
);

--
-- Dumping data for table 'LookupTiming'
--

INSERT INTO "LookupTiming" ("Timing") VALUES (E'Daytime');
INSERT INTO "LookupTiming" ("Timing") VALUES (E'Evening');
INSERT INTO "LookupTiming" ("Timing") VALUES (E'Fall');
INSERT INTO "LookupTiming" ("Timing") VALUES (E'Morning');
INSERT INTO "LookupTiming" ("Timing") VALUES (E'Night');
INSERT INTO "LookupTiming" ("Timing") VALUES (E'Seasonal');
INSERT INTO "LookupTiming" ("Timing") VALUES (E'Spring');
INSERT INTO "LookupTiming" ("Timing") VALUES (E'Summer');
INSERT INTO "LookupTiming" ("Timing") VALUES (E'Winter');
-- 9 records

--
-- Table structure for table 'LookupTribe'
--

DROP TABLE IF EXISTS "LookupTribe";

CREATE TABLE "LookupTribe" (
  "ID" SERIAL NOT NULL, 
  "TribeUnit" VARCHAR(50), 
  "Tribe" VARCHAR(100), 
  "FederalTribe" VARCHAR(100), 
  PRIMARY KEY ("ID")
);

--
-- Dumping data for table 'LookupTribe'
--

INSERT INTO "LookupTribe" ("ID", "TribeUnit", "Tribe", "FederalTribe") VALUES (1, E'Tolowa Dee-ni’', E'Tolowa', E'Smith River Rancheria');
-- 1 records

SELECT setval('"LookupTribe_ID_seq"', MAX("ID")) FROM "LookupTribe";

--
-- Table structure for table 'LookupUserInfo'
--

DROP TABLE IF EXISTS "LookupUserInfo";

CREATE TABLE "LookupUserInfo" (
  "UserName" VARCHAR(100), 
  "UsingCustomUsername" BOOLEAN DEFAULT E'0', 
  "UserTitle" VARCHAR(100), 
  "UserAffiliation" VARCHAR(100)
);

--
-- Dumping data for table 'LookupUserInfo'
--

INSERT INTO "LookupUserInfo" ("UserName", "UsingCustomUsername", "UserTitle", "UserAffiliation") VALUES (E'gary', E'0', E'gis', E'fw');
-- 1 records

--
-- Table structure for table 'Media'
--

DROP TABLE IF EXISTS "Media";

CREATE TABLE "Media" (
  "MediaID" SERIAL NOT NULL, 
  "MediaType" VARCHAR(255), 
  "MediaName" VARCHAR(255), 
  "MediaDescription" TEXT, 
  "MediaLink" VARCHAR(255), 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("MediaID")
);

--
-- Dumping data for table 'Media'
--

-- 0 records

SELECT setval('"Media_MediaID_seq"', MAX("MediaID")) FROM "Media";

CREATE INDEX "Media_MediaID" ON "Media" ("MediaID");

--
-- Table structure for table 'MediaCitationEvents'
--

DROP TABLE IF EXISTS "MediaCitationEvents";

CREATE TABLE "MediaCitationEvents" (
  "MediaID" INTEGER NOT NULL, 
  "CitationID" INTEGER NOT NULL, 
  "RelationshipDescription" VARCHAR(255), 
  "Pages" VARCHAR(255), 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("MediaID", "CitationID")
);

--
-- Dumping data for table 'MediaCitationEvents'
--

-- 0 records

CREATE INDEX "MediaCitationEvents_PlaceID" ON "MediaCitationEvents" ("MediaID");

CREATE INDEX "MediaCitationEvents_SpeciesID" ON "MediaCitationEvents" ("CitationID");

--
-- Table structure for table 'People'
--

DROP TABLE IF EXISTS "People";

CREATE TABLE "People" (
  "PersonID" SERIAL NOT NULL, 
  "FirstName" VARCHAR(255), 
  "LastName" VARCHAR(255), 
  "YearBorn" INTEGER, 
  "Village" VARCHAR(255), 
  "RelationshipToOtherPeople" TEXT, 
  PRIMARY KEY ("PersonID")
);

--
-- Dumping data for table 'People'
--

-- 0 records

SELECT setval('"People_PersonID_seq"', MAX("PersonID")) FROM "People";

CREATE INDEX "People_PersonID" ON "People" ("PersonID");

--
-- Table structure for table 'PlaceAltIndigenousName'
--

DROP TABLE IF EXISTS "PlaceAltIndigenousName";

CREATE TABLE "PlaceAltIndigenousName" (
  "AltIndigenousNameID" SERIAL NOT NULL, 
  "PlaceID" INTEGER, 
  "AltIndigenousName" VARCHAR(255), 
  PRIMARY KEY ("AltIndigenousNameID")
);

--
-- Dumping data for table 'PlaceAltIndigenousName'
--

-- 0 records

SELECT setval('"PlaceAltIndigenousName_AltIndigenousNameID_seq"', MAX("AltIndigenousNameID")) FROM "PlaceAltIndigenousName";

CREATE INDEX "PlaceAltIndigenousName_AltIndigenousNameID" ON "PlaceAltIndigenousName" ("AltIndigenousNameID");

CREATE INDEX "PlaceAltIndigenousName_PlaceID" ON "PlaceAltIndigenousName" ("PlaceID");

--
-- Table structure for table 'PlaceGISSelections'
--

DROP TABLE IF EXISTS "PlaceGISSelections";

CREATE TABLE "PlaceGISSelections" (
  "PlaceID" INTEGER, 
  "PlaceLabel" VARCHAR(255), 
  "SourceFC" VARCHAR(255)
);

--
-- Dumping data for table 'PlaceGISSelections'
--

-- 0 records

--
-- Table structure for table 'Places'
--

DROP TABLE IF EXISTS "Places";

CREATE TABLE "Places" (
  "PlaceID" SERIAL NOT NULL, 
  "IndigenousPlaceName" VARCHAR(255), 
  "IndigenousPlaceNameMeaning" VARCHAR(255), 
  "EnglishPlaceName" VARCHAR(255), 
  "PlanningUnitID" INTEGER DEFAULT 0, 
  "PrimaryHabitat" VARCHAR(100), 
  "TribeID" INTEGER, 
  "IsLocked" BOOLEAN DEFAULT E'0', 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("PlaceID")
);

--
-- Dumping data for table 'Places'
--

-- 0 records

SELECT setval('"Places_PlaceID_seq"', MAX("PlaceID")) FROM "Places";

CREATE INDEX "Places_PlaceID" ON "Places" ("PlaceID");

CREATE INDEX "Places_PlanningUnitID" ON "Places" ("PlanningUnitID");

--
-- Table structure for table 'PlacesCitationEvents'
--

DROP TABLE IF EXISTS "PlacesCitationEvents";

CREATE TABLE "PlacesCitationEvents" (
  "PlaceID" INTEGER NOT NULL, 
  "CitationID" INTEGER NOT NULL, 
  "RelationshipDescription" VARCHAR(255), 
  "Pages" VARCHAR(255), 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("PlaceID", "CitationID")
);

--
-- Dumping data for table 'PlacesCitationEvents'
--

-- 0 records

CREATE INDEX "PlacesCitationEvents_PlaceID" ON "PlacesCitationEvents" ("PlaceID");

CREATE INDEX "PlacesCitationEvents_SpeciesID" ON "PlacesCitationEvents" ("CitationID");

--
-- Table structure for table 'PlacesMediaEvents'
--

DROP TABLE IF EXISTS "PlacesMediaEvents";

CREATE TABLE "PlacesMediaEvents" (
  "PlaceID" INTEGER NOT NULL, 
  "MediaID" INTEGER NOT NULL, 
  "RelationshipDescription" VARCHAR(255), 
  "Pages" VARCHAR(50), 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("PlaceID", "MediaID")
);

--
-- Dumping data for table 'PlacesMediaEvents'
--

-- 0 records

CREATE INDEX "PlacesMediaEvents_MediaID" ON "PlacesMediaEvents" ("MediaID");

CREATE INDEX "PlacesMediaEvents_PlacesID" ON "PlacesMediaEvents" ("PlaceID");

--
-- Table structure for table 'PlacesResourceCitationEvents'
--

DROP TABLE IF EXISTS "PlacesResourceCitationEvents";

CREATE TABLE "PlacesResourceCitationEvents" (
  "PlaceResourceID" INTEGER NOT NULL, 
  "CitationID" INTEGER NOT NULL, 
  "RelationshipDescription" VARCHAR(255), 
  "Pages" VARCHAR(255), 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("PlaceResourceID", "CitationID")
);

--
-- Dumping data for table 'PlacesResourceCitationEvents'
--

-- 0 records

CREATE INDEX "PlacesResourceCitationEvents_PlaceResourceID" ON "PlacesResourceCitationEvents" ("PlaceResourceID");

CREATE INDEX "PlacesResourceCitationEvents_SpeciesID" ON "PlacesResourceCitationEvents" ("CitationID");

--
-- Table structure for table 'PlacesResourceEvents'
--

DROP TABLE IF EXISTS "PlacesResourceEvents";

CREATE TABLE "PlacesResourceEvents" (
  "PlaceResourceID" SERIAL NOT NULL, 
  "PlaceID" INTEGER NOT NULL, 
  "ResourceID" INTEGER NOT NULL, 
  "RelationshipDescription" VARCHAR(255), 
  "PartUsed" VARCHAR(255), 
  "CustomaryUse" VARCHAR(255), 
  "BarterResource" BOOLEAN DEFAULT E'0', 
  "Season" VARCHAR(255), 
  "Timing" VARCHAR(255), 
  "January" BOOLEAN DEFAULT E'0', 
  "February" BOOLEAN DEFAULT E'0', 
  "March" BOOLEAN DEFAULT E'0', 
  "April" BOOLEAN DEFAULT E'0', 
  "May" BOOLEAN DEFAULT E'0', 
  "June" BOOLEAN DEFAULT E'0', 
  "July" BOOLEAN DEFAULT E'0', 
  "August" BOOLEAN DEFAULT E'0', 
  "September" BOOLEAN DEFAULT E'0', 
  "October" BOOLEAN DEFAULT E'0', 
  "November" BOOLEAN DEFAULT E'0', 
  "December" BOOLEAN DEFAULT E'0', 
  "Year" INTEGER, 
  "IsLocked" BOOLEAN DEFAULT E'0', 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("PlaceResourceID")
);

--
-- Dumping data for table 'PlacesResourceEvents'
--

-- 0 records

SELECT setval('"PlacesResourceEvents_PlaceResourceID_seq"', MAX("PlaceResourceID")) FROM "PlacesResourceEvents";

CREATE INDEX "PlacesResourceEvents_NoDuplicates" ON "PlacesResourceEvents" ("PlaceID", "ResourceID");

CREATE INDEX "PlacesResourceEvents_PlaceID" ON "PlacesResourceEvents" ("PlaceID");

CREATE INDEX "PlacesResourceEvents_PlaceResourceID" ON "PlacesResourceEvents" ("PlaceResourceID");

CREATE INDEX "PlacesResourceEvents_ResourceID" ON "PlacesResourceEvents" ("ResourceID");

--
-- Table structure for table 'PlacesResourceMediaEvents'
--

DROP TABLE IF EXISTS "PlacesResourceMediaEvents";

CREATE TABLE "PlacesResourceMediaEvents" (
  "PlaceResourceID" INTEGER NOT NULL, 
  "MediaID" INTEGER NOT NULL, 
  "RelationshipDescription" VARCHAR(255), 
  "Pages" VARCHAR(50), 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("PlaceResourceID", "MediaID")
);

--
-- Dumping data for table 'PlacesResourceMediaEvents'
--

-- 0 records

CREATE INDEX "PlacesResourceMediaEvents_PlaceResourceID" ON "PlacesResourceMediaEvents" ("PlaceResourceID");

CREATE INDEX "PlacesResourceMediaEvents_SpeciesID" ON "PlacesResourceMediaEvents" ("MediaID");

--
-- Table structure for table 'ResourceActivityCitationEvents'
--

DROP TABLE IF EXISTS "ResourceActivityCitationEvents";

CREATE TABLE "ResourceActivityCitationEvents" (
  "ResourceActivityID" INTEGER NOT NULL, 
  "CitationID" INTEGER NOT NULL, 
  "RelationshipDescription" VARCHAR(255), 
  "Pages" VARCHAR(255), 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("ResourceActivityID", "CitationID")
);

--
-- Dumping data for table 'ResourceActivityCitationEvents'
--

-- 0 records

CREATE INDEX "ResourceActivityCitationEvents_ResourceActivityID" ON "ResourceActivityCitationEvents" ("ResourceActivityID");

CREATE INDEX "ResourceActivityCitationEvents_SpeciesID" ON "ResourceActivityCitationEvents" ("CitationID");

--
-- Table structure for table 'ResourceActivityMediaEvents'
--

DROP TABLE IF EXISTS "ResourceActivityMediaEvents";

CREATE TABLE "ResourceActivityMediaEvents" (
  "ResourceActivityID" INTEGER NOT NULL, 
  "MediaID" INTEGER NOT NULL, 
  "RelationshipDescription" VARCHAR(255), 
  "Pages" VARCHAR(50), 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("ResourceActivityID", "MediaID")
);

--
-- Dumping data for table 'ResourceActivityMediaEvents'
--

-- 0 records

CREATE INDEX "ResourceActivityMediaEvents_ResourceActivityID" ON "ResourceActivityMediaEvents" ("ResourceActivityID");

CREATE INDEX "ResourceActivityMediaEvents_SpeciesID" ON "ResourceActivityMediaEvents" ("MediaID");

--
-- Table structure for table 'ResourceAltIndigenousName'
--

DROP TABLE IF EXISTS "ResourceAltIndigenousName";

CREATE TABLE "ResourceAltIndigenousName" (
  "AltIndigenousNameID" SERIAL NOT NULL, 
  "ResourceID" INTEGER, 
  "AltIndigenousName" VARCHAR(255), 
  PRIMARY KEY ("AltIndigenousNameID")
);

--
-- Dumping data for table 'ResourceAltIndigenousName'
--

-- 0 records

SELECT setval('"ResourceAltIndigenousName_AltIndigenousNameID_seq"', MAX("AltIndigenousNameID")) FROM "ResourceAltIndigenousName";

CREATE INDEX "ResourceAltIndigenousName_AltIndigenousNameID" ON "ResourceAltIndigenousName" ("AltIndigenousNameID");

CREATE INDEX "ResourceAltIndigenousName_ResourceID" ON "ResourceAltIndigenousName" ("ResourceID");

--
-- Table structure for table 'ResourceResourceEvents'
--

DROP TABLE IF EXISTS "ResourceResourceEvents";

CREATE TABLE "ResourceResourceEvents" (
  "ResourceID" INTEGER NOT NULL, 
  "AltResourceID" INTEGER NOT NULL, 
  "RelationshipDescription" VARCHAR(255), 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("ResourceID", "AltResourceID")
);

--
-- Dumping data for table 'ResourceResourceEvents'
--

-- 0 records

CREATE INDEX "ResourceResourceEvents_PlaceID" ON "ResourceResourceEvents" ("ResourceID");

CREATE INDEX "ResourceResourceEvents_SpeciesID" ON "ResourceResourceEvents" ("AltResourceID");

--
-- Table structure for table 'Resources'
--

DROP TABLE IF EXISTS "Resources";

CREATE TABLE "Resources" (
  "ResourceID" SERIAL NOT NULL, 
  "CommonName" VARCHAR(255), 
  "IndigenousName" VARCHAR(255), 
  "Genus" VARCHAR(255), 
  "Species" VARCHAR(255), 
  "Specific" BOOLEAN DEFAULT E'0', 
  "ResourceClassificationGroup" VARCHAR(255), 
  "IsLocked" BOOLEAN DEFAULT E'0', 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("ResourceID")
);

--
-- Dumping data for table 'Resources'
--

INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (150, E'abalone', NULL, E'Haliotis', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, E'', E'', E'', '2014-08-14 20:59:09');
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (151, E'abalone, Black', NULL, E'Haliotis', E'cracherdoii', E'1', NULL, E'0', NULL, NULL, NULL, NULL, E'paul', E'GIS', E'Far Western', '2014-08-26 19:42:54');
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (152, E'abalone, Flat', NULL, E'Haliotis ', E'walallensis', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (153, E'abalone, Pinto/Northern', NULL, E'Haliotis ', E'kamtschatkana ', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (154, E'abalone, Red', NULL, E'Haliotis ', E'rufescens', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (155, E'alder, Red', NULL, E'Alnus', E'rubra', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (156, E'ash', NULL, E'Fraxinus', E'latifolia', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (157, E'aven', NULL, E'Geum', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (158, E'baneberry', NULL, E'Actaea', E'rubra', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (159, E'barnacle', NULL, E'Balanus', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (160, E'barnacle, Acorn', NULL, E'Balanus ', E'glandula', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (161, E'barnacle, Crenate', NULL, E'Balanus', E'crenatus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (162, E'barnacle, Giant', NULL, E'Balanus', E'nubilus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (163, E'barnacle, Gooseneck/Longneck/Pig''s foot)', NULL, E'Lepas', E'anatifera', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (164, E'barnacle, Leaf ', NULL, E'Pollicipes ', E'polymerus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (165, E'barnacle, Thatched', NULL, E'Semibalanus', E'cariosus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (166, E'beach grass', NULL, E'Ammophil', E'arenaria', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (167, E'beach pea', NULL, E'Lathyrus', E'japonicus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (168, E'beargrass /elkgrass', NULL, E'Xerophyllum', E'tenax', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (169, E'beaver', NULL, E'Castor', E'canadensis', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (170, E'black bass', NULL, E'Sebastes', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (171, E'black bear', NULL, E'Ursus', E'americanus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (172, E'Black turban snails', NULL, E'Tegula ', E'funebralis', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (173, E'blackberry, Evergreen', NULL, E'Rubus', E'laciniatus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (174, E'blackberry, Trailing/ Dewberry', NULL, E'Rubus', E'ursinus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (175, E'blueberry', NULL, E'Vaccinium', E'sp.', E'0', E'plant', E'0', NULL, NULL, NULL, NULL, E'paul', E'gis', E'fw', '2014-06-20 13:49:22');
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (176, E'bobcat', NULL, E'Lynx', E'rufus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (177, E'Bocaccio ', NULL, E'Sebastes ', E'paucispinus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (178, E'bull trout', NULL, E'Salvelinus', E'confluentus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (179, E'bullhead', NULL, NULL, NULL, E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (180, E'bulrush/ tule', NULL, E'Scirpus', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (181, E'Cabezon', NULL, E'Scorpaenichthys ', E'marmoratus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (182, E'camas', NULL, E'Camassia', E'quamash', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (183, E'cattail', NULL, E'Typha ', E'latifolia', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (184, E'cedar', NULL, NULL, NULL, E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (185, E'cedar, Western red', NULL, E'Thuja', E'plicata', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (186, E'China hats', NULL, NULL, NULL, E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (187, E'chiton', NULL, E'Mopalia', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (188, E'chiton, Gumboot', NULL, E'Cryptochiton', E'stelleri', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (189, E'clam', NULL, NULL, NULL, E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (190, E'clam, Butter', NULL, E'Saxidomus', E'giganteus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (191, E'clam, Manila', NULL, E'Tapes', E'japonica', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (192, E'clam, Quahog', NULL, E'Mercenaria', E'mercenaria', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (193, E'clam, Razor', NULL, E'Siliqua', E'patula', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (194, E'clam, Soft-shell/Mud', NULL, E'Mya', E'arenaria', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (195, E'clover', NULL, E'Trifolium', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (196, E'cockel', NULL, E'Clinocardium ', E'nuttallii', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (197, E'codfishes', NULL, E'Gadidae', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (198, E'cottonwood', NULL, E'Populus', E'balsamifera', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (199, E'cougar', NULL, E'Puma', E'concolor', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (200, E'cow parsnip', NULL, E'Heracleum', E'maximum', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (201, E'crab', NULL, E'Cancer', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (202, E'crab apple', NULL, E'Malus', E'fusca', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (203, E'crab, Dungenous', NULL, E'Cancer', E'magister', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (204, E'cranberry', NULL, E'Viburnum', E'macrocarpon', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (205, E'currant', NULL, E'Ribes', E'spp.', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (206, E'deer', NULL, E'Odocoileus', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (207, E'dentalium', NULL, E'Dentalium', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (208, E'devil''s club', NULL, E'Oplopanaz', E'horridus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (209, E'Dolly Varden', NULL, E'Salvelinus', E'malma', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (210, E'duck', NULL, E'Anatidae', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (211, E'dune grass', NULL, E'Leymus', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (212, E'eel, California  moray', NULL, E'Gymnothorax ', E'mordax', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (213, E'eelgrass', NULL, E'Zostera', E'marina', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (214, E'elderberry, Blue', NULL, E'Sambucus', E'mexicana', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (215, E'elderberry, Red', NULL, E'Sambucus', E'racemosa', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (216, E'elk', NULL, E'Cervus', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (217, E'eulachon/ candlefish', NULL, E'Thalyicthes', E'pacificus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (218, E'false hellebore', NULL, E'Veratrum', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (219, E'false lily-of-the-valley', NULL, E'Maianthemum', E'dilatatum', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (220, E'fern', NULL, NULL, NULL, E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (221, E'fern, Braken', NULL, E'Pteridium', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (222, E'fern, Deer', NULL, E'Blechnum', E'spicant', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (223, E'fern, Lady', NULL, E'Athyrium', E'femina', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (224, E'fern, Licorice', NULL, E'Polypodium', E'glycyrrhiza', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (225, E'fern, Maidenhair', NULL, E'Adiantum', E'aleuticum', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (226, E'fern, Sword', NULL, E'Polystichum', E'munitum', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (227, E'fern, Wood', NULL, E'Dryopteris', E'spp.', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (228, E'fir', NULL, E'Abies', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (229, E'fir, Douglas', NULL, E'Pseudotsuga', E'menziesii', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (230, E'fish', NULL, NULL, NULL, E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (231, E'Flatfish; sole, flounder', NULL, E'Pleuronectidae, Bothidae', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (232, E'Flounder, starry', NULL, E'Plathichthys ', E'stellatus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (233, E'Geoduck', NULL, E'Panopea', E'generosa', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (234, E'goose', NULL, E'Anserini ', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (235, E'gooseberry', NULL, E'Ribes', E'divaricatum', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (236, E'Greenling, Kelp/sea trout', NULL, E'Hexagrammos ', E'decagrammus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (237, E'Greenling, Rock/sea trout', NULL, E'Hexagrammos ', E'superciliosus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (238, E'groundfish', NULL, NULL, NULL, E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (239, E'hagfish', NULL, E'Eptatretus ', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (240, E'halibut, California', NULL, E'Paralichthys ', E'californicus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (241, E'hedge nettle', NULL, E'Stachys', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (242, E'hemlock, Western', NULL, E'Tsuga', E'heterophylla', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (243, E'heron, Blue', NULL, E'Ardea', E'herodias', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (244, E'horsetail, Giant', NULL, E'Equisetum', E'telmateia', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (245, E'horsetail, Snakeheads', NULL, E'Equisetum', E'arvense', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (246, E'huckleberry, Blue/Black/Shotberry', NULL, E'Vaccinium', E'ovalifolium', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (247, E'huckleberry, Bog', NULL, E'Vaccinium', E'uliginosum', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (248, E'huckleberry, Red', NULL, E'Vaccinium', E'parvifolium', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (249, E'huckleberry, Winter evergreen', NULL, E'Vaccinium', E'ovatum', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (250, E'kelp', NULL, NULL, NULL, E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (251, E'kelp, Bull', NULL, E'Nereocystis ', E'luetkeana', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (252, E'kelp, Giant', NULL, E'Macrocystis ', E'pyrifera', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (253, E'kinnikinnick', NULL, E'Arctostaphylos', E'ursi', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (254, E'lamprey, Pacific/Eel', NULL, E'Lampetra', E'tridentatus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (255, E'lamprey, river', NULL, E'Lampetra', E'ayresi', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (256, E'lily, Tiger/Columbia', NULL, E'Lilium', E'columbianum', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (257, E'limpet', NULL, E'Lottia; Tectura', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (258, E'limpet, Ribbed', NULL, E'Lottia', E'digitalis', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (259, E'limpet, Shield', NULL, E'Lottia', E'pelta', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (260, E'lingcod', NULL, E'Ophiodon', E'elongatus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (261, E'loon', NULL, E'Gavia', E'immer', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (262, E'miner''s lettuce', NULL, E'Claytonia', E'spp.', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (263, E'mink', NULL, E'Mustela', E'vison', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (264, E'mussel', NULL, E'Mytilus', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (265, E'mussel, Bay/Blue', NULL, E'Mytilu', E'trossulus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (266, E'mussel, California', NULL, E'Mytilus', E'californianus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (267, E'nodding onion', NULL, E'Allium', E'cernuum', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (268, E'Northern anchovy', NULL, E'Engraulis', E'mordax', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (269, E'ocean spray ', NULL, E'Holodiscus', E'discolor', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (270, E'octopus', NULL, E'Octopus', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (271, E'olivella', NULL, E'Olivella', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (272, E'oso berry/ Indian plum', NULL, E'Oemlaeria', E'cerasiformis', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (273, E'otter, River', NULL, E'Lutra', E'canadensis', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (274, E'oyster  ', NULL, NULL, NULL, E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (275, E'oyster, Rock', NULL, E'Pododesmus', E'cepio', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (276, E'Pacific halibut', NULL, E'Hippoglossus', E'stenolepis', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (277, E'Pacific herring', NULL, E'Clupea', E'harengus pallasi', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (278, E'perch, Pacific Ocean', NULL, E'Sebastes', E'alutus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (279, E'periwinkle', NULL, E'Littorina', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (280, E'pine, Lodgepole', NULL, E'Pinus', E'contorta', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (281, E'pine, Western white', NULL, E'Pinus', E'monticola', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (282, E'rabbit', NULL, E'Sylvilagus', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (283, E'raccoon', NULL, E'Procyon', E'lotor', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (284, E'Red snapper', NULL, E'Sebastes', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (285, E'rockfish', NULL, E'Sebastes', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (286, E'rose', NULL, E'Rosa', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (287, E'rush, Scouring', NULL, E'Equisetum ', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (288, E'rushes', NULL, E'Juncus', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (289, E'sablefish/ black cod', NULL, E'Anoplopoma', E'fimbria', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (290, E'salal', NULL, E'Gaultheria', E'shallon', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (291, E'salmon, Chinook/King', NULL, E'Oncorhynchus ', E'tshawytscha', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (292, E'salmon, Chum/Dog', NULL, E'Oncorhynchus', E'keta', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (293, E'salmon, Coho/Silver', NULL, E'Oncorhynchus', E'kiscutch', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (294, E'salmon, Pink/ Humpback', NULL, E'Oncorhynchus', E'gorbuscha', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (295, E'salmon, Sockeye/Blueback', NULL, E'Oncorhynchus', E'nerka', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (296, E'salmonberry', NULL, E'Rubus', E'spectabilis', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (297, E'sanddab, Pacific', NULL, E'Citharichthys ', E'sordidus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (298, E'sanddollar', NULL, E'Dendraster', E'excentricus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (299, E'scallop', NULL, E'Chlamys', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (300, E'scallop, Rock', NULL, E'Hinnites', E'giganteus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (301, E'scallop, Weather vane', NULL, E'Pecten', E'caurinus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (302, E'sculpin, Pacific Staghorn/Bullhead', NULL, E'Leptocottus ', E'armatus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (303, E'sea anemone/rose', NULL, E'Anthopleura; Urticina; Epiactis; Cnidopus', E'sp,; sp.; prolifera; ritteri', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (304, E'sea bass, white', NULL, E'Cynoscion', E'nobilis', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (305, E'sea cucumber', NULL, E'Cucumaria; Stichopus; Eupentacta; Psolus; Psolidium', E' sp.; californicas; quinquesemita; chitonoides; bullatum', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (306, E'sea gull', NULL, E'Laridae', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (307, E'sea lion, California', NULL, E'Zalophus', E'californianus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (308, E'sea lion, Steller/ Northern', NULL, E'Eumetopias', E'jubatus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (309, E'Sea Palm', NULL, E'Postelsia ', E'palmaeformis', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (310, E'sea snail', NULL, NULL, NULL, E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (311, E'sea star', NULL, NULL, NULL, E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (312, E'sea urchin', NULL, E'Strongylocentrotus', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (313, E'seabass', NULL, E'Sebastes', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (314, E'seabirds', NULL, NULL, NULL, E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (315, E'seal', NULL, NULL, NULL, E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (316, E'seal, Fur', NULL, E'Callorhinus', E'ursinus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (317, E'seal, Northern elephant', NULL, E'Mirounga', E'angustirostris', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (318, E'seal, Pacific harbor', NULL, E'Phoca', E'vitulina', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (319, E'seaweed ', NULL, E'Porphyra', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (320, E'sedge, Slough', NULL, E'Carex', E'obnupta', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (321, E'sedges', NULL, E'Carex', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (322, E'shore grass', NULL, E'Distichlis', E'spicata', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (323, E'shrimp', NULL, E'Pandalus', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (324, E'skate', NULL, E'Raja', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (325, E'skunk cabbage', NULL, E'Lysichiton', E'americanus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (326, E'smelt', NULL, E'Osmeridae', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (327, E'smelt, Longfin', NULL, E'Spirinchus', E'thalyicthys', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (328, E'smelt, Night/nightfish', NULL, E'Spirinchus ', E'starski', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (329, E'smelt, Surf/surfish', NULL, E'Hypomesus ', E'pretiosus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (330, E'smelt, White bait', NULL, E'Allosmerus', E'elongatus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (331, E'snail', NULL, E'Gastipodia', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (332, E'soapberry', NULL, E'Shepherdia', E'canadensis', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (333, E'sole, Sand', NULL, E'Psettichthys ', E'melanostictus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (334, E'spruce', NULL, E'Picea', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (335, E'spruce, Sitka', NULL, E'Picea', E'sitchensis', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (336, E'squid, Humboldt', NULL, E'Dosidicus', E'gigas', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (337, E'squid, Pacific/opalescent/market', NULL, E'Loligo', E'opalescens', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (338, E'steelhead', NULL, E'Oncorhynchus', E'mykiss', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (339, E'stinging nettle/ gen. nettle', NULL, E'Urtica', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (340, E'strawberry', NULL, E'Fragaria', E'chiloensis', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (341, E'sturgeon, green', NULL, E'Acipenser', E'medirostris', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (342, E'sturgeon, White', NULL, E'Acipenser', E'transmontanus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (343, E'surfgrass, Scouler''s', NULL, E'Phyllospadix', E'scouleri', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (344, E'surfgrass, Serrated', NULL, E'Phyllospadix', E'serrulatus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (345, E'surfgrass, Torrey''s', NULL, E'Phyllospadix', E'torreyi', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (346, E'surfgrasses', NULL, E'Phyllospadix', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (347, E'surfperch', NULL, E'Embiotocidae', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (348, E'surfperch, Black', NULL, E'Embiotoca ', E'jacksoni', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (349, E'surfperch, Calico', NULL, E'Amphistichus ', E'koelzi', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (350, E'surfperch, Pile', NULL, E'Damalichthys ', E'vacca', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (351, E'surfperch, Rainbow', NULL, E'Hypsurus ', E'caryi', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (352, E'surfperch, Redtail', NULL, E'Amphistichus ', E'rhodoterus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (353, E'surfperch, Rubberlip', NULL, E'Rhacochilus ', E'toxotes', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (354, E'surfperch, Shiner', NULL, E'Cymatogaster ', E'aggregata', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (355, E'surfperch, Striped', NULL, E'Embiotoca ', E'lateralis', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (356, E'surfperch, Walleye', NULL, E'Hyperprosopon ', E'argenteum', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (357, E'surfperch, White', NULL, E'Phanerodon ', E'furcatus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (358, E'sweet grass', NULL, E'Hierochloe', E'spp', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (359, E'tea, Labrador', NULL, E'Ledum', E'groenlandicum', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (360, E'thimbleberry', NULL, E'Rubus', E'parviflorus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (361, E'thistle', NULL, E'Cirsium', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (362, E'trout, Cutthroat/Sea trout', NULL, E'Salmo', E'clarki clarki', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (363, E'tubesnouts', NULL, E'Procellariiformes', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (364, E'turtle', NULL, NULL, NULL, E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (365, E'vine maple', NULL, E'Acer', E'circinatum', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (366, E'wapato/ arrowhead', NULL, E'Sagittaria', E'latifolia', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (367, E'water lilies', NULL, E'Nuphar', E'polysepalum', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (368, E'western pearlshell', NULL, E'Margaritifera', E'falcata', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (369, E'whale', NULL, NULL, NULL, E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (370, E'whale, Blue', NULL, E'Blaenoptera', E'musculus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (371, E'whale, Fin', NULL, E'Balaenoptera', E'physalus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (372, E'whale, Gray', NULL, E'Eschrichtius', E'robustus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (373, E'whale, Humpback', NULL, E'Megaptera', E'novaeangliae', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (374, E'whale, Killer', NULL, E'Orcinus', E'orca', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (375, E'whale, Minke', NULL, E'Balaenoptera', E'acutorostrata', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (376, E'whale, Right', NULL, E'Eubalaena', E'japonica', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (377, E'whale, Sperm', NULL, E'Physeter', E'macrocephalus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (378, E'whelk', NULL, E'Nassarius', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (379, E'whiting, Pacific/Pacific hake', NULL, E'Merluccius ', E'productus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (380, E'wild cherry', NULL, E'Prunus', E'emarginata', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (381, E'wild cranberry', NULL, E'Viburnum', E'oxycoccos', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (382, E'wild rye', NULL, E'Elymus', E'spp.', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (383, E'willow', NULL, E'Salix', E'sp.', E'0', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (384, E'wolf  ', NULL, E'Canis', E'lupus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (385, E'Wolf eel', NULL, E'Anarrhichthys ', E'ocellatus', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "Resources" ("ResourceID", "CommonName", "IndigenousName", "Genus", "Species", "Specific", "ResourceClassificationGroup", "IsLocked", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") VALUES (386, E'yarrow', NULL, E'Achillea', E'millefolium', E'1', NULL, E'0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
-- 237 records

SELECT setval('"Resources_ResourceID_seq"', MAX("ResourceID")) FROM "Resources";

CREATE INDEX "Resources_SpeciesID" ON "Resources" ("ResourceID");

--
-- Table structure for table 'ResourcesActivityEvents'
--

DROP TABLE IF EXISTS "ResourcesActivityEvents";

CREATE TABLE "ResourcesActivityEvents" (
  "ResourceActivityID" SERIAL NOT NULL, 
  "PlaceResourceID" INTEGER NOT NULL, 
  "RelationshipDescription" TEXT, 
  "PartUsed" VARCHAR(255), 
  "ActivityShortDescription" VARCHAR(255), 
  "ActivityLongDescription" TEXT, 
  "Participants" VARCHAR(50), 
  "Technique" VARCHAR(255), 
  "Gear" VARCHAR(255), 
  "CustomaryUse" VARCHAR(255), 
  "Timing" VARCHAR(255), 
  "TimingDescription" VARCHAR(255), 
  "IsLocked" BOOLEAN DEFAULT E'0', 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("ResourceActivityID")
);

--
-- Dumping data for table 'ResourcesActivityEvents'
--

-- 0 records

SELECT setval('"ResourcesActivityEvents_ResourceActivityID_seq"', MAX("ResourceActivityID")) FROM "ResourcesActivityEvents";

CREATE INDEX "ResourcesActivityEvents_ResourceActivityID" ON "ResourcesActivityEvents" ("ResourceActivityID");

CREATE INDEX "ResourcesActivityEvents_ResourcesActivityEventsPlaceResourceID" ON "ResourcesActivityEvents" ("PlaceResourceID");

--
-- Table structure for table 'ResourcesCitationEvents'
--

DROP TABLE IF EXISTS "ResourcesCitationEvents";

CREATE TABLE "ResourcesCitationEvents" (
  "ResourceID" INTEGER NOT NULL, 
  "CitationID" INTEGER NOT NULL, 
  "RelationshipDescription" VARCHAR(255), 
  "Pages" VARCHAR(255), 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("ResourceID", "CitationID")
);

--
-- Dumping data for table 'ResourcesCitationEvents'
--

-- 0 records

CREATE INDEX "ResourcesCitationEvents_PlaceID" ON "ResourcesCitationEvents" ("ResourceID");

CREATE INDEX "ResourcesCitationEvents_SpeciesID" ON "ResourcesCitationEvents" ("CitationID");

--
-- Table structure for table 'ResourcesMediaEvents'
--

DROP TABLE IF EXISTS "ResourcesMediaEvents";

CREATE TABLE "ResourcesMediaEvents" (
  "ResourceID" INTEGER NOT NULL, 
  "MediaID" INTEGER NOT NULL, 
  "RelationshipDescription" VARCHAR(255), 
  "Pages" VARCHAR(50), 
  "EnteredByName" VARCHAR(25), 
  "EnteredByTribe" VARCHAR(100), 
  "EnteredByTitle" VARCHAR(100), 
  "EnteredByDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  "ModifiedByName" VARCHAR(25), 
  "ModifiedByTitle" VARCHAR(100), 
  "ModifiedByTribe" VARCHAR(100), 
  "ModifiedByDate" TIMESTAMP, 
  PRIMARY KEY ("ResourceID", "MediaID")
);

--
-- Dumping data for table 'ResourcesMediaEvents'
--

-- 0 records

CREATE INDEX "ResourcesMediaEvents_PlaceID" ON "ResourcesMediaEvents" ("ResourceID");

CREATE INDEX "ResourcesMediaEvents_SpeciesID" ON "ResourcesMediaEvents" ("MediaID");

--
-- Table structure for table 'UserAccess'
--

DROP TABLE IF EXISTS "UserAccess";

CREATE TABLE "UserAccess" (
  "AccessID" SERIAL NOT NULL, 
  "AccessLevel" VARCHAR(255), 
  PRIMARY KEY ("AccessID")
);

--
-- Dumping data for table 'UserAccess'
--

INSERT INTO "UserAccess" ("AccessID", "AccessLevel") VALUES (1, E'Administrator');
INSERT INTO "UserAccess" ("AccessID", "AccessLevel") VALUES (2, E'Editor');
INSERT INTO "UserAccess" ("AccessID", "AccessLevel") VALUES (3, E'Reader');
-- 3 records

SELECT setval('"UserAccess_AccessID_seq"', MAX("AccessID")) FROM "UserAccess";

CREATE INDEX "UserAccess_AccessID" ON "UserAccess" ("AccessID");

--
-- Table structure for table 'Users'
--

DROP TABLE IF EXISTS "Users";

CREATE TABLE "Users" (
  "UserID" SERIAL NOT NULL, 
  "UserName" VARCHAR(20) NOT NULL, 
  "Password" VARCHAR(20) NOT NULL, 
  "FirstName" VARCHAR(255) NOT NULL, 
  "LastName" VARCHAR(255) NOT NULL, 
  "Affiliation" VARCHAR(255) NOT NULL, 
  "Title" VARCHAR(255) NOT NULL, 
  "AccessLevel" INTEGER NOT NULL, 
  PRIMARY KEY ("UserID")
);

--
-- Dumping data for table 'Users'
--

INSERT INTO "Users" ("UserID", "UserName", "Password", "FirstName", "LastName", "Affiliation", "Title", "AccessLevel") VALUES (5, E'admin', E'admin', E'Admin', E'Administrator', E'General Admin', E'Admin', 1);
INSERT INTO "Users" ("UserID", "UserName", "Password", "FirstName", "LastName", "Affiliation", "Title", "AccessLevel") VALUES (6, E'editor', E'editor', E'Editor', E'Editor', E'General Admin', E'Editor', 2);
INSERT INTO "Users" ("UserID", "UserName", "Password", "FirstName", "LastName", "Affiliation", "Title", "AccessLevel") VALUES (7, E'readonly', E'readonly', E'Read', E'Only', E'General Access', E'Mr. Reader', 3);
-- 3 records

SELECT setval('"Users_UserID_seq"', MAX("UserID")) FROM "Users";

CREATE INDEX "Users_UserID" ON "Users" ("UserID");

