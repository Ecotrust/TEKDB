/* ---- STYLES ---- */

const default_stroke_color = '#FF6000';
const default_fill_opacity = 0.4;
const default_fill_color = 'rgba(255, 96, 0, ' + default_fill_opacity + ')';

const fill = new ol.style.Fill({
  color: default_fill_color,
});
const stroke = new ol.style.Stroke({
  color: default_stroke_color,
  width: 1.25,
});
const styles = [
  new ol.style.Style({
    image: new ol.style.Circle({
      fill: fill,
      stroke: stroke,
      radius: 5,
    }),
    fill: fill,
    stroke: stroke,
  }),
];

const styleFunction = function(feature) {
  var style = feature.getStyle();
  if (!style) {
    style = styles[0]
  }
  console.log("Feature geometry type: " + feature.getGeometry().getType());
  {% comment %} if (feature.getGeometry().getType() == 'Point' && "{{ map_pin }}" != "") {
    style.setImage( new ol.style.Icon({
      anchor: [0.5, 1],
      anchorXUnits: 'fraction',
      anchorYUnits: 'fraction',
      src: '{{ map_pin }}',
      scale: 0.1
    }))
  } {% endcomment %}
  return style;
}

/* --- LAYERS --*/
var esriLabels = new ol.layer.Tile({
  title: 'Labels',
  zIndex: 5,
  source: new ol.source.XYZ({
    url: "http://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}.png",
    attributions: [
      "<br/><a href='http://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer' target='_blank'>\
        Labels Sources: Esri, HERE, DeLorme, MapmyIndia, Â© OpenStreetMap contributors, and the GIS user community</a>"
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
      "<a href='http://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer' target='_blank'>\
        Aerial Sources: Esri, DigitalGlobe, GeoEye, Earthstar Geographics, CNES/Airbus DS, USDA, USGS, AeroGRID, IGN, and the GIS User Community</a>"
    ]
  })
});


/* --- CONTROLS --*/
var scaleLineControl = new ol.control.ScaleLine({
units: 'us'
});
var mousePositionControl = new ol.control.MousePosition({
coordinateFormat: ol.coordinate.createStringXY(4),
projection: 'EPSG:4326',
target: 'mouse-position',
undefinedHTML: '&nbsp;'
});

/*--- MAP ZOOM ---*/
function buffer_extent(extent, buffer) {
  let lat_total = extent[2] - extent[0];
  let lon_total = extent[3] - extent[1];
  let lat_buffer = lat_total*buffer;
  let lon_buffer = lon_total*buffer;
  return [
    extent[0]-lat_buffer,
    extent[1]-lon_buffer,
    extent[2]+lat_buffer,
    extent[3]+lon_buffer,
  ];
}

/*--- MAP ---*/
var map = new ol.Map({
  controls: ol.control.defaults({
    attributionOptions: ({
      collapsible: true
    })
  }).extend([
    scaleLineControl,
    mousePositionControl
  ]),
  
  layers: [
    new ol.layer.Group({
      title: 'Overlays',
      layers: [
        esriLabels
      ],
      zIndex: 10
    }),
    new ol.layer.Group({
      'title': 'Base Maps',
      layers: [
        esriAerial,
      ],
      zIndex: 0
    })
  ],
  target: 'map',
  view: new ol.View({
    center: [-124.2, 41.9],
    zoom: 10,
    minZoom: 2,
    maxZoom: 19,
    extent: [-24000000, 1450000, -6200000, 13000000]
  })
});
var vectorLayers = [];
// cam we do the update source thing instead? Can we make all of the features a feature collection? 
/* --- VECTOR LAYERS FOR EACH MAP --- */
{% for link in maps %}
  {% if link.map %}
    var vectorLayer_{{ forloop.counter }} = new ol.layer.Vector({
      source: new ol.source.Vector({
        features: new ol.format.GeoJSON().readFeatures(JSON.parse(`{{ link.map|safe }}`))
      }),
      title: '{{ link.name|escapejs }}',
      zIndex: 100 + {{ forloop.counter }},
      style: styleFunction,
    });
    vectorLayers.push(vectorLayer_{{ forloop.counter }});
    map.addLayer(vectorLayer_{{ forloop.counter }});
  {% endif %}
{% endfor %}

// TODO: fit map to all vector layers
// get extent of all features in all vector layers

for (let i=0; i< vectorLayers.length; i++) {
    let layer = vectorLayers[i];
    if (layer.getSource().getFeatures().length > 0) {
    }
