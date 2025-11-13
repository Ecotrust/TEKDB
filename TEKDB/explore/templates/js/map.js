/* ---- STYLES ---- */

const getDefaultStrokeColor = () => '#FF6000';
const getDefaultFillOpacity = () => 0.4;
const getDefaultStrokeWidth = () => 1.25;
const getDefaultFillColor = () => 'rgba(255, 96, 0, ' + getDefaultFillOpacity() + ')';
const getDefaultRadius = () => 5;

const getFill = () => new ol.style.Fill({
  color: getDefaultFillColor(),
});

const getStroke = () => new ol.style.Stroke({
  color: getDefaultStrokeColor(),
  width: getDefaultStrokeWidth(),
});

const getStyles = (fill, stroke, radius) => {
  return new ol.style.Style({
    image: new ol.style.Circle({
      fill: fill,
      stroke: stroke,
      radius: radius,
    }),
    fill: fill,
    stroke: stroke,
  });
};

const applyStyles = (mapPin) => (feature) => {
  let style = feature.getStyle();

  if (!style) {
    style = getStyles(getFill(), getStroke(), getDefaultRadius());
  }
  if (feature.getGeometry().getType() === 'Point' && mapPin !== "") {
    style.setImage( new ol.style.Icon({
      anchor: [0.5, 1],
      anchorXUnits: 'fraction',
      anchorYUnits: 'fraction',
      src: mapPin,
      scale: 0.1
    }))
  }

  return style;
}

/* --- LAYERS --*/
const getEsriLabels = () => {
  return new ol.layer.Tile({
    title: 'Labels',  
    zIndex: 5,
    source: new ol.source.XYZ({
      url: "https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}.png",
      attributions: [
        "<br/><a href='https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer' target='_blank'>\
          Labels Sources: Esri, HERE, DeLorme, MapmyIndia, Â© OpenStreetMap contributors, and the GIS user community</a>"
      ]
    })
  });
}

const getEsriAerial = () => {
  return new ol.layer.Tile({
    title: 'Aerial',
    type: 'base',
    visible: 'true',
    source: new ol.source.XYZ({
      url: "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}.png",
      attributions: [
        "<a href='https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer' target='_blank'>\
          Aerial Sources: Esri, DigitalGlobe, GeoEye, Earthstar Geographics, CNES/Airbus DS, USDA, USGS, AeroGRID, IGN, and the GIS User Community</a>"
      ]
    })
  });
}


const getVectorLayer = (vectorSource) => {
  return new ol.layer.Vector({
    source: vectorSource,
    title: 'Place',
    zIndex: 100,
    style: applyStyles('{{ map_pin }}'),
  });
}

const getVectorSource = (mapData) => {
  return new ol.source.Vector({
      features: new ol.format.GeoJSON().readFeatures(JSON.parse(mapData))
    });
}

const makeFeatureCollection = (features) => {
  return {
    type: "FeatureCollection",
    crs: {
    type: "name",
      properties: {
        name: "EPSG:3857",
      },
    },
    features: features,
  };
}

const getGeojsonFromFeatureCollection = (featureCollection) => {
  return new ol.format.GeoJSON().readFeatures(featureCollection);
}

const addFeaturesToSource = (source, features) => {
  source.getSource().addFeatures(features);
}

/* --- CONTROLS --*/

const getScaleLineControl = () => {
  return new ol.control.ScaleLine({
    units: 'us'
  });
}
const getMousePositionControl = (target) => {
  return new ol.control.MousePosition({
    coordinateFormat: ol.coordinate.createStringXY(4),
    projection: 'EPSG:4326',
    target: target,
    undefinedHTML: '&nbsp;'
  });
};

/*--- MAP ZOOM ---*/

const getBufferExtent = (extent, buffer) => {
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

const getMapLayers = (overlayLayers, baseLayers) => {
  return [
    new ol.layer.Group({
      title: 'Overlays',
      layers: overlayLayers,
      zIndex: 10
    }),
    new ol.layer.Group({
      title: 'Base Maps',
      layers: baseLayers,
      zIndex: 0
    })
  ];
}

const getMap = (target, controls, layers, view) => {
  return new ol.Map({
    controls: ol.control.defaults({
    attributionOptions: ({
      collapsible: true
    })
  }).extend(controls),
    layers: layers,
    target: target,
    view: view
  })
}

const fitMapToFeatures = (layers, map) => {
  if (layers.getSource().getFeatures().length > 0) {
    let geometry_extent = layers.getSource().getExtent();
    geometry_extent = getBufferExtent(geometry_extent, 0.1);
    map.getView().fit(geometry_extent, map.getSize());
  }
}

const mapView = () => {
  return new ol.View({
    center: [{{ default_lon }}, {{ default_lat }}],
    zoom: {{ default_zoom }},
    minZoom: {{ min_zoom }},
    maxZoom: {{ max_zoom }},
    extent: {{ map_extent }}
  });
}

/*--- MAIN MAP ---*/

{% if record.map %}


  const mainEsriLabels = getEsriLabels();
  const mainEsriAerial = getEsriAerial();

  const mainScaleLineControl = getScaleLineControl();
  const mainMousePositionControl = getMousePositionControl('mouse-position');
  const mapVectorLayer = getVectorLayer(getVectorSource('{{ record.map | safe }}'));
  const mainMapLayers = getMapLayers([mapVectorLayer, esriLabels], [esriAerial]);
  const mainMapControls = [mainScaleLineControl, mainMousePositionControl];
  const mainMapTarget = 'map';

  const getMainMap = () => getMap(
    mainMapTarget,
    mainMapControls,
    mainMapLayers,
    mapView()
  );

  const mainMap = getMainMap();
  fitMapToFeatures(mapVectorLayer, mainMap);
{% endif %}

/* --- PLACE-RESOURCE MAP ---*/

{% if place_resource_features %}
  const makePlaceResourceFeaturesArray = () => {
    const features = [];
    {% for feature in place_resource_features %}
      {% if feature.map %}
        const geometry_{{ forloop.counter }} = JSON.parse(`{{ feature.map|safe }}`);
        if (geometry_{{ forloop.counter }}) {
          const feature = {
            type: "Feature",
            id: {{ forloop.counter }},
            geometry: geometry_{{ forloop.counter }},
            properties: {
              id: '{{ forloop.counter }}',
              name: '{{ feature.name|escapejs }}'
            }
          };

          features.push(feature);
        }
      {% endif %}
    {% endfor %}
    return features;
  }

  const placeResourcesFeatures = makePlaceResourceFeaturesArray();
  const placeResourceFeatureCollection = makeFeatureCollection(placeResourcesFeatures);
  const placeResourceGeojson = getGeojsonFromFeatureCollection(placeResourceFeatureCollection);

  const placeResourceVectorLayer = getVectorLayer(new ol.source.Vector());

  const placeResourceEsriLabels = getEsriLabels();
  const placeResourceEsriAerial = getEsriAerial();

  const placeResourceMapLayers = getMapLayers([placeResourceVectorLayer, placeResourceEsriLabels], [placeResourceEsriAerial]);
  const placeResourceScaleLineControl = getScaleLineControl();
  const placeResourceMouseControl = getMousePositionControl('place-resource-mouse-position');
  const placeResourceMapControls = [placeResourceScaleLineControl, placeResourceMouseControl];
  const placeResourceMapTarget = 'place-resource-map';

  const getPlaceResourceMap = () => getMap(
    placeResourceMapTarget,
    placeResourceMapControls,
    placeResourceMapLayers,
    mapView()
  );

  const placeResourceMap = getPlaceResourceMap();
  addFeaturesToSource(placeResourceVectorLayer, placeResourceGeojson);
  fitMapToFeatures(placeResourceVectorLayer, placeResourceMap);

{% endif %}