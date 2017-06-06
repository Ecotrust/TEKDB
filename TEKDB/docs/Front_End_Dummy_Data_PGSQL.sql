--
-- DUMP FILE
--
-- Database is ported from MS Access
--------------------------------------------------------------------
-- Created using "MS Access to PostgreSQL" form http://www.bullzip.com
-- Program Version 5.5.280
--
-- OPTIONS:
--   sourcefilename=C:/Users/mridul/Desktop/EcotrustBackup/frontend to postgres bull/original front end/ethnographic_elements.accdb
--   sourceusername=
--   sourcepassword=** HIDDEN **
--   sourcesystemdatabase=
--   destinationserver=localhost
--   destinationdatabase=TEK_front
--   maintenancedb=postgres
--   dropdatabase=1
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

DROP DATABASE IF EXISTS "TEK_front";
CREATE DATABASE "TEK_front";

-- NOTICE: At this place you need to connect to the new database and run the rest of the statements.

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

INSERT INTO "LocalityGISSelections" ("LocalityID", "LocalityLabel", "SourceFC") VALUES (5, E'Lake Earl', E'Locality (Point)');
-- 1 records

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

INSERT INTO "PlaceGISSelections" ("PlaceID", "PlaceLabel", "SourceFC") VALUES (10, NULL, E'Place (Area)');
-- 1 records

--
-- Table structure for table 'SelectedCitations'
--

DROP TABLE IF EXISTS "SelectedCitations";

CREATE TABLE "SelectedCitations" (
  "CitationID" INTEGER NOT NULL, 
  "IsSelected" BOOLEAN DEFAULT E'0', 
  "IsReSelected" BOOLEAN DEFAULT E'0', 
  PRIMARY KEY ("CitationID")
);

--
-- Dumping data for table 'SelectedCitations'
--

-- 0 records

CREATE INDEX "SelectedCitations_PlaceID" ON "SelectedCitations" ("CitationID");

--
-- Table structure for table 'SelectedLocalities'
--

DROP TABLE IF EXISTS "SelectedLocalities";

CREATE TABLE "SelectedLocalities" (
  "LocalityID" INTEGER NOT NULL, 
  "IsSelected" BOOLEAN DEFAULT E'0', 
  "IsReSelected" BOOLEAN DEFAULT E'0', 
  PRIMARY KEY ("LocalityID")
);

--
-- Dumping data for table 'SelectedLocalities'
--

-- 0 records

CREATE INDEX "SelectedLocalities_PlaceID" ON "SelectedLocalities" ("LocalityID");

--
-- Table structure for table 'SelectedMedia'
--

DROP TABLE IF EXISTS "SelectedMedia";

CREATE TABLE "SelectedMedia" (
  "MediaID" INTEGER NOT NULL, 
  "IsSelected" BOOLEAN DEFAULT E'0', 
  "IsReSelected" BOOLEAN DEFAULT E'0', 
  PRIMARY KEY ("MediaID")
);

--
-- Dumping data for table 'SelectedMedia'
--

-- 0 records

CREATE INDEX "SelectedMedia_PlaceID" ON "SelectedMedia" ("MediaID");

--
-- Table structure for table 'SelectedPlaceResourceEvents'
--

DROP TABLE IF EXISTS "SelectedPlaceResourceEvents";

CREATE TABLE "SelectedPlaceResourceEvents" (
  "PlaceResourceID" INTEGER NOT NULL, 
  "IsSelected" BOOLEAN DEFAULT E'0', 
  "IsReSelected" BOOLEAN DEFAULT E'0', 
  PRIMARY KEY ("PlaceResourceID")
);

--
-- Dumping data for table 'SelectedPlaceResourceEvents'
--

-- 0 records

CREATE INDEX "SelectedPlaceResourceEvents_PlaceID" ON "SelectedPlaceResourceEvents" ("PlaceResourceID");

--
-- Table structure for table 'SelectedPlaces'
--

DROP TABLE IF EXISTS "SelectedPlaces";

CREATE TABLE "SelectedPlaces" (
  "PlaceID" INTEGER NOT NULL, 
  "IsSelected" BOOLEAN DEFAULT E'0', 
  "IsReSelected" BOOLEAN DEFAULT E'0', 
  PRIMARY KEY ("PlaceID")
);

--
-- Dumping data for table 'SelectedPlaces'
--

-- 0 records

CREATE INDEX "SelectedPlaces_PlaceID" ON "SelectedPlaces" ("PlaceID");

--
-- Table structure for table 'SelectedResourceActivityEvents'
--

DROP TABLE IF EXISTS "SelectedResourceActivityEvents";

CREATE TABLE "SelectedResourceActivityEvents" (
  "ResourceActivityID" INTEGER NOT NULL, 
  "IsSelected" BOOLEAN DEFAULT E'0', 
  "IsReSelected" BOOLEAN DEFAULT E'0', 
  PRIMARY KEY ("ResourceActivityID")
);

--
-- Dumping data for table 'SelectedResourceActivityEvents'
--

-- 0 records

CREATE INDEX "SelectedResourceActivityEvents_PlaceID" ON "SelectedResourceActivityEvents" ("ResourceActivityID");

--
-- Table structure for table 'SelectedResources'
--

DROP TABLE IF EXISTS "SelectedResources";

CREATE TABLE "SelectedResources" (
  "ResourceID" INTEGER NOT NULL, 
  "IsSelected" BOOLEAN DEFAULT E'0', 
  "IsReSelected" BOOLEAN DEFAULT E'0', 
  PRIMARY KEY ("ResourceID")
);

--
-- Dumping data for table 'SelectedResources'
--

INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (150, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (151, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (152, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (153, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (154, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (155, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (156, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (157, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (158, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (159, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (160, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (161, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (162, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (163, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (164, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (165, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (166, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (167, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (168, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (169, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (170, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (171, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (172, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (173, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (174, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (175, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (176, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (177, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (178, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (179, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (180, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (181, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (182, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (183, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (184, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (185, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (186, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (187, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (188, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (189, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (190, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (191, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (192, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (193, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (194, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (195, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (196, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (197, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (198, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (199, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (200, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (201, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (202, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (203, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (204, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (205, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (206, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (207, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (208, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (209, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (210, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (211, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (212, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (213, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (214, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (215, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (216, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (217, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (218, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (219, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (220, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (221, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (222, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (223, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (224, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (225, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (226, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (227, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (228, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (229, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (230, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (231, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (232, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (233, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (234, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (235, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (236, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (237, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (238, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (239, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (240, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (241, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (242, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (243, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (244, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (245, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (246, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (247, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (248, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (249, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (250, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (251, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (252, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (253, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (254, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (255, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (256, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (257, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (258, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (259, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (260, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (261, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (262, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (263, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (264, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (265, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (266, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (267, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (268, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (269, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (270, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (271, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (272, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (273, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (274, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (275, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (276, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (277, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (278, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (279, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (280, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (281, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (282, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (283, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (284, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (285, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (286, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (287, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (288, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (289, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (290, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (291, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (292, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (293, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (294, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (295, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (296, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (297, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (298, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (299, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (300, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (301, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (302, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (303, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (304, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (305, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (306, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (307, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (308, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (309, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (310, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (311, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (312, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (313, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (314, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (315, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (316, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (317, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (318, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (319, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (320, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (321, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (322, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (323, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (324, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (325, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (326, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (327, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (328, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (329, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (330, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (331, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (332, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (333, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (334, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (335, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (336, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (337, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (338, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (339, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (340, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (341, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (342, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (343, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (344, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (345, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (346, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (347, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (348, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (349, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (350, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (351, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (352, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (353, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (354, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (355, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (356, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (357, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (358, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (359, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (360, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (361, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (362, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (363, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (364, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (365, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (366, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (367, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (368, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (369, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (370, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (371, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (372, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (373, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (374, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (375, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (376, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (377, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (378, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (379, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (380, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (381, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (382, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (383, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (384, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (385, E'0', E'0');
INSERT INTO "SelectedResources" ("ResourceID", "IsSelected", "IsReSelected") VALUES (386, E'0', E'0');
-- 237 records

CREATE INDEX "SelectedResources_PlaceID" ON "SelectedResources" ("ResourceID");

--
-- Table structure for table 'TableListing'
--

DROP TABLE IF EXISTS "TableListing";

CREATE TABLE "TableListing" (
  "ID" SERIAL NOT NULL, 
  "Table" VARCHAR(255), 
  "PrimaryKey" VARCHAR(255), 
  "TableStatus" VARCHAR(255), 
  "Import" BOOLEAN DEFAULT E'0', 
  PRIMARY KEY ("ID")
);

--
-- Dumping data for table 'TableListing'
--

INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (235, E'Citations', E'CitationID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (236, E'CurrentVersion', E'ID', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (237, E'Locality', E'LocalityID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (238, E'LocalityGISSelections', E'NA', E'TABLE', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (239, E'LocalityPlaceResourceEvent', E'LocalityID, PlaceResourceID', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (240, E'LookupActivity', E'Activity', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (241, E'LookupAuthorType', E'AuthorType', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (242, E'LookupCustomaryUse', E'UsedFor', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (243, E'LookupHabitat', E'Habitat', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (244, E'LookupLocalityType', E'LocalityType', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (245, E'LookupMediaType', E'MediaType', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (246, E'LookupParticipants', E'Participants', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (247, E'LookupPartUsed', E'PartUsed', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (248, E'LookupPlanningUnit', E'PlanningUnitID', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (249, E'LookupReferenceType', E'DocumentType', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (250, E'LookupResourceGroup', E'ResourceClassificationGroup', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (251, E'LookupSeason', E'Season', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (252, E'LookupTechniques', E'Techniques', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (253, E'LookupTiming', E'Timing', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (254, E'LookupTribe', E'ID', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (255, E'LookupUserInfo', E'NA', E'TABLE', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (256, E'Media', E'MediaID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (257, E'MediaCitationEvents', E'CitationID, MediaID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (258, E'People', E'PersonID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (259, E'PlaceAltIndigenousName', E'AltIndigenousNameID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (260, E'PlaceGISSelections', E'NA', E'TABLE', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (261, E'Places', E'PlaceID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (262, E'PlacesCitationEvents', E'CitationID, PlaceID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (263, E'PlacesMediaEvents', E'MediaID, PlaceID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (264, E'PlacesResourceCitationEvents', E'CitationID, PlaceResourceID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (265, E'PlacesResourceEvents', E'PlaceResourceID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (266, E'PlacesResourceMediaEvents', E'MediaID, PlaceResourceID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (267, E'PlacesResourceSelections', E'NA', E'VIEW', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (268, E'ResourceActivityCitationEvents', E'CitationID, ResourceActivityID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (269, E'ResourceActivityMediaEvents', E'MediaID, ResourceActivityID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (270, E'ResourceActivitySelections', E'NA', E'VIEW', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (271, E'ResourceAltIndigenousName', E'AltIndigenousNameID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (272, E'ResourceResourceEvents', E'AltResourceID, ResourceID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (273, E'Resources', E'ResourceID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (274, E'ResourcesActivityEvents', E'ResourceActivityID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (275, E'ResourcesCitationEvents', E'CitationID, ResourceID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (276, E'ResourcesMediaEvents', E'MediaID, ResourceID', E'LINK', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (277, E'SelectedCitations', E'CitationID', E'TABLE', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (278, E'SelectedLocalities', E'LocalityID', E'TABLE', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (279, E'SelectedMedia', E'MediaID', E'TABLE', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (280, E'SelectedPlaceResourceEvents', E'PlaceResourceID', E'TABLE', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (281, E'SelectedPlaces', E'PlaceID', E'TABLE', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (282, E'SelectedResourceActivityEvents', E'ResourceActivityID', E'TABLE', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (283, E'SelectedResources', E'ResourceID', E'TABLE', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (284, E'TableListing', E'ID', E'TABLE', E'1');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (285, E'UserAccess', E'AccessID', E'LINK', E'0');
INSERT INTO "TableListing" ("ID", "Table", "PrimaryKey", "TableStatus", "Import") VALUES (286, E'Users', E'UserID', E'LINK', E'0');
-- 52 records

SELECT setval('"TableListing_ID_seq"', MAX("ID")) FROM "TableListing";

CREATE INDEX "TableListing_ID" ON "TableListing" ("ID");

CREATE INDEX "TableListing_PrimaryKey" ON "TableListing" ("PrimaryKey");

