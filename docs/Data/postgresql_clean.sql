

ALTER TABLE MediaCitationEvents ADD CONSTRAINT CitationsMediaCitationEvents FOREIGN KEY (CitationID ) REFERENCES Citations(CitationID ) ON DELETE CASCADE;
ALTER TABLE ResourcesCitationEvents ADD CONSTRAINT CitationsResourcesCitationEvents FOREIGN KEY (CitationID ) REFERENCES Citations(CitationID ) ON DELETE CASCADE;
ALTER TABLE LocalityPlaceResourceEvent ADD CONSTRAINT LocalityLocalityPlaceResourceEvent FOREIGN KEY (LocalityID ) REFERENCES Locality(LocalityID ) ON DELETE CASCADE;
ALTER TABLE MediaCitationEvents ADD CONSTRAINT MediaMediaCitationEvents FOREIGN KEY (MediaID ) REFERENCES Media(MediaID ) ON DELETE CASCADE;
ALTER TABLE PlacesMediaEvents ADD CONSTRAINT MediaPlacesMediaEvents FOREIGN KEY (MediaID ) REFERENCES Media(MediaID );
ALTER TABLE ResourcesMediaEvents ADD CONSTRAINT MediaResourcesMediaEvents FOREIGN KEY (MediaID ) REFERENCES Media(MediaID ) ON DELETE CASCADE;
ALTER TABLE Citations ADD CONSTRAINT PlacesCitationEventsCitations FOREIGN KEY (CitationID ) REFERENCES PlacesCitationEvents(CitationID );
ALTER TABLE Locality ADD CONSTRAINT PlacesLocality FOREIGN KEY (PlaceID ) REFERENCES Places(PlaceID ) ON DELETE CASCADE;
ALTER TABLE PlacesCitationEvents ADD CONSTRAINT PlacesPlacesCitationEvents FOREIGN KEY (PlaceID ) REFERENCES Places(PlaceID ) ON DELETE CASCADE;
ALTER TABLE PlacesMediaEvents ADD CONSTRAINT PlacesPlacesMediaEvents FOREIGN KEY (PlaceID ) REFERENCES Places(PlaceID ) ON DELETE CASCADE;
ALTER TABLE PlacesResourceEvents ADD CONSTRAINT PlacesPlacesResourceEvents FOREIGN KEY (PlaceID ) REFERENCES Places(PlaceID ) ON DELETE CASCADE;
ALTER TABLE LocalityPlaceResourceEvent ADD CONSTRAINT PlacesResourceEventsLocalityPlaceResourceEvent FOREIGN KEY (PlaceResourceID ) REFERENCES PlacesResourceEvents(PlaceResourceID ) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE PlacesResourceCitationEvents ADD CONSTRAINT PlacesResourceEventsPlacesResourceCitationEvents FOREIGN KEY (PlaceResourceID ) REFERENCES PlacesResourceEvents(PlaceResourceID ) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE PlacesResourceMediaEvents ADD CONSTRAINT PlacesResourceEventsPlacesResourceMediaEvents FOREIGN KEY (PlaceResourceID ) REFERENCES PlacesResourceEvents(PlaceResourceID ) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE ResourcesActivityEvents ADD CONSTRAINT PlacesResourceEventsResourcesActivityEvents FOREIGN KEY (PlaceResourceID ) REFERENCES PlacesResourceEvents(PlaceResourceID ) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE ResourceActivityCitationEvents ADD CONSTRAINT ResourcesActivityEventsResourceActivityCitationEvents FOREIGN KEY (ResourceActivityID ) REFERENCES ResourcesActivityEvents(ResourceActivityID ) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE ResourceActivityMediaEvents ADD CONSTRAINT ResourcesActivityEventsResourceActivityMediaEvents FOREIGN KEY (ResourceActivityID ) REFERENCES ResourcesActivityEvents(ResourceActivityID ) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE ResourcesCitationEvents ADD CONSTRAINT ResourcesResourcesCitationEvents FOREIGN KEY (ResourceID ) REFERENCES Resources(ResourceID ) ON DELETE CASCADE;
ALTER TABLE ResourcesMediaEvents ADD CONSTRAINT ResourcesResourcesMediaEvents FOREIGN KEY (ResourceID ) REFERENCES Resources(ResourceID ) ON DELETE CASCADE;