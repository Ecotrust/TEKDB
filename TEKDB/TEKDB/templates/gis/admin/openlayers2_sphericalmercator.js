{% extends "gis/admin/openlayers2_master.js" %}

{% block base_layer %}new OpenLayers.Layer.XYZ( "Aerial",
      "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/${z}/${y}/${x}",
      {sphericalMercator: true, attribution: "<a href='http://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer' target='_blank'\
      >Aerial Sources: Esri, DigitalGlobe, GeoEye, Earthstar Geographics, CNES/Airbus DS, USDA, USGS, AeroGRID, IGN, and the GIS User Community</a>"} );
{% endblock %}

{% block extra_layers %}
var osmLayer = new OpenLayers.Layer.OSM("Streets");

var esri_2d = new OpenLayers.Layer.XYZ( "Topo",
      "https://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/${z}/${y}/${x}",
      {sphericalMercator: true, attribution: "<a href='http://services.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer' target='_blank'\
      >Basemap Sources: Esri, HERE, DeLorme, Intermap, increment P Corp., GEBCO, USGS, FAO, NPS, NRCAN, GeoBase, IGN, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), swisstopo, MapmyIndia, Â© OpenStreetMap contributors, and the GIS User Community</a>"} );

var label_layer = new OpenLayers.Layer.XYZ( "Labels",
      "http://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/${z}/${y}/${x}",
      {sphericalMercator: true, isBaseLayer:false, attribution: "<a href='http://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer' target='_blank'\
      >Labels Sources: Esri, HERE, DeLorme, MapmyIndia, Â© OpenStreetMap contributors, and the GIS user community</a>"} );

var nautical_charts = new OpenLayers.Layer.ArcGIS93Rest("Nautical",
      "http://seamlessrnc.nauticalcharts.noaa.gov/arcgis/rest/services/RNC/NOAA_RNC/ImageServer/exportImage",
      {
          layers: 'null'
      }, {
          isBaseLayer: true,
          numZoomLevels: 19,
          projection: "EPSG:3857",
          buffer: 3,
          attribution: 'NOAA Office of Coast Survey'
      });

{{ module }}.map.addLayers([osmLayer, esri_2d, label_layer, nautical_charts]);
{% endblock %} //extra_layers
