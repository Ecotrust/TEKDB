// import map from '../explore/js/results_map.js';

var esriLabels = new ol.layer.Tile({
    title: 'Labels',
    zIndex: 5,
    source: new ol.source.XYZ({
        url: "http://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}.png",
        attributions: [
            "<br/><a href='http://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer' target='_blank'>" +
            "Labels Sources: Esri, HERE, DeLorme, MapmyIndia, Â© OpenStreetMap contributors, and the GIS user community</a>"
        ]
    })
});
var esriAerial = new ol.layer.Tile({
    title: 'Aerial',
    type: 'base', 
    visible: 'true',
    source: new ol.source.XYZ({
        url: "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}.png",
        attributions: [
            "<a href='http://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer' target='_blank'>" +
            "Aerial Sources: Esri, DigitalGlobe, GeoEye, Earthstar Geographics, CNES/Airbus DS, USDA, USGS, AeroGRID, IGN, and the GIS User Community</a>"
        ]
    })
});

var map = new ol.Map({
    layers: [
      new ol.layer.Group({
        title: 'Overlays',
        layers: [
        //   vectorLayer,
          esriLabels
        ],
        zIndex: 10
      }),
      new ol.layer.Group({
        'title': 'Base Maps',
        layers: [
          esriAerial
        ],
        zIndex: 0
      })
    ],
    // overlays: [overlay],
    target: 'map',
    view: new ol.View({
      center: [37.4057, 8.81566],
      zoom: 4,
    })
  });