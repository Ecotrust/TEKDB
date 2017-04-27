--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner:
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner:
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: Citations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Citations" (
    "CitationID" integer NOT NULL,
    "ReferenceType" character varying(255),
    "ReferenceText" character varying(50),
    "AuthorType" character varying(255),
    "AuthorPrimary" character varying(255),
    "AuthorSecondary" character varying(255),
    "IntervieweeID" integer,
    "InterviewerID" integer,
    "PlaceofInterview" character varying(255),
    "Year" integer,
    "Title" text,
    "SeriesTitle" character varying(255),
    "SeriesVolume" character varying(50),
    "SeriesEditor" character varying(255),
    "Publisher" character varying(100),
    "PublisherCity" character varying(255),
    "PreparedFor" character varying(100),
    "Comments" text,
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "Citations" OWNER TO postgres;

--
-- Name: Citations_CitationID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Citations_CitationID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Citations_CitationID_seq" OWNER TO postgres;

--
-- Name: Citations_CitationID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Citations_CitationID_seq" OWNED BY "Citations"."CitationID";


--
-- Name: CurrentVersion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "CurrentVersion" (
    "ID" integer NOT NULL,
    "BackendVersion" integer,
    "FrontendVersion" integer
);


ALTER TABLE "CurrentVersion" OWNER TO postgres;

--
-- Name: CurrentVersion_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "CurrentVersion_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "CurrentVersion_ID_seq" OWNER TO postgres;

--
-- Name: CurrentVersion_ID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "CurrentVersion_ID_seq" OWNED BY "CurrentVersion"."ID";


--
-- Name: Locality; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Locality" (
    "LocalityID" integer NOT NULL,
    "PlaceID" integer,
    "EnglishName" character varying(255),
    "IndigenousName" character varying(255),
    "LocalityType" character varying(255),
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "Locality" OWNER TO postgres;

--
-- Name: LocalityGISSelections; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LocalityGISSelections" (
    "LocalityID" integer,
    "LocalityLabel" character varying(255),
    "SourceFC" character varying(255)
);


ALTER TABLE "LocalityGISSelections" OWNER TO postgres;

--
-- Name: LocalityPlaceResourceEvent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LocalityPlaceResourceEvent" (
    "PlaceResourceID" integer NOT NULL,
    "LocalityID" integer NOT NULL,
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "LocalityPlaceResourceEvent" OWNER TO postgres;

--
-- Name: Locality_LocalityID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Locality_LocalityID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Locality_LocalityID_seq" OWNER TO postgres;

--
-- Name: Locality_LocalityID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Locality_LocalityID_seq" OWNED BY "Locality"."LocalityID";


--
-- Name: LookupActivity; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupActivity" (
    "Activity" character varying(255) NOT NULL
);


ALTER TABLE "LookupActivity" OWNER TO postgres;

--
-- Name: LookupAuthorType; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupAuthorType" (
    "AuthorType" character varying(50) NOT NULL
);


ALTER TABLE "LookupAuthorType" OWNER TO postgres;

--
-- Name: LookupCustomaryUse; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupCustomaryUse" (
    "UsedFor" character varying(255) NOT NULL
);


ALTER TABLE "LookupCustomaryUse" OWNER TO postgres;

--
-- Name: LookupHabitat; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupHabitat" (
    "Habitat" character varying(100) NOT NULL
);


ALTER TABLE "LookupHabitat" OWNER TO postgres;

--
-- Name: LookupLocalityType; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupLocalityType" (
    "LocalityType" character varying(255) NOT NULL
);


ALTER TABLE "LookupLocalityType" OWNER TO postgres;

--
-- Name: LookupMediaType; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupMediaType" (
    "MediaType" character varying(255) NOT NULL,
    "MediaCategory" character varying(255)
);


ALTER TABLE "LookupMediaType" OWNER TO postgres;

--
-- Name: LookupPartUsed; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupPartUsed" (
    "PartUsed" character varying(255) NOT NULL
);


ALTER TABLE "LookupPartUsed" OWNER TO postgres;

--
-- Name: LookupParticipants; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupParticipants" (
    "Participants" character varying(255) NOT NULL
);


ALTER TABLE "LookupParticipants" OWNER TO postgres;

--
-- Name: LookupPlanningUnit; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupPlanningUnit" (
    "PlanningUnitID" integer NOT NULL,
    "PlanningUnitName" character varying(100)
);


ALTER TABLE "LookupPlanningUnit" OWNER TO postgres;

--
-- Name: LookupReferenceType; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupReferenceType" (
    "DocumentType" character varying(25) NOT NULL
);


ALTER TABLE "LookupReferenceType" OWNER TO postgres;

--
-- Name: LookupResourceGroup; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupResourceGroup" (
    "ResourceClassificationGroup" character varying(255) NOT NULL
);


ALTER TABLE "LookupResourceGroup" OWNER TO postgres;

--
-- Name: LookupSeason; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupSeason" (
    "Season" character varying(255) NOT NULL
);


ALTER TABLE "LookupSeason" OWNER TO postgres;

--
-- Name: LookupTechniques; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupTechniques" (
    "Techniques" character varying(255) NOT NULL
);


ALTER TABLE "LookupTechniques" OWNER TO postgres;

--
-- Name: LookupTiming; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupTiming" (
    "Timing" character varying(255) NOT NULL
);


ALTER TABLE "LookupTiming" OWNER TO postgres;

--
-- Name: LookupTribe; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupTribe" (
    "ID" integer NOT NULL,
    "TribeUnit" character varying(50),
    "Tribe" character varying(100),
    "FederalTribe" character varying(100)
);


ALTER TABLE "LookupTribe" OWNER TO postgres;

--
-- Name: LookupTribe_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "LookupTribe_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "LookupTribe_ID_seq" OWNER TO postgres;

--
-- Name: LookupTribe_ID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "LookupTribe_ID_seq" OWNED BY "LookupTribe"."ID";


--
-- Name: LookupUserInfo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "LookupUserInfo" (
    "UserName" character varying(100),
    "UsingCustomUsername" boolean DEFAULT false,
    "UserTitle" character varying(100),
    "UserAffiliation" character varying(100)
);


ALTER TABLE "LookupUserInfo" OWNER TO postgres;

--
-- Name: Media; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Media" (
    "MediaID" integer NOT NULL,
    "MediaType" character varying(255),
    "MediaName" character varying(255),
    "MediaDescription" text,
    "MediaLink" character varying(255),
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "Media" OWNER TO postgres;

--
-- Name: MediaCitationEvents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "MediaCitationEvents" (
    "MediaID" integer NOT NULL,
    "CitationID" integer NOT NULL,
    "RelationshipDescription" character varying(255),
    "Pages" character varying(255),
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "MediaCitationEvents" OWNER TO postgres;

--
-- Name: Media_MediaID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Media_MediaID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Media_MediaID_seq" OWNER TO postgres;

--
-- Name: Media_MediaID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Media_MediaID_seq" OWNED BY "Media"."MediaID";


--
-- Name: People; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "People" (
    "PersonID" integer NOT NULL,
    "FirstName" character varying(255),
    "LastName" character varying(255),
    "YearBorn" integer,
    "Village" character varying(255),
    "RelationshipToOtherPeople" text
);


ALTER TABLE "People" OWNER TO postgres;

--
-- Name: People_PersonID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "People_PersonID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "People_PersonID_seq" OWNER TO postgres;

--
-- Name: People_PersonID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "People_PersonID_seq" OWNED BY "People"."PersonID";


--
-- Name: PlaceAltIndigenousName; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "PlaceAltIndigenousName" (
    "AltIndigenousNameID" integer NOT NULL,
    "PlaceID" integer,
    "AltIndigenousName" character varying(255)
);


ALTER TABLE "PlaceAltIndigenousName" OWNER TO postgres;

--
-- Name: PlaceAltIndigenousName_AltIndigenousNameID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "PlaceAltIndigenousName_AltIndigenousNameID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "PlaceAltIndigenousName_AltIndigenousNameID_seq" OWNER TO postgres;

--
-- Name: PlaceAltIndigenousName_AltIndigenousNameID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "PlaceAltIndigenousName_AltIndigenousNameID_seq" OWNED BY "PlaceAltIndigenousName"."AltIndigenousNameID";


--
-- Name: PlaceGISSelections; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "PlaceGISSelections" (
    "PlaceID" integer,
    "PlaceLabel" character varying(255),
    "SourceFC" character varying(255)
);


ALTER TABLE "PlaceGISSelections" OWNER TO postgres;

--
-- Name: Places; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Places" (
    "PlaceID" integer NOT NULL,
    "IndigenousPlaceName" character varying(255),
    "IndigenousPlaceNameMeaning" character varying(255),
    "EnglishPlaceName" character varying(255),
    "PlanningUnitID" integer DEFAULT 0,
    "PrimaryHabitat" character varying(100),
    "TribeID" integer,
    "IsLocked" boolean DEFAULT false,
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "Places" OWNER TO postgres;

--
-- Name: PlacesCitationEvents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "PlacesCitationEvents" (
    "PlaceID" integer NOT NULL,
    "CitationID" integer NOT NULL,
    "RelationshipDescription" character varying(255),
    "Pages" character varying(255),
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "PlacesCitationEvents" OWNER TO postgres;

--
-- Name: PlacesMediaEvents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "PlacesMediaEvents" (
    "PlaceID" integer NOT NULL,
    "MediaID" integer NOT NULL,
    "RelationshipDescription" character varying(255),
    "Pages" character varying(50),
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "PlacesMediaEvents" OWNER TO postgres;

--
-- Name: PlacesResourceCitationEvents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "PlacesResourceCitationEvents" (
    "PlaceResourceID" integer NOT NULL,
    "CitationID" integer NOT NULL,
    "RelationshipDescription" character varying(255),
    "Pages" character varying(255),
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "PlacesResourceCitationEvents" OWNER TO postgres;

--
-- Name: PlacesResourceEvents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "PlacesResourceEvents" (
    "PlaceResourceID" integer NOT NULL,
    "PlaceID" integer NOT NULL,
    "ResourceID" integer NOT NULL,
    "RelationshipDescription" character varying(255),
    "PartUsed" character varying(255),
    "CustomaryUse" character varying(255),
    "BarterResource" boolean DEFAULT false,
    "Season" character varying(255),
    "Timing" character varying(255),
    "January" boolean DEFAULT false,
    "February" boolean DEFAULT false,
    "March" boolean DEFAULT false,
    "April" boolean DEFAULT false,
    "May" boolean DEFAULT false,
    "June" boolean DEFAULT false,
    "July" boolean DEFAULT false,
    "August" boolean DEFAULT false,
    "September" boolean DEFAULT false,
    "October" boolean DEFAULT false,
    "November" boolean DEFAULT false,
    "December" boolean DEFAULT false,
    "Year" integer,
    "IsLocked" boolean DEFAULT false,
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "PlacesResourceEvents" OWNER TO postgres;

--
-- Name: PlacesResourceEvents_PlaceResourceID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "PlacesResourceEvents_PlaceResourceID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "PlacesResourceEvents_PlaceResourceID_seq" OWNER TO postgres;

--
-- Name: PlacesResourceEvents_PlaceResourceID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "PlacesResourceEvents_PlaceResourceID_seq" OWNED BY "PlacesResourceEvents"."PlaceResourceID";


--
-- Name: PlacesResourceMediaEvents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "PlacesResourceMediaEvents" (
    "PlaceResourceID" integer NOT NULL,
    "MediaID" integer NOT NULL,
    "RelationshipDescription" character varying(255),
    "Pages" character varying(50),
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "PlacesResourceMediaEvents" OWNER TO postgres;

--
-- Name: Places_PlaceID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Places_PlaceID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Places_PlaceID_seq" OWNER TO postgres;

--
-- Name: Places_PlaceID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Places_PlaceID_seq" OWNED BY "Places"."PlaceID";


--
-- Name: ResourceActivityCitationEvents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "ResourceActivityCitationEvents" (
    "ResourceActivityID" integer NOT NULL,
    "CitationID" integer NOT NULL,
    "RelationshipDescription" character varying(255),
    "Pages" character varying(255),
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "ResourceActivityCitationEvents" OWNER TO postgres;

--
-- Name: ResourceActivityMediaEvents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "ResourceActivityMediaEvents" (
    "ResourceActivityID" integer NOT NULL,
    "MediaID" integer NOT NULL,
    "RelationshipDescription" character varying(255),
    "Pages" character varying(50),
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "ResourceActivityMediaEvents" OWNER TO postgres;

--
-- Name: ResourceAltIndigenousName; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "ResourceAltIndigenousName" (
    "AltIndigenousNameID" integer NOT NULL,
    "ResourceID" integer,
    "AltIndigenousName" character varying(255)
);


ALTER TABLE "ResourceAltIndigenousName" OWNER TO postgres;

--
-- Name: ResourceAltIndigenousName_AltIndigenousNameID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "ResourceAltIndigenousName_AltIndigenousNameID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "ResourceAltIndigenousName_AltIndigenousNameID_seq" OWNER TO postgres;

--
-- Name: ResourceAltIndigenousName_AltIndigenousNameID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "ResourceAltIndigenousName_AltIndigenousNameID_seq" OWNED BY "ResourceAltIndigenousName"."AltIndigenousNameID";


--
-- Name: ResourceResourceEvents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "ResourceResourceEvents" (
    "ResourceID" integer NOT NULL,
    "AltResourceID" integer NOT NULL,
    "RelationshipDescription" character varying(255),
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "ResourceResourceEvents" OWNER TO postgres;

--
-- Name: Resources; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Resources" (
    "ResourceID" integer NOT NULL,
    "CommonName" character varying(255),
    "IndigenousName" character varying(255),
    "Genus" character varying(255),
    "Species" character varying(255),
    "Specific" boolean DEFAULT false,
    "ResourceClassificationGroup" character varying(255),
    "IsLocked" boolean DEFAULT false,
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "Resources" OWNER TO postgres;

--
-- Name: ResourcesActivityEvents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "ResourcesActivityEvents" (
    "ResourceActivityID" integer NOT NULL,
    "PlaceResourceID" integer NOT NULL,
    "RelationshipDescription" text,
    "PartUsed" character varying(255),
    "ActivityShortDescription" character varying(255),
    "ActivityLongDescription" text,
    "Participants" character varying(50),
    "Technique" character varying(255),
    "Gear" character varying(255),
    "CustomaryUse" character varying(255),
    "Timing" character varying(255),
    "TimingDescription" character varying(255),
    "IsLocked" boolean DEFAULT false,
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "ResourcesActivityEvents" OWNER TO postgres;

--
-- Name: ResourcesActivityEvents_ResourceActivityID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "ResourcesActivityEvents_ResourceActivityID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "ResourcesActivityEvents_ResourceActivityID_seq" OWNER TO postgres;

--
-- Name: ResourcesActivityEvents_ResourceActivityID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "ResourcesActivityEvents_ResourceActivityID_seq" OWNED BY "ResourcesActivityEvents"."ResourceActivityID";


--
-- Name: ResourcesCitationEvents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "ResourcesCitationEvents" (
    "ResourceID" integer NOT NULL,
    "CitationID" integer NOT NULL,
    "RelationshipDescription" character varying(255),
    "Pages" character varying(255),
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "ResourcesCitationEvents" OWNER TO postgres;

--
-- Name: ResourcesMediaEvents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "ResourcesMediaEvents" (
    "ResourceID" integer NOT NULL,
    "MediaID" integer NOT NULL,
    "RelationshipDescription" character varying(255),
    "Pages" character varying(50),
    "EnteredByName" character varying(25),
    "EnteredByTribe" character varying(100),
    "EnteredByTitle" character varying(100),
    "EnteredByDate" timestamp without time zone DEFAULT now(),
    "ModifiedByName" character varying(25),
    "ModifiedByTitle" character varying(100),
    "ModifiedByTribe" character varying(100),
    "ModifiedByDate" timestamp without time zone
);


ALTER TABLE "ResourcesMediaEvents" OWNER TO postgres;

--
-- Name: Resources_ResourceID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Resources_ResourceID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Resources_ResourceID_seq" OWNER TO postgres;

--
-- Name: Resources_ResourceID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Resources_ResourceID_seq" OWNED BY "Resources"."ResourceID";


--
-- Name: UserAccess; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "UserAccess" (
    "AccessID" integer NOT NULL,
    "AccessLevel" character varying(255)
);


ALTER TABLE "UserAccess" OWNER TO postgres;

--
-- Name: UserAccess_AccessID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "UserAccess_AccessID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "UserAccess_AccessID_seq" OWNER TO postgres;

--
-- Name: UserAccess_AccessID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "UserAccess_AccessID_seq" OWNED BY "UserAccess"."AccessID";


--
-- Name: Users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Users" (
    "UserID" integer NOT NULL,
    "UserName" character varying(20) NOT NULL,
    "Password" character varying(20) NOT NULL,
    "FirstName" character varying(255) NOT NULL,
    "LastName" character varying(255) NOT NULL,
    "Affiliation" character varying(255) NOT NULL,
    "Title" character varying(255) NOT NULL,
    "AccessLevel" integer NOT NULL
);


ALTER TABLE "Users" OWNER TO postgres;

--
-- Name: Users_UserID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Users_UserID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Users_UserID_seq" OWNER TO postgres;

--
-- Name: Users_UserID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Users_UserID_seq" OWNED BY "Users"."UserID";


--
-- Name: CitationID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Citations" ALTER COLUMN "CitationID" SET DEFAULT nextval('"Citations_CitationID_seq"'::regclass);


--
-- Name: ID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "CurrentVersion" ALTER COLUMN "ID" SET DEFAULT nextval('"CurrentVersion_ID_seq"'::regclass);


--
-- Name: LocalityID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Locality" ALTER COLUMN "LocalityID" SET DEFAULT nextval('"Locality_LocalityID_seq"'::regclass);


--
-- Name: ID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "LookupTribe" ALTER COLUMN "ID" SET DEFAULT nextval('"LookupTribe_ID_seq"'::regclass);


--
-- Name: MediaID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Media" ALTER COLUMN "MediaID" SET DEFAULT nextval('"Media_MediaID_seq"'::regclass);


--
-- Name: PersonID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "People" ALTER COLUMN "PersonID" SET DEFAULT nextval('"People_PersonID_seq"'::regclass);


--
-- Name: AltIndigenousNameID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "PlaceAltIndigenousName" ALTER COLUMN "AltIndigenousNameID" SET DEFAULT nextval('"PlaceAltIndigenousName_AltIndigenousNameID_seq"'::regclass);


--
-- Name: PlaceID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Places" ALTER COLUMN "PlaceID" SET DEFAULT nextval('"Places_PlaceID_seq"'::regclass);


--
-- Name: PlaceResourceID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "PlacesResourceEvents" ALTER COLUMN "PlaceResourceID" SET DEFAULT nextval('"PlacesResourceEvents_PlaceResourceID_seq"'::regclass);


--
-- Name: AltIndigenousNameID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "ResourceAltIndigenousName" ALTER COLUMN "AltIndigenousNameID" SET DEFAULT nextval('"ResourceAltIndigenousName_AltIndigenousNameID_seq"'::regclass);


--
-- Name: ResourceID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Resources" ALTER COLUMN "ResourceID" SET DEFAULT nextval('"Resources_ResourceID_seq"'::regclass);


--
-- Name: ResourceActivityID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "ResourcesActivityEvents" ALTER COLUMN "ResourceActivityID" SET DEFAULT nextval('"ResourcesActivityEvents_ResourceActivityID_seq"'::regclass);


--
-- Name: AccessID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "UserAccess" ALTER COLUMN "AccessID" SET DEFAULT nextval('"UserAccess_AccessID_seq"'::regclass);


--
-- Name: UserID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Users" ALTER COLUMN "UserID" SET DEFAULT nextval('"Users_UserID_seq"'::regclass);


--
-- Data for Name: Citations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Citations" ("CitationID", "ReferenceType", "ReferenceText", "AuthorType", "AuthorPrimary", "AuthorSecondary", "IntervieweeID", "InterviewerID", "PlaceofInterview", "Year", "Title", "SeriesTitle", "SeriesVolume", "SeriesEditor", "Publisher", "PublisherCity", "PreparedFor", "Comments", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") FROM stdin;
\.


--
-- Name: Citations_CitationID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"Citations_CitationID_seq"', 1, false);


--
-- Data for Name: CurrentVersion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "CurrentVersion" ("ID", "BackendVersion", "FrontendVersion") FROM stdin;
1	1	1
\.


--
-- Name: CurrentVersion_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"CurrentVersion_ID_seq"', 1, true);


--
-- Data for Name: Locality; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Locality" ("LocalityID", "PlaceID", "EnglishName", "IndigenousName", "LocalityType", "EnteredByName", "EnteredByTribe", "EnteredByTitle", "EnteredByDate", "ModifiedByName", "ModifiedByTitle", "ModifiedByTribe", "ModifiedByDate") FROM stdin;
\.


--
-- Data for Name: LocalityGISSelections; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY
