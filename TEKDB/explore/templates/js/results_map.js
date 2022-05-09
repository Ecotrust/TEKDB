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
// var esri_2d = new ol.layer.Tile({
//   title: 'Topo',
//   type: 'base',
//   source: new ol.source.XYZ({
//       url: "https://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}",
//       attributions: [
//         new ol.Attribution({
//           html: "<a href='http://services.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer' target='_blank'\
//           >Topo Sources: Esri, HERE, DeLorme, Intermap, increment P Corp., GEBCO, USGS, FAO, NPS, NRCAN, GeoBase, IGN, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), swisstopo, MapmyIndia, Â© OpenStreetMap contributors, and the GIS User Community</a>"
//         })
//       ]
//   })
// });
// var nautical_charts = new ol.layer.Tile({
//   title: 'Nautical',
//   type: 'base',
//   source: new ol.source.TileWMS({
//     url: 'https://seamlessrnc.nauticalcharts.noaa.gov/arcgis/services/RNC/NOAA_RNC/ImageServer/WMSServer',
//     // params: {'LAYERS': 'NOAA_RNC'},
//     params: {'LAYERS': '0'},
//     attributions: [
//       new ol.Attribution({
//         html: 'Natical Source: NOAA Office of Coast Survey'
//       })
//     ]
//   })
// });
var vectorLayer = new ol.layer.Vector({
  source: new ol.source.Vector({
      format: new ol.format.GeoJSON(),
    // features: new ol.format.GeoJSON().readFeatures([])
    // features: []
  }),
  title: 'Place',
  zIndex: 100
});
// var osmLayer = new ol.layer.Tile({
//   source: new ol.source.OSM(),
//   title: 'Street',
//   type: 'base'
// });

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

const selectStyle = new ol.style.Style({
  fill: new ol.style.Fill({
    color: '#eeeeee',
  }),
  stroke: new ol.style.Stroke({
    color: 'rgba(255, 255, 255, 0.7)',
    width: 2,
  }),
});

let selected = null;
map.on('pointermove', function(e){
  if (selected !== null) {
    selected.setStyle(undefined);
    selected = null;
  }

  map.forEachFeatureAtPixel(e.pixel, function (f) {
    selected = f;
    selectStyle.getFill().setColor(f.get('COLOR') || '#eeeeee');
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

