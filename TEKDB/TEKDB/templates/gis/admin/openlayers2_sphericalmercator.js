{% extends "gis/admin/openlayers2_master.js" %}

{% block base_layer %}new OpenLayers.Layer.XYZ( "ESRI Aerial",
      "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/${z}/${y}/${x}",
      {sphericalMercator: true, attribution: "<a href='http://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer' target='_blank'\
      >Aerial Sources: Esri, DigitalGlobe, GeoEye, Earthstar Geographics, CNES/Airbus DS, USDA, USGS, AeroGRID, IGN, and the GIS User Community</a>"} );
{% endblock %}

{% block extra_layers %}
var osmLayer = new OpenLayers.Layer.OSM("OpenStreetMap");

var esri_2d = new OpenLayers.Layer.XYZ( "ESRI Base",
      "https://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/${z}/${y}/${x}",
      {sphericalMercator: true, attribution: "<a href='http://services.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer' target='_blank'\
      >Basemap Sources: Esri, HERE, DeLorme, Intermap, increment P Corp., GEBCO, USGS, FAO, NPS, NRCAN, GeoBase, IGN, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), swisstopo, MapmyIndia, Â© OpenStreetMap contributors, and the GIS User Community</a>"} );

var label_layer = new OpenLayers.Layer.XYZ( "Place Labels",
      "http://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/${z}/${y}/${x}",
      {sphericalMercator: true, isBaseLayer:false, attribution: "<a href='http://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer' target='_blank'\
      >Labels Sources: Esri, HERE, DeLorme, MapmyIndia, Â© OpenStreetMap contributors, and the GIS user community</a>"} );

{{ module }}.map.addLayers([osmLayer, esri_2d, label_layer]);
{% endblock %} //extra_layers
