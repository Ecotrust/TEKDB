-- ----------------------------------------------------------------------------
-- MySQL Workbench Migration
-- Migrated Schemata: ethnographic_elements_be
-- Source Schemata: ethnographic_elements_be
-- Created: Sat Mar 04 09:59:28 2017
-- Workbench Version: 6.3.8
-- ----------------------------------------------------------------------------

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------------------------------------------------------
-- Schema ethnographic_elements_be
-- ----------------------------------------------------------------------------
DROP SCHEMA IF EXISTS `ethnographic_elements_be` ;
CREATE SCHEMA IF NOT EXISTS `ethnographic_elements_be` ;

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.ResourcesActivityEvents
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`ResourcesActivityEvents` (
  `ResourceActivityID` INT(10) NOT NULL,
  `PlaceResourceID` INT(10) NULL,
  `RelationshipDescription` LONGTEXT NULL,
  `PartUsed` VARCHAR(255) NULL,
  `ActivityShortDescription` VARCHAR(255) NULL,
  `ActivityLongDescription` LONGTEXT NULL,
  `Participants` VARCHAR(50) NULL,
  `Technique` VARCHAR(255) NULL,
  `Gear` VARCHAR(255) NULL,
  `CustomaryUse` VARCHAR(255) NULL,
  `Timing` VARCHAR(255) NULL,
  `TimingDescription` VARCHAR(255) NULL,
  `IsLocked` TINYINT(1) NOT NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `ResourcesActivityEventsPlaceResourceID` (`PlaceResourceID` ASC),
  PRIMARY KEY (`ResourceActivityID`),
  INDEX `ResourceActivityID` (`ResourceActivityID` ASC),
  INDEX `PlacesResourceEventsResourcesActivityEvents` (`PlaceResourceID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LocalityGISSelections
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LocalityGISSelections` (
  `LocalityID` INT(10) NULL,
  `LocalityLabel` VARCHAR(255) NULL,
  `SourceFC` VARCHAR(255) NULL);

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupTechniques
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupTechniques` (
  `Techniques` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`Techniques`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.Locality
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`Locality` (
  `LocalityID` INT(10) NOT NULL,
  `PlaceID` INT(10) NULL,
  `EnglishName` VARCHAR(255) NULL,
  `IndigenousName` VARCHAR(255) NULL,
  `LocalityType` VARCHAR(255) NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `PlacesLocality` (`PlaceID` ASC),
  INDEX `LocalityID` (`LocalityID` ASC),
  PRIMARY KEY (`LocalityID`),
  INDEX `PlaceID` (`PlaceID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.Media
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`Media` (
  `MediaID` INT(10) NOT NULL,
  `MediaType` VARCHAR(255) NULL,
  `MediaName` VARCHAR(255) NULL,
  `MediaDescription` LONGTEXT NULL,
  `MediaLink` VARCHAR(255) NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `MediaID` (`MediaID` ASC),
  PRIMARY KEY (`MediaID`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupParticipants
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupParticipants` (
  `Participants` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`Participants`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.MediaCitationEvents
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`MediaCitationEvents` (
  `MediaID` INT(10) NOT NULL,
  `CitationID` INT(10) NOT NULL,
  `RelationshipDescription` VARCHAR(255) NULL,
  `Pages` VARCHAR(255) NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `MediaMediaCitationEvents` (`MediaID` ASC),
  INDEX `SpeciesID` (`CitationID` ASC),
  PRIMARY KEY (`MediaID`, `CitationID`),
  INDEX `CitationsMediaCitationEvents` (`CitationID` ASC),
  INDEX `PlaceID` (`MediaID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.Citations
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`Citations` (
  `CitationID` INT(10) NOT NULL,
  `ReferenceType` VARCHAR(255) NULL,
  `ReferenceText` VARCHAR(50) NULL,
  `AuthorType` VARCHAR(255) NULL,
  `AuthorPrimary` VARCHAR(255) NULL,
  `AuthorSecondary` VARCHAR(255) NULL,
  `IntervieweeID` INT(10) NULL,
  `InterviewerID` INT(10) NULL,
  `PlaceofInterview` VARCHAR(255) NULL,
  `Year` INT(10) NULL,
  `Title` LONGTEXT NULL,
  `SeriesTitle` VARCHAR(255) NULL,
  `SeriesVolume` VARCHAR(50) NULL,
  `SeriesEditor` VARCHAR(255) NULL,
  `Publisher` VARCHAR(100) NULL,
  `PublisherCity` VARCHAR(255) NULL,
  `PreparedFor` VARCHAR(100) NULL,
  `Comments` LONGTEXT NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `CitationsCitationID` (`CitationID` ASC),
  PRIMARY KEY (`CitationID`),
  INDEX `InteviewerID` (`InterviewerID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupUserInfo
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupUserInfo` (
  `UserName` VARCHAR(100) NULL,
  `UsingCustomUsername` TINYINT(1) NOT NULL,
  `UserTitle` VARCHAR(100) NULL,
  `UserAffiliation` VARCHAR(100) NULL);

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupActivity
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupActivity` (
  `Activity` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`Activity`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.PlacesResourceCitationEvents
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`PlacesResourceCitationEvents` (
  `PlaceResourceID` INT(10) NOT NULL,
  `CitationID` INT(10) NOT NULL,
  `RelationshipDescription` VARCHAR(255) NULL,
  `Pages` VARCHAR(255) NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `SpeciesID` (`CitationID` ASC),
  INDEX `PlaceResourceID` (`PlaceResourceID` ASC),
  PRIMARY KEY (`PlaceResourceID`, `CitationID`),
  INDEX `PlacesResourceEventsPlacesResourceCitationEvents` (`PlaceResourceID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupHabitat
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupHabitat` (
  `Habitat` VARCHAR(100) NOT NULL,
  INDEX `LookupHabitatID` (`Habitat` ASC),
  PRIMARY KEY (`Habitat`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.Users
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`Users` (
  `UserID` INT(10) NOT NULL,
  `UserName` VARCHAR(20) NULL,
  `Password` VARCHAR(20) NULL,
  `FirstName` VARCHAR(255) NULL,
  `LastName` VARCHAR(255) NULL,
  `Affiliation` VARCHAR(255) NULL,
  `Title` VARCHAR(255) NULL,
  `AccessLevel` INT(10) NULL,
  INDEX `UserID` (`UserID` ASC),
  PRIMARY KEY (`UserID`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.PlaceAltIndigenousName
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`PlaceAltIndigenousName` (
  `AltIndigenousNameID` INT(10) NOT NULL,
  `PlaceID` INT(10) NULL,
  `AltIndigenousName` VARCHAR(255) NULL,
  INDEX `AltIndigenousNameID` (`AltIndigenousNameID` ASC),
  PRIMARY KEY (`AltIndigenousNameID`),
  INDEX `PlaceID` (`PlaceID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupReferenceType
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupReferenceType` (
  `DocumentType` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`DocumentType`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupLocalityType
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupLocalityType` (
  `LocalityType` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`LocalityType`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupPartUsed
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupPartUsed` (
  `PartUsed` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`PartUsed`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupSeason
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupSeason` (
  `Season` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`Season`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.ResourceActivityCitationEvents
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`ResourceActivityCitationEvents` (
  `ResourceActivityID` INT(10) NOT NULL,
  `CitationID` INT(10) NOT NULL,
  `RelationshipDescription` VARCHAR(255) NULL,
  `Pages` VARCHAR(255) NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `SpeciesID` (`CitationID` ASC),
  INDEX `ResourcesActivityEventsResourceActivityCitationEvents` (`ResourceActivityID` ASC),
  PRIMARY KEY (`ResourceActivityID`, `CitationID`),
  INDEX `ResourceActivityID` (`ResourceActivityID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.PlacesMediaEvents
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`PlacesMediaEvents` (
  `PlaceID` INT(10) NOT NULL,
  `MediaID` INT(10) NOT NULL,
  `RelationshipDescription` VARCHAR(255) NULL,
  `Pages` VARCHAR(50) NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `PlacesPlacesMediaEvents` (`PlaceID` ASC),
  INDEX `MediaID` (`MediaID` ASC),
  PRIMARY KEY (`PlaceID`, `MediaID`),
  INDEX `PlacesID` (`PlaceID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.ResourcesMediaEvents
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`ResourcesMediaEvents` (
  `ResourceID` INT(10) NOT NULL,
  `MediaID` INT(10) NOT NULL,
  `RelationshipDescription` VARCHAR(255) NULL,
  `Pages` VARCHAR(50) NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `ResourcesResourcesMediaEvents` (`ResourceID` ASC),
  INDEX `SpeciesID` (`MediaID` ASC),
  PRIMARY KEY (`ResourceID`, `MediaID`),
  INDEX `PlaceID` (`ResourceID` ASC),
  INDEX `MediaResourcesMediaEvents` (`MediaID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.ResourcesCitationEvents
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`ResourcesCitationEvents` (
  `ResourceID` INT(10) NOT NULL,
  `CitationID` INT(10) NOT NULL,
  `RelationshipDescription` VARCHAR(255) NULL,
  `Pages` VARCHAR(255) NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `SpeciesID` (`CitationID` ASC),
  INDEX `ResourcesResourcesCitationEvents` (`ResourceID` ASC),
  PRIMARY KEY (`ResourceID`, `CitationID`),
  INDEX `PlaceID` (`ResourceID` ASC),
  INDEX `CitationsResourcesCitationEvents` (`CitationID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.ResourceAltIndigenousName
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`ResourceAltIndigenousName` (
  `AltIndigenousNameID` INT(10) NOT NULL,
  `ResourceID` INT(10) NULL,
  `AltIndigenousName` VARCHAR(255) NULL,
  INDEX `AltIndigenousNameID` (`AltIndigenousNameID` ASC),
  PRIMARY KEY (`AltIndigenousNameID`),
  INDEX `ResourceID` (`ResourceID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupMediaType
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupMediaType` (
  `MediaType` VARCHAR(255) NOT NULL,
  `MediaCategory` VARCHAR(255) NULL,
  PRIMARY KEY (`MediaType`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.Places
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`Places` (
  `PlaceID` INT(10) NOT NULL,
  `IndigenousPlaceName` VARCHAR(255) NULL,
  `IndigenousPlaceNameMeaning` VARCHAR(255) NULL,
  `EnglishPlaceName` VARCHAR(255) NULL,
  `PlanningUnitID` INT(10) NULL,
  `PrimaryHabitat` VARCHAR(100) NULL,
  `TribeID` INT(10) NULL,
  `IsLocked` TINYINT(1) NOT NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `PlanningUnitID` (`PlanningUnitID` ASC),
  PRIMARY KEY (`PlaceID`),
  INDEX `PlaceID` (`PlaceID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupCustomaryUse
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupCustomaryUse` (
  `UsedFor` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`UsedFor`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.ResourceResourceEvents
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`ResourceResourceEvents` (
  `ResourceID` INT(10) NOT NULL,
  `AltResourceID` INT(10) NOT NULL,
  `RelationshipDescription` VARCHAR(255) NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `SpeciesID` (`AltResourceID` ASC),
  PRIMARY KEY (`ResourceID`, `AltResourceID`),
  INDEX `PlaceID` (`ResourceID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.PlacesCitationEvents
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`PlacesCitationEvents` (
  `PlaceID` INT(10) NOT NULL,
  `CitationID` INT(10) NOT NULL,
  `RelationshipDescription` VARCHAR(255) NULL,
  `Pages` VARCHAR(255) NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `SpeciesID` (`CitationID` ASC),
  INDEX `PlacesPlacesCitationEvents` (`PlaceID` ASC),
  PRIMARY KEY (`PlaceID`, `CitationID`),
  INDEX `PlaceID` (`PlaceID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.CurrentVersion
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`CurrentVersion` (
  `ID` INT(10) NOT NULL,
  `BackendVersion` INT(10) NULL,
  `FrontendVersion` INT(10) NULL,
  PRIMARY KEY (`ID`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupTiming
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupTiming` (
  `Timing` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`Timing`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.UserAccess
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`UserAccess` (
  `AccessID` INT(10) NOT NULL,
  `AccessLevel` VARCHAR(255) NULL,
  PRIMARY KEY (`AccessID`),
  INDEX `AccessID` (`AccessID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.PlacesResourceEvents
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`PlacesResourceEvents` (
  `PlaceResourceID` INT(10) NOT NULL,
  `PlaceID` INT(10) NULL,
  `ResourceID` INT(10) NULL,
  `RelationshipDescription` VARCHAR(255) NULL,
  `PartUsed` VARCHAR(255) NULL,
  `CustomaryUse` VARCHAR(255) NULL,
  `BarterResource` TINYINT(1) NOT NULL,
  `Season` VARCHAR(255) NULL,
  `Timing` VARCHAR(255) NULL,
  `January` TINYINT(1) NOT NULL,
  `February` TINYINT(1) NOT NULL,
  `March` TINYINT(1) NOT NULL,
  `April` TINYINT(1) NOT NULL,
  `May` TINYINT(1) NOT NULL,
  `June` TINYINT(1) NOT NULL,
  `July` TINYINT(1) NOT NULL,
  `August` TINYINT(1) NOT NULL,
  `September` TINYINT(1) NOT NULL,
  `October` TINYINT(1) NOT NULL,
  `November` TINYINT(1) NOT NULL,
  `December` TINYINT(1) NOT NULL,
  `Year` SMALLINT(5) NULL,
  `IsLocked` TINYINT(1) NOT NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `ResourceID` (`ResourceID` ASC),
  INDEX `PlaceID` (`PlaceID` ASC),
  INDEX `NoDuplicates` (`PlaceID` ASC, `ResourceID` ASC),
  INDEX `PlacesPlacesResourceEvents` (`PlaceID` ASC),
  INDEX `PlaceResourceID` (`PlaceResourceID` ASC),
  PRIMARY KEY (`PlaceResourceID`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.PlacesResourceMediaEvents
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`PlacesResourceMediaEvents` (
  `PlaceResourceID` INT(10) NOT NULL,
  `MediaID` INT(10) NOT NULL,
  `RelationshipDescription` VARCHAR(255) NULL,
  `Pages` VARCHAR(50) NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `SpeciesID` (`MediaID` ASC),
  INDEX `PlaceResourceID` (`PlaceResourceID` ASC),
  PRIMARY KEY (`PlaceResourceID`, `MediaID`),
  INDEX `PlacesResourceEventsPlacesResourceMediaEvents` (`PlaceResourceID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupAuthorType
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupAuthorType` (
  `AuthorType` VARCHAR(50) NOT NULL,
  UNIQUE INDEX `PK_LookupDocumentAuthorType` (`AuthorType` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.People
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`People` (
  `PersonID` INT(10) NOT NULL,
  `FirstName` VARCHAR(255) NULL,
  `LastName` VARCHAR(255) NULL,
  `YearBorn` INT(10) NULL,
  `Village` VARCHAR(255) NULL,
  `RelationshipToOtherPeople` LONGTEXT NULL,
  INDEX `PersonID` (`PersonID` ASC),
  PRIMARY KEY (`PersonID`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupResourceGroup
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupResourceGroup` (
  `ResourceClassificationGroup` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`ResourceClassificationGroup`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.Resources
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`Resources` (
  `ResourceID` INT(10) NOT NULL,
  `CommonName` VARCHAR(255) NULL,
  `IndigenousName` VARCHAR(255) NULL,
  `Genus` VARCHAR(255) NULL,
  `Species` VARCHAR(255) NULL,
  `Specific` TINYINT(1) NOT NULL,
  `ResourceClassificationGroup` VARCHAR(255) NULL,
  `IsLocked` TINYINT(1) NOT NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `SpeciesID` (`ResourceID` ASC),
  PRIMARY KEY (`ResourceID`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.ResourceActivityMediaEvents
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`ResourceActivityMediaEvents` (
  `ResourceActivityID` INT(10) NOT NULL,
  `MediaID` INT(10) NOT NULL,
  `RelationshipDescription` VARCHAR(255) NULL,
  `Pages` VARCHAR(50) NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `SpeciesID` (`MediaID` ASC),
  INDEX `ResourcesActivityEventsResourceActivityMediaEvents` (`ResourceActivityID` ASC),
  PRIMARY KEY (`ResourceActivityID`, `MediaID`),
  INDEX `ResourceActivityID` (`ResourceActivityID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupTribe
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupTribe` (
  `ID` INT(10) NOT NULL,
  `TribeUnit` VARCHAR(50) NULL,
  `Tribe` VARCHAR(100) NULL,
  `FederalTribe` VARCHAR(100) NULL,
  PRIMARY KEY (`ID`));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LocalityPlaceResourceEvent
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LocalityPlaceResourceEvent` (
  `PlaceResourceID` INT(10) NOT NULL,
  `LocalityID` INT(10) NOT NULL,
  `EnteredByName` VARCHAR(25) NULL,
  `EnteredByTribe` VARCHAR(100) NULL,
  `EnteredByTitle` VARCHAR(100) NULL,
  `EnteredByDate` DATETIME NULL,
  `ModifiedByName` VARCHAR(25) NULL,
  `ModifiedByTitle` VARCHAR(100) NULL,
  `ModifiedByTribe` VARCHAR(100) NULL,
  `ModifiedByDate` DATETIME NULL,
  INDEX `LocalityLocalityPlaceResourceEvent` (`LocalityID` ASC),
  INDEX `LocalityID` (`LocalityID` ASC),
  INDEX `PlacesResourceEventsLocalityPlaceResourceEvent` (`PlaceResourceID` ASC),
  PRIMARY KEY (`PlaceResourceID`, `LocalityID`),
  INDEX `PlaceResourceID` (`PlaceResourceID` ASC));

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.PlaceGISSelections
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`PlaceGISSelections` (
  `PlaceID` INT(10) NULL,
  `PlaceLabel` VARCHAR(255) NULL,
  `SourceFC` VARCHAR(255) NULL);

-- ----------------------------------------------------------------------------
-- Table ethnographic_elements_be.LookupPlanningUnit
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ethnographic_elements_be`.`LookupPlanningUnit` (
  `PlanningUnitID` INT(10) NOT NULL,
  `PlanningUnitName` VARCHAR(100) NULL,
  INDEX `PlanningUnitID` (`PlanningUnitID` ASC),
  PRIMARY KEY (`PlanningUnitID`));
SET FOREIGN_KEY_CHECKS = 1;
