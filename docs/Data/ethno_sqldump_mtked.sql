#
# DUMP FILE
#
# Database is ported from MS Access
#------------------------------------------------------------------
# Created using "MS Access to MySQL" form http://www.bullzip.com
# Program Version 5.4.274
#
# OPTIONS:
#   sourcefilename=C:\Users\mridul\Desktop\EcotrustBackup\DummyData\MTKED Database\backend\db\ethnographic_elements_be.accdb
#   sourceusername=
#   sourcepassword=
#   sourcesystemdatabase=
#   destinationdatabase=ethnographic_elements_be
#   storageengine=MyISAM
#   dropdatabase=0
#   createtables=1
#   unicode=1
#   autocommit=1
#   transferdefaultvalues=1
#   transferindexes=1
#   transferautonumbers=1
#   transferrecords=1
#   columnlist=1
#   tableprefix=
#   negativeboolean=0
#   ignorelargeblobs=0
#   memotype=LONGTEXT
#   datetimetype=DATETIME
#

CREATE DATABASE IF NOT EXISTS `ethnographic_elements_be`;
USE `ethnographic_elements_be`;

#
# Table structure for table 'Citations'
#

DROP TABLE IF EXISTS `Citations`;

CREATE TABLE `Citations` (
  `CitationID` INTEGER NOT NULL AUTO_INCREMENT, 
  `ReferenceType` VARCHAR(255), 
  `ReferenceText` VARCHAR(50), 
  `AuthorType` VARCHAR(255), 
  `AuthorPrimary` VARCHAR(255), 
  `AuthorSecondary` VARCHAR(255), 
  `IntervieweeID` INTEGER, 
  `InterviewerID` INTEGER, 
  `PlaceofInterview` VARCHAR(255), 
  `Year` INTEGER, 
  `Title` LONGTEXT, 
  `SeriesTitle` VARCHAR(255), 
  `SeriesVolume` VARCHAR(50), 
  `SeriesEditor` VARCHAR(255), 
  `Publisher` VARCHAR(100), 
  `PublisherCity` VARCHAR(255), 
  `PreparedFor` VARCHAR(100), 
  `Comments` LONGTEXT, 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  INDEX (`CitationID`), 
  INDEX (`InterviewerID`), 
  PRIMARY KEY (`CitationID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'Citations'
#

INSERT INTO `Citations` (`CitationID`, `ReferenceType`, `ReferenceText`, `AuthorType`, `AuthorPrimary`, `AuthorSecondary`, `IntervieweeID`, `InterviewerID`, `PlaceofInterview`, `Year`, `Title`, `SeriesTitle`, `SeriesVolume`, `SeriesEditor`, `Publisher`, `PublisherCity`, `PreparedFor`, `Comments`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (11, 'Book', 'Text on marine flora and fauna', NULL, 'Tanner, J.J.', NULL, NULL, NULL, NULL, 2017, 'Traditional Marine Harvesting of Native Americans', NULL, NULL, NULL, 'Si~s-xa Publishing', 'Smith River', NULL, 'Text on flora and fauna harvested by Native Americans in the marine environment', 'admin', 'General Admin', 'Admin', '2017-03-20 14:23:22', 'admin', 'Admin', 'General Admin', '2017-03-20 14:30:47');
INSERT INTO `Citations` (`CitationID`, `ReferenceType`, `ReferenceText`, `AuthorType`, `AuthorPrimary`, `AuthorSecondary`, `IntervieweeID`, `InterviewerID`, `PlaceofInterview`, `Year`, `Title`, `SeriesTitle`, `SeriesVolume`, `SeriesEditor`, `Publisher`, `PublisherCity`, `PreparedFor`, `Comments`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (12, 'Interview', 'Ethnographic Interview', NULL, NULL, NULL, 6, 7, 'TDN Natural Resources Office', 2016, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Interview regarding marine harvesting', 'admin', 'General Admin', 'Admin', '2017-03-20 14:31:12', 'admin', 'Admin', 'General Admin', '2017-03-20 14:39:36');
# 2 records

#
# Table structure for table 'CurrentVersion'
#

DROP TABLE IF EXISTS `CurrentVersion`;

CREATE TABLE `CurrentVersion` (
  `ID` INTEGER NOT NULL AUTO_INCREMENT, 
  `BackendVersion` INTEGER, 
  `FrontendVersion` INTEGER, 
  PRIMARY KEY (`ID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'CurrentVersion'
#

INSERT INTO `CurrentVersion` (`ID`, `BackendVersion`, `FrontendVersion`) VALUES (1, 1, 1);
# 1 records

#
# Table structure for table 'Locality'
#

DROP TABLE IF EXISTS `Locality`;

CREATE TABLE `Locality` (
  `LocalityID` INTEGER NOT NULL AUTO_INCREMENT, 
  `PlaceID` INTEGER, 
  `EnglishName` VARCHAR(255), 
  `IndigenousName` VARCHAR(255), 
  `LocalityType` VARCHAR(255), 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  INDEX (`LocalityID`), 
  INDEX (`PlaceID`), 
  PRIMARY KEY (`LocalityID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'Locality'
#

# 0 records

#
# Table structure for table 'LocalityGISSelections'
#

DROP TABLE IF EXISTS `LocalityGISSelections`;

CREATE TABLE `LocalityGISSelections` (
  `LocalityID` INTEGER, 
  `LocalityLabel` VARCHAR(255), 
  `SourceFC` VARCHAR(255)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LocalityGISSelections'
#

# 0 records

#
# Table structure for table 'LocalityPlaceResourceEvent'
#

DROP TABLE IF EXISTS `LocalityPlaceResourceEvent`;

CREATE TABLE `LocalityPlaceResourceEvent` (
  `PlaceResourceID` INTEGER NOT NULL, 
  `LocalityID` INTEGER NOT NULL, 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  INDEX (`LocalityID`), 
  INDEX (`PlaceResourceID`), 
  PRIMARY KEY (`PlaceResourceID`, `LocalityID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LocalityPlaceResourceEvent'
#

# 0 records

#
# Table structure for table 'LookupActivity'
#

DROP TABLE IF EXISTS `LookupActivity`;

CREATE TABLE `LookupActivity` (
  `Activity` VARCHAR(255) NOT NULL, 
  PRIMARY KEY (`Activity`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupActivity'
#

INSERT INTO `LookupActivity` (`Activity`) VALUES ('Cemetery');
INSERT INTO `LookupActivity` (`Activity`) VALUES ('Customary Fishing and Gathering from Shore');
INSERT INTO `LookupActivity` (`Activity`) VALUES ('Customary Fishing and Gathering Offshore');
INSERT INTO `LookupActivity` (`Activity`) VALUES ('Customary Hunting from Shore');
INSERT INTO `LookupActivity` (`Activity`) VALUES ('Customary Hunting Offshore');
INSERT INTO `LookupActivity` (`Activity`) VALUES ('Processing');
INSERT INTO `LookupActivity` (`Activity`) VALUES ('Related to Ceremony');
INSERT INTO `LookupActivity` (`Activity`) VALUES ('Related to Song');
INSERT INTO `LookupActivity` (`Activity`) VALUES ('Related to Story');
INSERT INTO `LookupActivity` (`Activity`) VALUES ('Residence/Village');
INSERT INTO `LookupActivity` (`Activity`) VALUES ('Training');
# 11 records

#
# Table structure for table 'LookupAuthorType'
#

DROP TABLE IF EXISTS `LookupAuthorType`;

CREATE TABLE `LookupAuthorType` (
  `AuthorType` VARCHAR(50) NOT NULL, 
  PRIMARY KEY (`AuthorType`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupAuthorType'
#

INSERT INTO `LookupAuthorType` (`AuthorType`) VALUES ('Author');
INSERT INTO `LookupAuthorType` (`AuthorType`) VALUES ('Corporate Author');
INSERT INTO `LookupAuthorType` (`AuthorType`) VALUES ('Editor');
# 3 records

#
# Table structure for table 'LookupCustomaryUse'
#

DROP TABLE IF EXISTS `LookupCustomaryUse`;

CREATE TABLE `LookupCustomaryUse` (
  `UsedFor` VARCHAR(255) NOT NULL, 
  PRIMARY KEY (`UsedFor`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupCustomaryUse'
#

INSERT INTO `LookupCustomaryUse` (`UsedFor`) VALUES ('Barter');
INSERT INTO `LookupCustomaryUse` (`UsedFor`) VALUES ('Ceremony');
INSERT INTO `LookupCustomaryUse` (`UsedFor`) VALUES ('Food');
INSERT INTO `LookupCustomaryUse` (`UsedFor`) VALUES ('Regalia');
INSERT INTO `LookupCustomaryUse` (`UsedFor`) VALUES ('Song');
INSERT INTO `LookupCustomaryUse` (`UsedFor`) VALUES ('Story');
INSERT INTO `LookupCustomaryUse` (`UsedFor`) VALUES ('Tool');
# 7 records

#
# Table structure for table 'LookupHabitat'
#

DROP TABLE IF EXISTS `LookupHabitat`;

CREATE TABLE `LookupHabitat` (
  `Habitat` VARCHAR(100) NOT NULL, 
  INDEX (`Habitat`), 
  PRIMARY KEY (`Habitat`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupHabitat'
#

INSERT INTO `LookupHabitat` (`Habitat`) VALUES ('Coastal Marsh');
INSERT INTO `LookupHabitat` (`Habitat`) VALUES ('Deep Canyon');
INSERT INTO `LookupHabitat` (`Habitat`) VALUES ('Estuary');
INSERT INTO `LookupHabitat` (`Habitat`) VALUES ('Hard-bottom >100m');
INSERT INTO `LookupHabitat` (`Habitat`) VALUES ('Hard-bottom 0-100m');
INSERT INTO `LookupHabitat` (`Habitat`) VALUES ('Offshore Reefs');
INSERT INTO `LookupHabitat` (`Habitat`) VALUES ('Offshore Rock');
INSERT INTO `LookupHabitat` (`Habitat`) VALUES ('Rocky Intertidal');
INSERT INTO `LookupHabitat` (`Habitat`) VALUES ('Sandy Beach');
INSERT INTO `LookupHabitat` (`Habitat`) VALUES ('Soft-bottom >100m');
INSERT INTO `LookupHabitat` (`Habitat`) VALUES ('Soft-bottom 0-100m');
INSERT INTO `LookupHabitat` (`Habitat`) VALUES ('Tidal Flats');
# 12 records

#
# Table structure for table 'LookupLocalityType'
#

DROP TABLE IF EXISTS `LookupLocalityType`;

CREATE TABLE `LookupLocalityType` (
  `LocalityType` VARCHAR(255) NOT NULL, 
  PRIMARY KEY (`LocalityType`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupLocalityType'
#

INSERT INTO `LookupLocalityType` (`LocalityType`) VALUES ('bay');
INSERT INTO `LookupLocalityType` (`LocalityType`) VALUES ('beach');
INSERT INTO `LookupLocalityType` (`LocalityType`) VALUES ('creek');
INSERT INTO `LookupLocalityType` (`LocalityType`) VALUES ('estuary');
INSERT INTO `LookupLocalityType` (`LocalityType`) VALUES ('intertidal');
INSERT INTO `LookupLocalityType` (`LocalityType`) VALUES ('lagoon');
INSERT INTO `LookupLocalityType` (`LocalityType`) VALUES ('mainstem river');
INSERT INTO `LookupLocalityType` (`LocalityType`) VALUES ('offshore rocks');
INSERT INTO `LookupLocalityType` (`LocalityType`) VALUES ('open ocean');
INSERT INTO `LookupLocalityType` (`LocalityType`) VALUES ('river eddy');
INSERT INTO `LookupLocalityType` (`LocalityType`) VALUES ('river mouth');
INSERT INTO `LookupLocalityType` (`LocalityType`) VALUES ('side channel river');
INSERT INTO `LookupLocalityType` (`LocalityType`) VALUES ('subtidal');
# 13 records

#
# Table structure for table 'LookupMediaType'
#

DROP TABLE IF EXISTS `LookupMediaType`;

CREATE TABLE `LookupMediaType` (
  `MediaType` VARCHAR(255) NOT NULL, 
  `MediaCategory` VARCHAR(255), 
  PRIMARY KEY (`MediaType`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupMediaType'
#

INSERT INTO `LookupMediaType` (`MediaType`, `MediaCategory`) VALUES ('audio', NULL);
INSERT INTO `LookupMediaType` (`MediaType`, `MediaCategory`) VALUES ('image', NULL);
INSERT INTO `LookupMediaType` (`MediaType`, `MediaCategory`) VALUES ('other', NULL);
INSERT INTO `LookupMediaType` (`MediaType`, `MediaCategory`) VALUES ('PDF', NULL);
INSERT INTO `LookupMediaType` (`MediaType`, `MediaCategory`) VALUES ('video', NULL);
# 5 records

#
# Table structure for table 'LookupParticipants'
#

DROP TABLE IF EXISTS `LookupParticipants`;

CREATE TABLE `LookupParticipants` (
  `Participants` VARCHAR(255) NOT NULL, 
  PRIMARY KEY (`Participants`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupParticipants'
#

INSERT INTO `LookupParticipants` (`Participants`) VALUES ('Children');
INSERT INTO `LookupParticipants` (`Participants`) VALUES ('Children-boys');
INSERT INTO `LookupParticipants` (`Participants`) VALUES ('Children-girls');
INSERT INTO `LookupParticipants` (`Participants`) VALUES ('Everyone');
INSERT INTO `LookupParticipants` (`Participants`) VALUES ('Men');
INSERT INTO `LookupParticipants` (`Participants`) VALUES ('Other beings');
INSERT INTO `LookupParticipants` (`Participants`) VALUES ('Women');
# 7 records

#
# Table structure for table 'LookupPartUsed'
#

DROP TABLE IF EXISTS `LookupPartUsed`;

CREATE TABLE `LookupPartUsed` (
  `PartUsed` VARCHAR(255) NOT NULL, 
  PRIMARY KEY (`PartUsed`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupPartUsed'
#

INSERT INTO `LookupPartUsed` (`PartUsed`) VALUES ('Antler');
INSERT INTO `LookupPartUsed` (`PartUsed`) VALUES ('Bone');
INSERT INTO `LookupPartUsed` (`PartUsed`) VALUES ('Egg');
INSERT INTO `LookupPartUsed` (`PartUsed`) VALUES ('Feather');
INSERT INTO `LookupPartUsed` (`PartUsed`) VALUES ('Flower');
INSERT INTO `LookupPartUsed` (`PartUsed`) VALUES ('Meat');
INSERT INTO `LookupPartUsed` (`PartUsed`) VALUES ('Shell');
INSERT INTO `LookupPartUsed` (`PartUsed`) VALUES ('Tooth');
INSERT INTO `LookupPartUsed` (`PartUsed`) VALUES ('Whisker');
# 9 records

#
# Table structure for table 'LookupPlanningUnit'
#

DROP TABLE IF EXISTS `LookupPlanningUnit`;

CREATE TABLE `LookupPlanningUnit` (
  `PlanningUnitID` INTEGER NOT NULL, 
  `PlanningUnitName` VARCHAR(100), 
  INDEX (`PlanningUnitID`), 
  PRIMARY KEY (`PlanningUnitID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupPlanningUnit'
#

INSERT INTO `LookupPlanningUnit` (`PlanningUnitID`, `PlanningUnitName`) VALUES (0, 'Undefined');
INSERT INTO `LookupPlanningUnit` (`PlanningUnitID`, `PlanningUnitName`) VALUES (1, 'Southern');
INSERT INTO `LookupPlanningUnit` (`PlanningUnitID`, `PlanningUnitName`) VALUES (2, 'Northern');
INSERT INTO `LookupPlanningUnit` (`PlanningUnitID`, `PlanningUnitName`) VALUES (3, 'Middle');
# 4 records

#
# Table structure for table 'LookupReferenceType'
#

DROP TABLE IF EXISTS `LookupReferenceType`;

CREATE TABLE `LookupReferenceType` (
  `DocumentType` VARCHAR(25) NOT NULL, 
  PRIMARY KEY (`DocumentType`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupReferenceType'
#

INSERT INTO `LookupReferenceType` (`DocumentType`) VALUES ('Book');
INSERT INTO `LookupReferenceType` (`DocumentType`) VALUES ('Other');
INSERT INTO `LookupReferenceType` (`DocumentType`) VALUES ('Edited Volume');
INSERT INTO `LookupReferenceType` (`DocumentType`) VALUES ('Interview');
# 4 records

#
# Table structure for table 'LookupResourceGroup'
#

DROP TABLE IF EXISTS `LookupResourceGroup`;

CREATE TABLE `LookupResourceGroup` (
  `ResourceClassificationGroup` VARCHAR(255) NOT NULL, 
  PRIMARY KEY (`ResourceClassificationGroup`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupResourceGroup'
#

INSERT INTO `LookupResourceGroup` (`ResourceClassificationGroup`) VALUES ('anadromous finfish');
INSERT INTO `LookupResourceGroup` (`ResourceClassificationGroup`) VALUES ('bird');
INSERT INTO `LookupResourceGroup` (`ResourceClassificationGroup`) VALUES ('coastal watershed mammal');
INSERT INTO `LookupResourceGroup` (`ResourceClassificationGroup`) VALUES ('crustacean');
INSERT INTO `LookupResourceGroup` (`ResourceClassificationGroup`) VALUES ('fern & relative');
INSERT INTO `LookupResourceGroup` (`ResourceClassificationGroup`) VALUES ('flowering plant');
INSERT INTO `LookupResourceGroup` (`ResourceClassificationGroup`) VALUES ('invertebrate');
INSERT INTO `LookupResourceGroup` (`ResourceClassificationGroup`) VALUES ('marine finfish');
INSERT INTO `LookupResourceGroup` (`ResourceClassificationGroup`) VALUES ('marine mammal');
INSERT INTO `LookupResourceGroup` (`ResourceClassificationGroup`) VALUES ('mollusk');
INSERT INTO `LookupResourceGroup` (`ResourceClassificationGroup`) VALUES ('seaweed/algae');
INSERT INTO `LookupResourceGroup` (`ResourceClassificationGroup`) VALUES ('tree');
# 12 records

#
# Table structure for table 'LookupSeason'
#

DROP TABLE IF EXISTS `LookupSeason`;

CREATE TABLE `LookupSeason` (
  `Season` VARCHAR(255) NOT NULL, 
  PRIMARY KEY (`Season`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupSeason'
#

INSERT INTO `LookupSeason` (`Season`) VALUES ('All');
INSERT INTO `LookupSeason` (`Season`) VALUES ('Fall');
INSERT INTO `LookupSeason` (`Season`) VALUES ('Fall/Winter');
INSERT INTO `LookupSeason` (`Season`) VALUES ('Spring');
INSERT INTO `LookupSeason` (`Season`) VALUES ('Spring/Summer');
INSERT INTO `LookupSeason` (`Season`) VALUES ('Summer');
INSERT INTO `LookupSeason` (`Season`) VALUES ('Summer/Fall');
INSERT INTO `LookupSeason` (`Season`) VALUES ('Winter');
INSERT INTO `LookupSeason` (`Season`) VALUES ('Winter/Spring');
# 9 records

#
# Table structure for table 'LookupTechniques'
#

DROP TABLE IF EXISTS `LookupTechniques`;

CREATE TABLE `LookupTechniques` (
  `Techniques` VARCHAR(255) NOT NULL, 
  PRIMARY KEY (`Techniques`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupTechniques'
#

INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('A-frame net');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('canoe');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('club');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('conical basket');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('dip net');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('eel basket');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('eel hook');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('gaff hook');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('gill net');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('hand fishing');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('hand gathered');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('harpoon');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('hook and line');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('net');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('poison');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('seine');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('snare');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('spears with detachable points');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('spears without detachable points');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('V-frame scoop net');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('V-shaped/converging weir');
INSERT INTO `LookupTechniques` (`Techniques`) VALUES ('weir/fish dam');
# 22 records

#
# Table structure for table 'LookupTiming'
#

DROP TABLE IF EXISTS `LookupTiming`;

CREATE TABLE `LookupTiming` (
  `Timing` VARCHAR(255) NOT NULL, 
  PRIMARY KEY (`Timing`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupTiming'
#

INSERT INTO `LookupTiming` (`Timing`) VALUES ('Daytime');
INSERT INTO `LookupTiming` (`Timing`) VALUES ('Evening');
INSERT INTO `LookupTiming` (`Timing`) VALUES ('Fall');
INSERT INTO `LookupTiming` (`Timing`) VALUES ('Morning');
INSERT INTO `LookupTiming` (`Timing`) VALUES ('Night');
INSERT INTO `LookupTiming` (`Timing`) VALUES ('Seasonal');
INSERT INTO `LookupTiming` (`Timing`) VALUES ('Spring');
INSERT INTO `LookupTiming` (`Timing`) VALUES ('Summer');
INSERT INTO `LookupTiming` (`Timing`) VALUES ('Winter');
# 9 records

#
# Table structure for table 'LookupTribe'
#

DROP TABLE IF EXISTS `LookupTribe`;

CREATE TABLE `LookupTribe` (
  `ID` INTEGER NOT NULL AUTO_INCREMENT, 
  `TribeUnit` VARCHAR(50), 
  `Tribe` VARCHAR(100), 
  `FederalTribe` VARCHAR(100), 
  PRIMARY KEY (`ID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupTribe'
#

INSERT INTO `LookupTribe` (`ID`, `TribeUnit`, `Tribe`, `FederalTribe`) VALUES (1, 'Tolowa Dee-ni’', 'Tolowa', 'Smith River Rancheria');
# 1 records

#
# Table structure for table 'LookupUserInfo'
#

DROP TABLE IF EXISTS `LookupUserInfo`;

CREATE TABLE `LookupUserInfo` (
  `UserName` VARCHAR(100), 
  `UsingCustomUsername` TINYINT(1) DEFAULT 0, 
  `UserTitle` VARCHAR(100), 
  `UserAffiliation` VARCHAR(100)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'LookupUserInfo'
#

INSERT INTO `LookupUserInfo` (`UserName`, `UsingCustomUsername`, `UserTitle`, `UserAffiliation`) VALUES ('gary', 0, 'gis', 'fw');
# 1 records

#
# Table structure for table 'Media'
#

DROP TABLE IF EXISTS `Media`;

CREATE TABLE `Media` (
  `MediaID` INTEGER NOT NULL AUTO_INCREMENT, 
  `MediaType` VARCHAR(255), 
  `MediaName` VARCHAR(255), 
  `MediaDescription` LONGTEXT, 
  `MediaLink` VARCHAR(255), 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  INDEX (`MediaID`), 
  PRIMARY KEY (`MediaID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'Media'
#

INSERT INTO `Media` (`MediaID`, `MediaType`, `MediaName`, `MediaDescription`, `MediaLink`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (6, 'image', 'Chiton Photo', 'Photo taken by Manaha Herman, 2015', 'C:\\Users\\rosa.laucci\\MTKED Database\\Media\\IMG_3996.JPG', 'admin', 'General Admin', 'Admin', '2017-03-20 15:12:46', 'admin', 'Admin', 'General Admin', '2017-03-20 15:13:36');
INSERT INTO `Media` (`MediaID`, `MediaType`, `MediaName`, `MediaDescription`, `MediaLink`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (7, 'image', 'Mussel Photo', 'Photo taken by Manaha Herman, 2014', 'C:\\Users\\rosa.laucci\\MTKED Database\\Media\\IMG_0470.JPG', 'admin', 'General Admin', 'Admin', '2017-03-20 15:13:45', 'admin', 'Admin', 'General Admin', '2017-03-20 15:14:32');
INSERT INTO `Media` (`MediaID`, `MediaType`, `MediaName`, `MediaDescription`, `MediaLink`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (8, 'image', 'Perch Photo', 'Photo taken by Manahe Herman, 2004', 'C:\\Users\\rosa.laucci\\MTKED Database\\Media\\IMGP0344.JPG', 'admin', 'General Admin', 'Admin', '2017-03-20 15:14:37', 'admin', 'Admin', 'General Admin', '2017-03-20 15:15:18');
INSERT INTO `Media` (`MediaID`, `MediaType`, `MediaName`, `MediaDescription`, `MediaLink`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (9, 'PDF', 'Jay Tosanic Interview Transcript', 'Interview transcript for Jay Tosanic on marine havesting  from 2016', 'C:\\Users\\rosa.laucci\\MTKED Database\\Media\\giant_devil_ray_st_factsheet.pdf', 'admin', 'General Admin', 'Admin', '2017-03-20 15:15:26', 'admin', 'Admin', 'General Admin', '2017-03-20 15:17:51');
# 4 records

#
# Table structure for table 'MediaCitationEvents'
#

DROP TABLE IF EXISTS `MediaCitationEvents`;

CREATE TABLE `MediaCitationEvents` (
  `MediaID` INTEGER NOT NULL, 
  `CitationID` INTEGER NOT NULL, 
  `RelationshipDescription` VARCHAR(255), 
  `Pages` VARCHAR(255), 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  INDEX (`MediaID`), 
  PRIMARY KEY (`MediaID`, `CitationID`), 
  INDEX (`CitationID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'MediaCitationEvents'
#

INSERT INTO `MediaCitationEvents` (`MediaID`, `CitationID`, `RelationshipDescription`, `Pages`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (9, 12, NULL, NULL, 'admin', 'General Admin', 'Admin', '2017-03-20 15:17:29', 'admin', 'Admin', 'General Admin', '2017-03-20 15:17:33');
# 1 records

#
# Table structure for table 'People'
#

DROP TABLE IF EXISTS `People`;

CREATE TABLE `People` (
  `PersonID` INTEGER NOT NULL AUTO_INCREMENT, 
  `FirstName` VARCHAR(255), 
  `LastName` VARCHAR(255), 
  `YearBorn` INTEGER, 
  `Village` VARCHAR(255), 
  `RelationshipToOtherPeople` LONGTEXT, 
  INDEX (`PersonID`), 
  PRIMARY KEY (`PersonID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'People'
#

INSERT INTO `People` (`PersonID`, `FirstName`, `LastName`, `YearBorn`, `Village`, `RelationshipToOtherPeople`) VALUES (6, 'Jay', 'Tosanic', 1978, 'T\'uu-yaa~-sdvm-dvn', 'Cheryl Tosanic, mother');
INSERT INTO `People` (`PersonID`, `FirstName`, `LastName`, `YearBorn`, `Village`, `RelationshipToOtherPeople`) VALUES (7, 'Manahe', 'Herman', 1978, 'None', NULL);
# 2 records

#
# Table structure for table 'PlaceAltIndigenousName'
#

DROP TABLE IF EXISTS `PlaceAltIndigenousName`;

CREATE TABLE `PlaceAltIndigenousName` (
  `AltIndigenousNameID` INTEGER NOT NULL AUTO_INCREMENT, 
  `PlaceID` INTEGER, 
  `AltIndigenousName` VARCHAR(255), 
  INDEX (`AltIndigenousNameID`), 
  INDEX (`PlaceID`), 
  PRIMARY KEY (`AltIndigenousNameID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'PlaceAltIndigenousName'
#

# 0 records

#
# Table structure for table 'PlaceGISSelections'
#

DROP TABLE IF EXISTS `PlaceGISSelections`;

CREATE TABLE `PlaceGISSelections` (
  `PlaceID` INTEGER, 
  `PlaceLabel` VARCHAR(255), 
  `SourceFC` VARCHAR(255)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'PlaceGISSelections'
#

# 0 records

#
# Table structure for table 'Places'
#

DROP TABLE IF EXISTS `Places`;

CREATE TABLE `Places` (
  `PlaceID` INTEGER NOT NULL AUTO_INCREMENT, 
  `IndigenousPlaceName` VARCHAR(255), 
  `IndigenousPlaceNameMeaning` VARCHAR(255), 
  `EnglishPlaceName` VARCHAR(255), 
  `PlanningUnitID` INTEGER DEFAULT 0, 
  `PrimaryHabitat` VARCHAR(100), 
  `TribeID` INTEGER, 
  `IsLocked` TINYINT(1) DEFAULT 0, 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  INDEX (`PlaceID`), 
  INDEX (`PlanningUnitID`), 
  PRIMARY KEY (`PlaceID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'Places'
#

INSERT INTO `Places` (`PlaceID`, `IndigenousPlaceName`, `IndigenousPlaceNameMeaning`, `EnglishPlaceName`, `PlanningUnitID`, `PrimaryHabitat`, `TribeID`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (19, 'Yan\'-tr\'ee-nash See', 'shark-rock', 'Shark Rock', 3, 'Offshore Rock', 1, 0, 'admin', 'General Admin', 'Admin', '2017-03-20 14:40:12', 'admin', 'Admin', 'General Admin', '2017-03-20 14:41:38');
INSERT INTO `Places` (`PlaceID`, `IndigenousPlaceName`, `IndigenousPlaceNameMeaning`, `EnglishPlaceName`, `PlanningUnitID`, `PrimaryHabitat`, `TribeID`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (20, 'Naa~-k\'vt Mii~-sdvm', 'gravel-size-for fish', 'Gravel Bed', 1, 'Sandy Beach', 1, 0, 'admin', 'General Admin', 'Admin', '2017-03-20 14:48:34', 'admin', 'Admin', 'General Admin', '2017-03-20 14:50:05');
# 2 records

#
# Table structure for table 'PlacesCitationEvents'
#

DROP TABLE IF EXISTS `PlacesCitationEvents`;

CREATE TABLE `PlacesCitationEvents` (
  `PlaceID` INTEGER NOT NULL, 
  `CitationID` INTEGER NOT NULL, 
  `RelationshipDescription` VARCHAR(255), 
  `Pages` VARCHAR(255), 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  INDEX (`PlaceID`), 
  PRIMARY KEY (`PlaceID`, `CitationID`), 
  INDEX (`CitationID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'PlacesCitationEvents'
#

# 0 records

#
# Table structure for table 'PlacesMediaEvents'
#

DROP TABLE IF EXISTS `PlacesMediaEvents`;

CREATE TABLE `PlacesMediaEvents` (
  `PlaceID` INTEGER NOT NULL, 
  `MediaID` INTEGER NOT NULL, 
  `RelationshipDescription` VARCHAR(255), 
  `Pages` VARCHAR(50), 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  INDEX (`MediaID`), 
  INDEX (`PlaceID`), 
  PRIMARY KEY (`PlaceID`, `MediaID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'PlacesMediaEvents'
#

# 0 records

#
# Table structure for table 'PlacesResourceCitationEvents'
#

DROP TABLE IF EXISTS `PlacesResourceCitationEvents`;

CREATE TABLE `PlacesResourceCitationEvents` (
  `PlaceResourceID` INTEGER NOT NULL, 
  `CitationID` INTEGER NOT NULL, 
  `RelationshipDescription` VARCHAR(255), 
  `Pages` VARCHAR(255), 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  INDEX (`PlaceResourceID`), 
  PRIMARY KEY (`PlaceResourceID`, `CitationID`), 
  INDEX (`CitationID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'PlacesResourceCitationEvents'
#

INSERT INTO `PlacesResourceCitationEvents` (`PlaceResourceID`, `CitationID`, `RelationshipDescription`, `Pages`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (22, 12, 'Discussion about mussels and otters', '11', 'admin', 'General Admin', 'Admin', '2017-03-20 14:58:29', 'admin', 'Admin', 'General Admin', '2017-03-20 14:59:40');
INSERT INTO `PlacesResourceCitationEvents` (`PlaceResourceID`, `CitationID`, `RelationshipDescription`, `Pages`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (23, 12, 'discussion about mussels and otters', '11', 'admin', 'General Admin', 'Admin', '2017-03-20 15:00:31', 'admin', 'Admin', 'General Admin', '2017-03-20 15:00:47');
# 2 records

#
# Table structure for table 'PlacesResourceEvents'
#

DROP TABLE IF EXISTS `PlacesResourceEvents`;

CREATE TABLE `PlacesResourceEvents` (
  `PlaceResourceID` INTEGER NOT NULL AUTO_INCREMENT, 
  `PlaceID` INTEGER NOT NULL, 
  `ResourceID` INTEGER NOT NULL, 
  `RelationshipDescription` VARCHAR(255), 
  `PartUsed` VARCHAR(255), 
  `CustomaryUse` VARCHAR(255), 
  `BarterResource` TINYINT(1) DEFAULT 0, 
  `Season` VARCHAR(255), 
  `Timing` VARCHAR(255), 
  `January` TINYINT(1) DEFAULT 0, 
  `February` TINYINT(1) DEFAULT 0, 
  `March` TINYINT(1) DEFAULT 0, 
  `April` TINYINT(1) DEFAULT 0, 
  `May` TINYINT(1) DEFAULT 0, 
  `June` TINYINT(1) DEFAULT 0, 
  `July` TINYINT(1) DEFAULT 0, 
  `August` TINYINT(1) DEFAULT 0, 
  `September` TINYINT(1) DEFAULT 0, 
  `October` TINYINT(1) DEFAULT 0, 
  `November` TINYINT(1) DEFAULT 0, 
  `December` TINYINT(1) DEFAULT 0, 
  `Year` INTEGER, 
  `IsLocked` TINYINT(1) DEFAULT 0, 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  INDEX (`PlaceID`, `ResourceID`), 
  INDEX (`PlaceID`), 
  INDEX (`PlaceResourceID`), 
  PRIMARY KEY (`PlaceResourceID`), 
  INDEX (`ResourceID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'PlacesResourceEvents'
#

INSERT INTO `PlacesResourceEvents` (`PlaceResourceID`, `PlaceID`, `ResourceID`, `RelationshipDescription`, `PartUsed`, `CustomaryUse`, `BarterResource`, `Season`, `Timing`, `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`, `Year`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (20, 19, 188, 'Bright orange chiton found on Shark Rock.  Plates (shells) were used for tools and meat was prepared for summer ceremony.', 'Shell', NULL, 0, 'All', NULL, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, NULL, 0, 'admin', 'General Admin', 'Admin', '2017-03-20 14:42:11', 'admin', 'Admin', 'General Admin', '2017-03-20 14:44:01');
INSERT INTO `PlacesResourceEvents` (`PlaceResourceID`, `PlaceID`, `ResourceID`, `RelationshipDescription`, `PartUsed`, `CustomaryUse`, `BarterResource`, `Season`, `Timing`, `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`, `Year`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (21, 20, 207, 'Dentalia shells were found mostly in gravel beds and used as a trading comodity by Native Americans.  Women were responsible for hand collecting the shells during the low tides of the spring, summer and fall.', 'Shell', NULL, 1, 'All', NULL, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, NULL, 0, 'admin', 'General Admin', 'Admin', '2017-03-20 14:50:16', 'admin', 'Admin', 'General Admin', '2017-03-20 14:52:50');
INSERT INTO `PlacesResourceEvents` (`PlaceResourceID`, `PlaceID`, `ResourceID`, `RelationshipDescription`, `PartUsed`, `CustomaryUse`, `BarterResource`, `Season`, `Timing`, `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`, `Year`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (22, 19, 266, '\"Some of the biggest mussels I\'ve ever seen, I got from Shark Rock. You could tell they were good eatin\', the otters always tried to get to \'em.\"', 'Meat', NULL, 0, 'Spring/Summer', NULL, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, NULL, 0, 'admin', 'General Admin', 'Admin', '2017-03-20 14:55:45', 'admin', 'Admin', 'General Admin', '2017-03-20 14:58:17');
INSERT INTO `PlacesResourceEvents` (`PlaceResourceID`, `PlaceID`, `ResourceID`, `RelationshipDescription`, `PartUsed`, `CustomaryUse`, `BarterResource`, `Season`, `Timing`, `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`, `Year`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (23, 19, 273, '\"Some of the biggest mussels I\'ve ever seen, I got from Shark Rock. You could tell they were good eatin\', the otters always tried to get to \'em.\"', NULL, NULL, 0, 'All', NULL, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, NULL, 0, 'admin', 'General Admin', 'Admin', '2017-03-20 15:00:05', 'admin', 'Admin', 'General Admin', '2017-03-20 15:00:18');
INSERT INTO `PlacesResourceEvents` (`PlaceResourceID`, `PlaceID`, `ResourceID`, `RelationshipDescription`, `PartUsed`, `CustomaryUse`, `BarterResource`, `Season`, `Timing`, `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`, `Year`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (24, 20, 347, '\"The men use A-frame nets to catch perch in the vacinity of gravel beds on the beach, because that\'s where the fish like to spawn and they gather in great numbers there in late spring and through summer - like May through August.\"', 'Meat', NULL, 0, 'Spring/Summer', NULL, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, NULL, 0, 'admin', 'General Admin', 'Admin', '2017-03-20 15:04:31', 'admin', 'Admin', 'General Admin', '2017-03-20 15:08:02');
# 5 records

#
# Table structure for table 'PlacesResourceMediaEvents'
#

DROP TABLE IF EXISTS `PlacesResourceMediaEvents`;

CREATE TABLE `PlacesResourceMediaEvents` (
  `PlaceResourceID` INTEGER NOT NULL, 
  `MediaID` INTEGER NOT NULL, 
  `RelationshipDescription` VARCHAR(255), 
  `Pages` VARCHAR(50), 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  INDEX (`PlaceResourceID`), 
  PRIMARY KEY (`PlaceResourceID`, `MediaID`), 
  INDEX (`MediaID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'PlacesResourceMediaEvents'
#

# 0 records

#
# Table structure for table 'ResourceActivityCitationEvents'
#

DROP TABLE IF EXISTS `ResourceActivityCitationEvents`;

CREATE TABLE `ResourceActivityCitationEvents` (
  `ResourceActivityID` INTEGER NOT NULL, 
  `CitationID` INTEGER NOT NULL, 
  `RelationshipDescription` VARCHAR(255), 
  `Pages` VARCHAR(255), 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  PRIMARY KEY (`ResourceActivityID`, `CitationID`), 
  INDEX (`ResourceActivityID`), 
  INDEX (`CitationID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'ResourceActivityCitationEvents'
#

INSERT INTO `ResourceActivityCitationEvents` (`ResourceActivityID`, `CitationID`, `RelationshipDescription`, `Pages`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (27, 11, 'harvesting of chitons', '16', 'admin', 'General Admin', 'Admin', '2017-03-20 14:44:54', 'admin', 'Admin', 'General Admin', '2017-03-20 14:45:08');
INSERT INTO `ResourceActivityCitationEvents` (`ResourceActivityID`, `CitationID`, `RelationshipDescription`, `Pages`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (28, 11, 'Gathering of dentalia', '36', 'admin', 'General Admin', 'Admin', '2017-03-20 14:53:14', 'admin', 'Admin', 'General Admin', '2017-03-20 14:53:34');
INSERT INTO `ResourceActivityCitationEvents` (`ResourceActivityID`, `CitationID`, `RelationshipDescription`, `Pages`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (31, 12, 'Discussion of perch fishing', '20', 'admin', 'General Admin', 'Admin', '2017-03-20 15:08:12', 'admin', 'Admin', 'General Admin', '2017-03-20 15:08:28');
# 3 records

#
# Table structure for table 'ResourceActivityMediaEvents'
#

DROP TABLE IF EXISTS `ResourceActivityMediaEvents`;

CREATE TABLE `ResourceActivityMediaEvents` (
  `ResourceActivityID` INTEGER NOT NULL, 
  `MediaID` INTEGER NOT NULL, 
  `RelationshipDescription` VARCHAR(255), 
  `Pages` VARCHAR(50), 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  PRIMARY KEY (`ResourceActivityID`, `MediaID`), 
  INDEX (`ResourceActivityID`), 
  INDEX (`MediaID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'ResourceActivityMediaEvents'
#

# 0 records

#
# Table structure for table 'ResourceAltIndigenousName'
#

DROP TABLE IF EXISTS `ResourceAltIndigenousName`;

CREATE TABLE `ResourceAltIndigenousName` (
  `AltIndigenousNameID` INTEGER NOT NULL AUTO_INCREMENT, 
  `ResourceID` INTEGER, 
  `AltIndigenousName` VARCHAR(255), 
  INDEX (`AltIndigenousNameID`), 
  PRIMARY KEY (`AltIndigenousNameID`), 
  INDEX (`ResourceID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'ResourceAltIndigenousName'
#

INSERT INTO `ResourceAltIndigenousName` (`AltIndigenousNameID`, `ResourceID`, `AltIndigenousName`) VALUES (6, 207, 'scaphapod');
# 1 records

#
# Table structure for table 'ResourceResourceEvents'
#

DROP TABLE IF EXISTS `ResourceResourceEvents`;

CREATE TABLE `ResourceResourceEvents` (
  `ResourceID` INTEGER NOT NULL, 
  `AltResourceID` INTEGER NOT NULL, 
  `RelationshipDescription` VARCHAR(255), 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  INDEX (`ResourceID`), 
  PRIMARY KEY (`ResourceID`, `AltResourceID`), 
  INDEX (`AltResourceID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'ResourceResourceEvents'
#

# 0 records

#
# Table structure for table 'Resources'
#

DROP TABLE IF EXISTS `Resources`;

CREATE TABLE `Resources` (
  `ResourceID` INTEGER NOT NULL AUTO_INCREMENT, 
  `CommonName` VARCHAR(255), 
  `IndigenousName` VARCHAR(255), 
  `Genus` VARCHAR(255), 
  `Species` VARCHAR(255), 
  `Specific` TINYINT(1) DEFAULT 0, 
  `ResourceClassificationGroup` VARCHAR(255), 
  `IsLocked` TINYINT(1) DEFAULT 0, 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  PRIMARY KEY (`ResourceID`), 
  INDEX (`ResourceID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'Resources'
#

INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (150, 'abalone', NULL, 'Haliotis', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, '', '', '', '2014-08-14 20:59:09');
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (151, 'abalone, Black', NULL, 'Haliotis', 'cracherdoii', 1, NULL, 0, NULL, NULL, NULL, NULL, 'paul', 'GIS', 'Far Western', '2014-08-26 19:42:54');
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (152, 'abalone, Flat', NULL, 'Haliotis ', 'walallensis', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (153, 'abalone, Pinto/Northern', NULL, 'Haliotis ', 'kamtschatkana ', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (154, 'abalone, Red', NULL, 'Haliotis ', 'rufescens', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (155, 'alder, Red', NULL, 'Alnus', 'rubra', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (156, 'ash', NULL, 'Fraxinus', 'latifolia', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (157, 'aven', NULL, 'Geum', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (158, 'baneberry', NULL, 'Actaea', 'rubra', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (159, 'barnacle', NULL, 'Balanus', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (160, 'barnacle, Acorn', NULL, 'Balanus ', 'glandula', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (161, 'barnacle, Crenate', NULL, 'Balanus', 'crenatus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (162, 'barnacle, Giant', NULL, 'Balanus', 'nubilus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (163, 'barnacle, Gooseneck/Longneck/Pig\'s foot)', NULL, 'Lepas', 'anatifera', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (164, 'barnacle, Leaf ', NULL, 'Pollicipes ', 'polymerus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (165, 'barnacle, Thatched', NULL, 'Semibalanus', 'cariosus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (166, 'beach grass', NULL, 'Ammophil', 'arenaria', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (167, 'beach pea', NULL, 'Lathyrus', 'japonicus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (168, 'beargrass /elkgrass', NULL, 'Xerophyllum', 'tenax', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (169, 'beaver', NULL, 'Castor', 'canadensis', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (170, 'black bass', NULL, 'Sebastes', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (171, 'black bear', NULL, 'Ursus', 'americanus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (172, 'Black turban snails', NULL, 'Tegula ', 'funebralis', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (173, 'blackberry, Evergreen', NULL, 'Rubus', 'laciniatus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (174, 'blackberry, Trailing/ Dewberry', NULL, 'Rubus', 'ursinus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (175, 'blueberry', NULL, 'Vaccinium', 'sp.', 0, 'plant', 0, NULL, NULL, NULL, NULL, 'paul', 'gis', 'fw', '2014-06-20 13:49:22');
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (176, 'bobcat', NULL, 'Lynx', 'rufus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (177, 'Bocaccio ', NULL, 'Sebastes ', 'paucispinus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (178, 'bull trout', NULL, 'Salvelinus', 'confluentus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (179, 'bullhead', NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (180, 'bulrush/ tule', NULL, 'Scirpus', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (181, 'Cabezon', NULL, 'Scorpaenichthys ', 'marmoratus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (182, 'camas', NULL, 'Camassia', 'quamash', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (183, 'cattail', NULL, 'Typha ', 'latifolia', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (184, 'cedar', NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (185, 'cedar, Western red', NULL, 'Thuja', 'plicata', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (186, 'China hats', NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (187, 'chiton', NULL, 'Mopalia', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (188, 'chiton, Gumboot', 'Met-gaa-chu', 'Cryptochiton', 'stelleri', 1, 'invertebrate', 0, NULL, NULL, NULL, NULL, 'admin', 'Admin', 'General Admin', '2017-03-20 14:46:40');
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (189, 'clam', NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (190, 'clam, Butter', NULL, 'Saxidomus', 'giganteus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (191, 'clam, Manila', NULL, 'Tapes', 'japonica', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (192, 'clam, Quahog', NULL, 'Mercenaria', 'mercenaria', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (193, 'clam, Razor', NULL, 'Siliqua', 'patula', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (194, 'clam, Soft-shell/Mud', NULL, 'Mya', 'arenaria', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (195, 'clover', NULL, 'Trifolium', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (196, 'cockel', NULL, 'Clinocardium ', 'nuttallii', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (197, 'codfishes', NULL, 'Gadidae', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (198, 'cottonwood', NULL, 'Populus', 'balsamifera', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (199, 'cougar', NULL, 'Puma', 'concolor', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (200, 'cow parsnip', NULL, 'Heracleum', 'maximum', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (201, 'crab', NULL, 'Cancer', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (202, 'crab apple', NULL, 'Malus', 'fusca', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (203, 'crab, Dungenous', NULL, 'Cancer', 'magister', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (204, 'cranberry', NULL, 'Viburnum', 'macrocarpon', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (205, 'currant', NULL, 'Ribes', 'spp.', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (206, 'deer', NULL, 'Odocoileus', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (207, 'dentalium', 'tr\'vt', 'Dentalium', 'sp.', 0, 'mollusk', 0, NULL, NULL, NULL, NULL, 'admin', 'Admin', 'General Admin', '2017-03-20 14:55:20');
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (208, 'devil\'s club', NULL, 'Oplopanaz', 'horridus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (209, 'Dolly Varden', NULL, 'Salvelinus', 'malma', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (210, 'duck', NULL, 'Anatidae', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (211, 'dune grass', NULL, 'Leymus', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (212, 'eel, California  moray', NULL, 'Gymnothorax ', 'mordax', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (213, 'eelgrass', NULL, 'Zostera', 'marina', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (214, 'elderberry, Blue', NULL, 'Sambucus', 'mexicana', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (215, 'elderberry, Red', NULL, 'Sambucus', 'racemosa', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (216, 'elk', NULL, 'Cervus', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (217, 'eulachon/ candlefish', NULL, 'Thalyicthes', 'pacificus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (218, 'false hellebore', NULL, 'Veratrum', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (219, 'false lily-of-the-valley', NULL, 'Maianthemum', 'dilatatum', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (220, 'fern', NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (221, 'fern, Braken', NULL, 'Pteridium', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (222, 'fern, Deer', NULL, 'Blechnum', 'spicant', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (223, 'fern, Lady', NULL, 'Athyrium', 'femina', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (224, 'fern, Licorice', NULL, 'Polypodium', 'glycyrrhiza', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (225, 'fern, Maidenhair', NULL, 'Adiantum', 'aleuticum', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (226, 'fern, Sword', NULL, 'Polystichum', 'munitum', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (227, 'fern, Wood', NULL, 'Dryopteris', 'spp.', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (228, 'fir', NULL, 'Abies', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (229, 'fir, Douglas', NULL, 'Pseudotsuga', 'menziesii', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (230, 'fish', NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (231, 'Flatfish; sole, flounder', NULL, 'Pleuronectidae, Bothidae', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (232, 'Flounder, starry', NULL, 'Plathichthys ', 'stellatus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (233, 'Geoduck', NULL, 'Panopea', 'generosa', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (234, 'goose', NULL, 'Anserini ', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (235, 'gooseberry', NULL, 'Ribes', 'divaricatum', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (236, 'Greenling, Kelp/sea trout', NULL, 'Hexagrammos ', 'decagrammus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (237, 'Greenling, Rock/sea trout', NULL, 'Hexagrammos ', 'superciliosus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (238, 'groundfish', NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (239, 'hagfish', NULL, 'Eptatretus ', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (240, 'halibut, California', NULL, 'Paralichthys ', 'californicus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (241, 'hedge nettle', NULL, 'Stachys', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (242, 'hemlock, Western', NULL, 'Tsuga', 'heterophylla', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (243, 'heron, Blue', NULL, 'Ardea', 'herodias', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (244, 'horsetail, Giant', NULL, 'Equisetum', 'telmateia', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (245, 'horsetail, Snakeheads', NULL, 'Equisetum', 'arvense', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (246, 'huckleberry, Blue/Black/Shotberry', NULL, 'Vaccinium', 'ovalifolium', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (247, 'huckleberry, Bog', NULL, 'Vaccinium', 'uliginosum', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (248, 'huckleberry, Red', NULL, 'Vaccinium', 'parvifolium', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (249, 'huckleberry, Winter evergreen', NULL, 'Vaccinium', 'ovatum', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (250, 'kelp', NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (251, 'kelp, Bull', NULL, 'Nereocystis ', 'luetkeana', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (252, 'kelp, Giant', NULL, 'Macrocystis ', 'pyrifera', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (253, 'kinnikinnick', NULL, 'Arctostaphylos', 'ursi', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (254, 'lamprey, Pacific/Eel', NULL, 'Lampetra', 'tridentatus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (255, 'lamprey, river', NULL, 'Lampetra', 'ayresi', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (256, 'lily, Tiger/Columbia', NULL, 'Lilium', 'columbianum', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (257, 'limpet', NULL, 'Lottia; Tectura', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (258, 'limpet, Ribbed', NULL, 'Lottia', 'digitalis', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (259, 'limpet, Shield', NULL, 'Lottia', 'pelta', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (260, 'lingcod', NULL, 'Ophiodon', 'elongatus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (261, 'loon', NULL, 'Gavia', 'immer', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (262, 'miner\'s lettuce', NULL, 'Claytonia', 'spp.', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (263, 'mink', NULL, 'Mustela', 'vison', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (264, 'mussel', NULL, 'Mytilus', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (265, 'mussel, Bay/Blue', NULL, 'Mytilu', 'trossulus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (266, 'mussel, California', 'dee-lhat', 'Mytilus', 'californianus', 1, 'mollusk', 0, NULL, NULL, NULL, NULL, 'admin', 'Admin', 'General Admin', '2017-03-20 15:01:38');
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (267, 'nodding onion', NULL, 'Allium', 'cernuum', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (268, 'Northern anchovy', NULL, 'Engraulis', 'mordax', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (269, 'ocean spray ', NULL, 'Holodiscus', 'discolor', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (270, 'octopus', NULL, 'Octopus', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (271, 'olivella', NULL, 'Olivella', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (272, 'oso berry/ Indian plum', NULL, 'Oemlaeria', 'cerasiformis', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (273, 'otter, River', 'naa-ghaa-t\'u\'-ne', 'Lutra', 'canadensis', 1, 'marine mammal', 0, NULL, NULL, NULL, NULL, 'admin', 'Admin', 'General Admin', '2017-03-20 15:03:48');
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (274, 'oyster  ', NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (275, 'oyster, Rock', NULL, 'Pododesmus', 'cepio', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (276, 'Pacific halibut', NULL, 'Hippoglossus', 'stenolepis', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (277, 'Pacific herring', NULL, 'Clupea', 'harengus pallasi', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (278, 'perch, Pacific Ocean', NULL, 'Sebastes', 'alutus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (279, 'periwinkle', NULL, 'Littorina', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (280, 'pine, Lodgepole', NULL, 'Pinus', 'contorta', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (281, 'pine, Western white', NULL, 'Pinus', 'monticola', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (282, 'rabbit', NULL, 'Sylvilagus', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (283, 'raccoon', NULL, 'Procyon', 'lotor', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (284, 'Red snapper', NULL, 'Sebastes', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (285, 'rockfish', NULL, 'Sebastes', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (286, 'rose', NULL, 'Rosa', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (287, 'rush, Scouring', NULL, 'Equisetum ', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (288, 'rushes', NULL, 'Juncus', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (289, 'sablefish/ black cod', NULL, 'Anoplopoma', 'fimbria', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (290, 'salal', NULL, 'Gaultheria', 'shallon', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (291, 'salmon, Chinook/King', NULL, 'Oncorhynchus ', 'tshawytscha', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (292, 'salmon, Chum/Dog', NULL, 'Oncorhynchus', 'keta', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (293, 'salmon, Coho/Silver', NULL, 'Oncorhynchus', 'kiscutch', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (294, 'salmon, Pink/ Humpback', NULL, 'Oncorhynchus', 'gorbuscha', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (295, 'salmon, Sockeye/Blueback', NULL, 'Oncorhynchus', 'nerka', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (296, 'salmonberry', NULL, 'Rubus', 'spectabilis', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (297, 'sanddab, Pacific', NULL, 'Citharichthys ', 'sordidus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (298, 'sanddollar', NULL, 'Dendraster', 'excentricus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (299, 'scallop', NULL, 'Chlamys', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (300, 'scallop, Rock', NULL, 'Hinnites', 'giganteus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (301, 'scallop, Weather vane', NULL, 'Pecten', 'caurinus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (302, 'sculpin, Pacific Staghorn/Bullhead', NULL, 'Leptocottus ', 'armatus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (303, 'sea anemone/rose', NULL, 'Anthopleura; Urticina; Epiactis; Cnidopus', 'sp,; sp.; prolifera; ritteri', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (304, 'sea bass, white', NULL, 'Cynoscion', 'nobilis', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (305, 'sea cucumber', NULL, 'Cucumaria; Stichopus; Eupentacta; Psolus; Psolidium', ' sp.; californicas; quinquesemita; chitonoides; bullatum', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (306, 'sea gull', NULL, 'Laridae', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (307, 'sea lion, California', NULL, 'Zalophus', 'californianus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (308, 'sea lion, Steller/ Northern', NULL, 'Eumetopias', 'jubatus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (309, 'Sea Palm', NULL, 'Postelsia ', 'palmaeformis', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (310, 'sea snail', NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (311, 'sea star', NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (312, 'sea urchin', NULL, 'Strongylocentrotus', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (313, 'seabass', NULL, 'Sebastes', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (314, 'seabirds', NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (315, 'seal', NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (316, 'seal, Fur', NULL, 'Callorhinus', 'ursinus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (317, 'seal, Northern elephant', NULL, 'Mirounga', 'angustirostris', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (318, 'seal, Pacific harbor', NULL, 'Phoca', 'vitulina', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (319, 'seaweed ', NULL, 'Porphyra', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (320, 'sedge, Slough', NULL, 'Carex', 'obnupta', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (321, 'sedges', NULL, 'Carex', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (322, 'shore grass', NULL, 'Distichlis', 'spicata', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (323, 'shrimp', NULL, 'Pandalus', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (324, 'skate', NULL, 'Raja', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (325, 'skunk cabbage', NULL, 'Lysichiton', 'americanus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (326, 'smelt', NULL, 'Osmeridae', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (327, 'smelt, Longfin', NULL, 'Spirinchus', 'thalyicthys', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (328, 'smelt, Night/nightfish', NULL, 'Spirinchus ', 'starski', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (329, 'smelt, Surf/surfish', NULL, 'Hypomesus ', 'pretiosus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (330, 'smelt, White bait', NULL, 'Allosmerus', 'elongatus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (331, 'snail', NULL, 'Gastipodia', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (332, 'soapberry', NULL, 'Shepherdia', 'canadensis', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (333, 'sole, Sand', NULL, 'Psettichthys ', 'melanostictus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (334, 'spruce', NULL, 'Picea', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (335, 'spruce, Sitka', NULL, 'Picea', 'sitchensis', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (336, 'squid, Humboldt', NULL, 'Dosidicus', 'gigas', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (337, 'squid, Pacific/opalescent/market', NULL, 'Loligo', 'opalescens', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (338, 'steelhead', NULL, 'Oncorhynchus', 'mykiss', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (339, 'stinging nettle/ gen. nettle', NULL, 'Urtica', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (340, 'strawberry', NULL, 'Fragaria', 'chiloensis', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (341, 'sturgeon, green', NULL, 'Acipenser', 'medirostris', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (342, 'sturgeon, White', NULL, 'Acipenser', 'transmontanus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (343, 'surfgrass, Scouler\'s', NULL, 'Phyllospadix', 'scouleri', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (344, 'surfgrass, Serrated', NULL, 'Phyllospadix', 'serrulatus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (345, 'surfgrass, Torrey\'s', NULL, 'Phyllospadix', 'torreyi', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (346, 'surfgrasses', NULL, 'Phyllospadix', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (347, 'surfperch', 'Chii-la\'', 'Embiotocidae', 'sp.', 0, 'anadromous finfish', 0, NULL, NULL, NULL, NULL, 'admin', 'Admin', 'General Admin', '2017-03-20 15:19:39');
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (348, 'surfperch, Black', NULL, 'Embiotoca ', 'jacksoni', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (349, 'surfperch, Calico', NULL, 'Amphistichus ', 'koelzi', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (350, 'surfperch, Pile', NULL, 'Damalichthys ', 'vacca', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (351, 'surfperch, Rainbow', NULL, 'Hypsurus ', 'caryi', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (352, 'surfperch, Redtail', NULL, 'Amphistichus ', 'rhodoterus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (353, 'surfperch, Rubberlip', NULL, 'Rhacochilus ', 'toxotes', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (354, 'surfperch, Shiner', NULL, 'Cymatogaster ', 'aggregata', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (355, 'surfperch, Striped', NULL, 'Embiotoca ', 'lateralis', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (356, 'surfperch, Walleye', NULL, 'Hyperprosopon ', 'argenteum', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (357, 'surfperch, White', NULL, 'Phanerodon ', 'furcatus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (358, 'sweet grass', NULL, 'Hierochloe', 'spp', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (359, 'tea, Labrador', NULL, 'Ledum', 'groenlandicum', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (360, 'thimbleberry', NULL, 'Rubus', 'parviflorus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (361, 'thistle', NULL, 'Cirsium', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (362, 'trout, Cutthroat/Sea trout', NULL, 'Salmo', 'clarki clarki', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (363, 'tubesnouts', NULL, 'Procellariiformes', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (364, 'turtle', NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (365, 'vine maple', NULL, 'Acer', 'circinatum', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (366, 'wapato/ arrowhead', NULL, 'Sagittaria', 'latifolia', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (367, 'water lilies', NULL, 'Nuphar', 'polysepalum', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (368, 'western pearlshell', NULL, 'Margaritifera', 'falcata', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (369, 'whale', NULL, NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (370, 'whale, Blue', NULL, 'Blaenoptera', 'musculus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (371, 'whale, Fin', NULL, 'Balaenoptera', 'physalus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (372, 'whale, Gray', NULL, 'Eschrichtius', 'robustus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (373, 'whale, Humpback', NULL, 'Megaptera', 'novaeangliae', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (374, 'whale, Killer', NULL, 'Orcinus', 'orca', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (375, 'whale, Minke', NULL, 'Balaenoptera', 'acutorostrata', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (376, 'whale, Right', NULL, 'Eubalaena', 'japonica', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (377, 'whale, Sperm', NULL, 'Physeter', 'macrocephalus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (378, 'whelk', NULL, 'Nassarius', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (379, 'whiting, Pacific/Pacific hake', NULL, 'Merluccius ', 'productus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (380, 'wild cherry', NULL, 'Prunus', 'emarginata', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (381, 'wild cranberry', NULL, 'Viburnum', 'oxycoccos', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (382, 'wild rye', NULL, 'Elymus', 'spp.', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (383, 'willow', NULL, 'Salix', 'sp.', 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (384, 'wolf  ', NULL, 'Canis', 'lupus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (385, 'Wolf eel', NULL, 'Anarrhichthys ', 'ocellatus', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `Resources` (`ResourceID`, `CommonName`, `IndigenousName`, `Genus`, `Species`, `Specific`, `ResourceClassificationGroup`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (386, 'yarrow', NULL, 'Achillea', 'millefolium', 1, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
# 237 records

#
# Table structure for table 'ResourcesActivityEvents'
#

DROP TABLE IF EXISTS `ResourcesActivityEvents`;

CREATE TABLE `ResourcesActivityEvents` (
  `ResourceActivityID` INTEGER NOT NULL AUTO_INCREMENT, 
  `PlaceResourceID` INTEGER NOT NULL, 
  `RelationshipDescription` LONGTEXT, 
  `PartUsed` VARCHAR(255), 
  `ActivityShortDescription` VARCHAR(255), 
  `ActivityLongDescription` LONGTEXT, 
  `Participants` VARCHAR(50), 
  `Technique` VARCHAR(255), 
  `Gear` VARCHAR(255), 
  `CustomaryUse` VARCHAR(255), 
  `Timing` VARCHAR(255), 
  `TimingDescription` VARCHAR(255), 
  `IsLocked` TINYINT(1) DEFAULT 0, 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  PRIMARY KEY (`ResourceActivityID`), 
  INDEX (`ResourceActivityID`), 
  INDEX (`PlaceResourceID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'ResourcesActivityEvents'
#

INSERT INTO `ResourcesActivityEvents` (`ResourceActivityID`, `PlaceResourceID`, `RelationshipDescription`, `PartUsed`, `ActivityShortDescription`, `ActivityLongDescription`, `Participants`, `Technique`, `Gear`, `CustomaryUse`, `Timing`, `TimingDescription`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (27, 20, 'Bright orange chiton gathered off Shark Rock for meet and for use in tools', NULL, NULL, NULL, 'Everyone', 'hand gathered', NULL, NULL, NULL, NULL, 0, 'admin', 'General Admin', 'Admin', '2017-03-20 14:44:00', 'admin', 'Admin', 'General Admin', '2017-03-20 14:44:54');
INSERT INTO `ResourcesActivityEvents` (`ResourceActivityID`, `PlaceResourceID`, `RelationshipDescription`, `PartUsed`, `ActivityShortDescription`, `ActivityLongDescription`, `Participants`, `Technique`, `Gear`, `CustomaryUse`, `Timing`, `TimingDescription`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (28, 21, 'Women gathered by hand dentalia shells from the beach', NULL, NULL, NULL, 'Women', 'hand gathered', NULL, NULL, NULL, NULL, 0, 'admin', 'General Admin', 'Admin', '2017-03-20 14:52:50', 'admin', 'Admin', 'General Admin', '2017-03-20 14:53:14');
INSERT INTO `ResourcesActivityEvents` (`ResourceActivityID`, `PlaceResourceID`, `RelationshipDescription`, `PartUsed`, `ActivityShortDescription`, `ActivityLongDescription`, `Participants`, `Technique`, `Gear`, `CustomaryUse`, `Timing`, `TimingDescription`, `IsLocked`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (31, 24, '\"The men use A-frame nets to catch perch in the vacinity of gravel beds on the beach, because that\'s where the fish like to spawn and they gather in great numbers there in late spring and through summer - like May through August.\"', NULL, NULL, NULL, 'Men', 'A-frame net', NULL, NULL, NULL, NULL, 0, 'admin', 'General Admin', 'Admin', '2017-03-20 15:08:02', 'admin', 'Admin', 'General Admin', '2017-03-20 15:08:12');
# 3 records

#
# Table structure for table 'ResourcesCitationEvents'
#

DROP TABLE IF EXISTS `ResourcesCitationEvents`;

CREATE TABLE `ResourcesCitationEvents` (
  `ResourceID` INTEGER NOT NULL, 
  `CitationID` INTEGER NOT NULL, 
  `RelationshipDescription` VARCHAR(255), 
  `Pages` VARCHAR(255), 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  INDEX (`ResourceID`), 
  PRIMARY KEY (`ResourceID`, `CitationID`), 
  INDEX (`CitationID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'ResourcesCitationEvents'
#

# 0 records

#
# Table structure for table 'ResourcesMediaEvents'
#

DROP TABLE IF EXISTS `ResourcesMediaEvents`;

CREATE TABLE `ResourcesMediaEvents` (
  `ResourceID` INTEGER NOT NULL, 
  `MediaID` INTEGER NOT NULL, 
  `RelationshipDescription` VARCHAR(255), 
  `Pages` VARCHAR(50), 
  `EnteredByName` VARCHAR(25), 
  `EnteredByTribe` VARCHAR(100), 
  `EnteredByTitle` VARCHAR(100), 
  `EnteredByDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  `ModifiedByName` VARCHAR(25), 
  `ModifiedByTitle` VARCHAR(100), 
  `ModifiedByTribe` VARCHAR(100), 
  `ModifiedByDate` DATETIME, 
  INDEX (`ResourceID`), 
  PRIMARY KEY (`ResourceID`, `MediaID`), 
  INDEX (`MediaID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'ResourcesMediaEvents'
#

INSERT INTO `ResourcesMediaEvents` (`ResourceID`, `MediaID`, `RelationshipDescription`, `Pages`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (188, 6, NULL, NULL, 'admin', 'General Admin', 'Admin', '2017-03-20 15:18:08', 'admin', 'Admin', 'General Admin', '2017-03-20 15:18:13');
INSERT INTO `ResourcesMediaEvents` (`ResourceID`, `MediaID`, `RelationshipDescription`, `Pages`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (266, 7, NULL, NULL, 'admin', 'General Admin', 'Admin', '2017-03-20 15:18:26', 'admin', 'Admin', 'General Admin', '2017-03-20 15:18:32');
INSERT INTO `ResourcesMediaEvents` (`ResourceID`, `MediaID`, `RelationshipDescription`, `Pages`, `EnteredByName`, `EnteredByTribe`, `EnteredByTitle`, `EnteredByDate`, `ModifiedByName`, `ModifiedByTitle`, `ModifiedByTribe`, `ModifiedByDate`) VALUES (347, 8, NULL, NULL, 'admin', 'General Admin', 'Admin', '2017-03-20 15:19:30', 'admin', 'Admin', 'General Admin', '2017-03-20 15:19:35');
# 3 records

#
# Table structure for table 'UserAccess'
#

DROP TABLE IF EXISTS `UserAccess`;

CREATE TABLE `UserAccess` (
  `AccessID` INTEGER NOT NULL AUTO_INCREMENT, 
  `AccessLevel` VARCHAR(255), 
  INDEX (`AccessID`), 
  PRIMARY KEY (`AccessID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'UserAccess'
#

INSERT INTO `UserAccess` (`AccessID`, `AccessLevel`) VALUES (1, 'Administrator');
INSERT INTO `UserAccess` (`AccessID`, `AccessLevel`) VALUES (2, 'Editor');
INSERT INTO `UserAccess` (`AccessID`, `AccessLevel`) VALUES (3, 'Reader');
# 3 records

#
# Table structure for table 'Users'
#

DROP TABLE IF EXISTS `Users`;

CREATE TABLE `Users` (
  `UserID` INTEGER NOT NULL AUTO_INCREMENT, 
  `UserName` VARCHAR(20) NOT NULL, 
  `Password` VARCHAR(20) NOT NULL, 
  `FirstName` VARCHAR(255) NOT NULL, 
  `LastName` VARCHAR(255) NOT NULL, 
  `Affiliation` VARCHAR(255) NOT NULL, 
  `Title` VARCHAR(255) NOT NULL, 
  `AccessLevel` INTEGER NOT NULL, 
  PRIMARY KEY (`UserID`), 
  INDEX (`UserID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'Users'
#

INSERT INTO `Users` (`UserID`, `UserName`, `Password`, `FirstName`, `LastName`, `Affiliation`, `Title`, `AccessLevel`) VALUES (5, 'admin', 'admin', 'Admin', 'Administrator', 'General Admin', 'Admin', 1);
INSERT INTO `Users` (`UserID`, `UserName`, `Password`, `FirstName`, `LastName`, `Affiliation`, `Title`, `AccessLevel`) VALUES (6, 'editor', 'editor', 'Editor', 'Editor', 'General Admin', 'Editor', 2);
INSERT INTO `Users` (`UserID`, `UserName`, `Password`, `FirstName`, `LastName`, `Affiliation`, `Title`, `AccessLevel`) VALUES (7, 'readonly', 'readonly', 'Read', 'Only', 'General Access', 'Mr. Reader', 3);
# 3 records

