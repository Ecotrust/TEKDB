/* --- LAYERS --*/
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

/* ---- STYLES ---- */

const default_stroke_color = '#FF6000';
const default_fill_opacity = 0.4;
const default_fill_color = 'rgba(255, 96, 0, ' + default_fill_opacity + ')';
const selected_stroke_color = '#b44ba3';
const selected_fill_color = 'rgba(180,75,163,' + default_fill_opacity + ')';

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

const selectStyle = new ol.style.Style({
  fill: new ol.style.Fill({
    color: selected_fill_color,
  }),
  stroke: new ol.style.Stroke({
    color: selected_stroke_color,
    width: 2,
  }),
  image: new ol.style.Icon({
    anchor: [0.5, 1],
    anchorXUnits: 'fraction',
    anchorYUnits: 'fraction',
    src: '{{ map_pin_selected }}',
    scale: 0.1
  })
});

const styleFunction = function(feature) {
  var style = feature.getStyle();
  if (!style) {
    style = styles[0]
  }
  if (feature.getGeometry().getType() == 'Point' && feature.get('map_pin')) {
    style.setImage( new ol.style.Icon({
      anchor: [0.5, 1],
      anchorXUnits: 'fraction',
      anchorYUnits: 'fraction',
      src: feature.get('map_pin'),
      scale: 0.1
    }))
  }
  return style;
}

var vectorLayer = new ol.layer.Vector({
  source: new ol.source.Vector({
      format: new ol.format.GeoJSON(),
  }),
  title: 'Place',
  zIndex: 100,
  style: styleFunction,
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

//////////////////////////////////////////////
// Pop-up identifier on map
//////////////////////////////////////////////

// Largely ripped from https://openlayers.org/en/latest/examples/popup.html

/**
 * Elements that make up the popup.
 */
const container = document.getElementById('popup');
const content = document.getElementById('popup-content');
// const closer = document.getElementById('popup-closer');

/**
  * Create an overlay to anchor the popup to the map.
  */
const overlay = new ol.Overlay({
  element: container,
  autoPan: {
    animation: {
      duration: 250,
    },
  },
});

/**
  * Add a click handler to hide the popup.
  * @return {boolean} Don't follow the href.
  */
// closer.onclick = function () {
//   overlay.setPosition(undefined);
//   closer.blur();
//   return false;
// };


/*--- MAP ---*/
var map = new ol.Map({
  controls: ol.control.defaults({
    attributionOptions: ({
      collapsible: false
    })
  }).extend([
    scaleLineControl,
    mousePositionControl
  ]),
  layers: [
    new ol.layer.Group({
      title: 'Overlays',
      layers: [
        vectorLayer,
        esriLabels
      ],
      zIndex: 10
    }),
    new ol.layer.Group({
      'title': 'Base Maps',
      layers: [
        // nautical_charts,
        // esri_2d,
        // osmLayer,
        esriAerial
      ],
      zIndex: 0
    })
  ],
  overlays: [overlay],
  target: 'map',
  view: new ol.View({
    center: [{{ default_lon }}, {{ default_lat }}],
    zoom: {{ default_zoom }},
    minZoom: {{ min_zoom }},
    maxZoom: {{ max_zoom }},
    extent: {{ map_extent }}
  })
});
if (vectorLayer.getSource().getFeatures().length > 0) {
  var geometry_extent = vectorLayer.getSource().getExtent();
  map.getView().fit(geometry_extent,map.getSize());
}
// var layerSwitcher = new ol.control.LayerSwitcher();
// map.addControl(layerSwitcher);

//////////////////////////////////////////////
// SELECT ON HOVER
//////////////////////////////////////////////

// Largely ripped from https://openlayers.org/en/latest/examples/select-hover-features.html

let selected = null;
map.on('pointermove', function(e){
  if (selected !== null) {
    selected.setStyle(undefined);
    selected = null;
  }

  map.forEachFeatureAtPixel(e.pixel, function (f) {
    selected = f;
    f.setStyle(selectStyle);
    return true;
  });

  if (selected) {
    const coordinate = e.coordinate;
    content.innerHTML = '<p>' + selected.get('name') + '</p>';
    overlay.setPosition(coordinate);
  } else {
    overlay.setPosition(undefined);
    // closer.blur();
    return false;
  }

});

