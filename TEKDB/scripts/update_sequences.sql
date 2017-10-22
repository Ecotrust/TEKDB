BEGIN;
-- TEKDB
SELECT setval(pg_get_serial_sequence('"places"','placeid'), coalesce(max("placeid"), 1), max("placeid") IS NOT null) FROM "places";
SELECT setval(pg_get_serial_sequence('"resources"','resourceid'), coalesce(max("resourceid"), 1), max("resourceid") IS NOT null) FROM "resources";
SELECT setval(pg_get_serial_sequence('"resourcesactivityevents"','resourceactivityid'), coalesce(max("resourceactivityid"), 1), max("resourceactivityid") IS NOT null) FROM "resourcesactivityevents";
SELECT setval(pg_get_serial_sequence('"citations"','citationid'), coalesce(max("citationid"), 1), max("citationid") IS NOT null) FROM "citations";
SELECT setval(pg_get_serial_sequence('"locality"','localityid'), coalesce(max("localityid"), 1), max("localityid") IS NOT null) FROM "locality";
SELECT setval(pg_get_serial_sequence('"media"','mediaid'), coalesce(max("mediaid"), 1), max("mediaid") IS NOT null) FROM "media";

-- 'Accounts'
SELECT setval(pg_get_serial_sequence('"useraccess"','accessid'), coalesce(max("accessid"), 1), max("accessid") IS NOT null) FROM "useraccess";
SELECT setval(pg_get_serial_sequence('"users_groups"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "users_groups";
SELECT setval(pg_get_serial_sequence('"users_user_permissions"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "users_user_permissions";
SELECT setval(pg_get_serial_sequence('"users"','userid'), coalesce(max("userid"), 1), max("userid") IS NOT null) FROM "users";

-- 'explore'

-- 'Lookup'
SELECT setval(pg_get_serial_sequence('"lookupplanningunit"','planningunitid'), coalesce(max("planningunitid"), 1), max("planningunitid") IS NOT null) FROM "lookupplanningunit";
SELECT setval(pg_get_serial_sequence('"lookuptribe"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lookuptribe";
SELECT setval(pg_get_serial_sequence('"lookuphabitat"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lookuphabitat";
SELECT setval(pg_get_serial_sequence('"lookupresourcegroup"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lookupresourcegroup";
SELECT setval(pg_get_serial_sequence('"lookuppartused"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lookuppartused";
SELECT setval(pg_get_serial_sequence('"lookupcustomaryuse"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lookupcustomaryuse";
SELECT setval(pg_get_serial_sequence('"lookupseason"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lookupseason";
SELECT setval(pg_get_serial_sequence('"lookuptiming"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lookuptiming";
SELECT setval(pg_get_serial_sequence('"lookupparticipants"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lookupparticipants";
SELECT setval(pg_get_serial_sequence('"lookuptechniques"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lookuptechniques";
SELECT setval(pg_get_serial_sequence('"lookupactivity"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lookupactivity";
SELECT setval(pg_get_serial_sequence('"people"','personid'), coalesce(max("personid"), 1), max("personid") IS NOT null) FROM "people";
SELECT setval(pg_get_serial_sequence('"lookupreferencetype"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lookupreferencetype";
SELECT setval(pg_get_serial_sequence('"lookupauthortype"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lookupauthortype";
SELECT setval(pg_get_serial_sequence('"currentversion"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "currentversion";
SELECT setval(pg_get_serial_sequence('"lookuplocalitytype"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lookuplocalitytype";
SELECT setval(pg_get_serial_sequence('"lookupmediatype"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lookupmediatype";
SELECT setval(pg_get_serial_sequence('"lookupuserinfo"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lookupuserinfo";

-- 'Relationships'
SELECT setval(pg_get_serial_sequence('"placesresourceevents"','placeresourceid'), coalesce(max("placeresourceid"), 1), max("placeresourceid") IS NOT null) FROM "placesresourceevents";
SELECT setval(pg_get_serial_sequence('"placescitationevents"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "placescitationevents";
SELECT setval(pg_get_serial_sequence('"localitygisselections"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "localitygisselections";
SELECT setval(pg_get_serial_sequence('"localityplaceresourceevent"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "localityplaceresourceevent";
SELECT setval(pg_get_serial_sequence('"mediacitationevents"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "mediacitationevents";
SELECT setval(pg_get_serial_sequence('"placealtindigenousname"','altindigenousnameid'), coalesce(max("altindigenousnameid"), 1), max("altindigenousnameid") IS NOT null) FROM "placealtindigenousname";
SELECT setval(pg_get_serial_sequence('"placegisselections"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "placegisselections";
SELECT setval(pg_get_serial_sequence('"placesmediaevents"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "placesmediaevents";
SELECT setval(pg_get_serial_sequence('"placesresourcecitationevents"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "placesresourcecitationevents";
SELECT setval(pg_get_serial_sequence('"placesresourcemediaevents"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "placesresourcemediaevents";
SELECT setval(pg_get_serial_sequence('"resourceactivitycitationevents"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "resourceactivitycitationevents";
SELECT setval(pg_get_serial_sequence('"resourceactivitymediaevents"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "resourceactivitymediaevents";
SELECT setval(pg_get_serial_sequence('"resourcealtindigenousname"','altindigenousnameid'), coalesce(max("altindigenousnameid"), 1), max("altindigenousnameid") IS NOT null) FROM "resourcealtindigenousname";
SELECT setval(pg_get_serial_sequence('"resourceresourceevents"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "resourceresourceevents";
SELECT setval(pg_get_serial_sequence('"resourcescitationevents"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "resourcescitationevents";
SELECT setval(pg_get_serial_sequence('"resourcesmediaevents"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "resourcesmediaevents";

COMMIT;
