function resultViewModel() {
  this.results = ko.observableArray([]);
  this.paginated_results = ko.observableArray([]);
  this.categories = ko.observableArray(['all']);
  this.db_query = ko.observable('*');
  this.filter_categories = ko.observable("");
  this.state_page = ko.observable();
  this.state_items_per_page = ko.observable();
  this.state_order = ko.observableArray([]);
  this.state_view = ko.observable('list');
  this.view_is_tiled = ko.computed(function() {
    return this.state_view() == 'tile';
  }, this);
  this.view_is_list = ko.computed(function() {
    return this.state_view() == 'list';
  }, this);

  this.place_results = ko.observableArray([]);

  this.loadPlaceResults = function(results){
    var new_place_results = [];
    for (var i = 0; i < results.length; i++) {
      if (results[i].type == "places") {
        new_place_results.push(results[i]);
      }
    }
    app.resultViewModel.place_results(new_place_results);
    show_map_results();
  };


  this.results.subscribe(this.loadPlaceResults);

  this.loadStateFromHash = function(){
    if ($.query.get('view') == 'tile' || $.query.get('view') == 'list'){
      this.state_view($.query.get('view'));
    }
    if ($.query.get('page') != '' && !isNaN($.query.get('page'))) {
      this.state_page($.query.get('page'));
    }
    if ($.query.get('items_per_page') != '' && !isNaN($.query.get('items_per_page'))) {
      this.state_page($.query.get('items_per_page'));
    }
  }

  this.show_pagination = function(view) {
      $('.paginationjs').hide();
      $('#results_table_paginate').show()
  };

  this.state_view.subscribe(this.show_pagination);

  this.state_page.subscribe(function(newPage) {
    // if (app.tileViewModel && app.tileViewModel.tilepagination()){
      // app.tileViewModel.tilepagination().pagination(newPage);
    // }
    if (app.hasOwnProperty('datatable')) {
      app.datatable.page(newPage-1).draw('page');
    }
  });

  // this.state_items_per_page.subscribe(function(new_ipp){
  //   if (app.tileViewModel) {
  //     app.tileViewModel.reset_tilepagination();
  //   }
  // });

  this.get_state = function() {
    state = [];
    if (this.state_page() != null) {
      state.push('page='+this.state_page());
    }
    if (this.state_items_per_page() != null) {
      state.push('items_per_page='+this.state_items_per_page());
    }
    if (this.db_query() != '*') {
      state.push('filter='+this.db_query());
    }
    if (this.state_order().length > 0) {
      $.query.EMPTY();
      state.push($.query.set('order', this.state_order()));
      $.query.parseNew('', location.hash);
    }
    if (this.state_view() == 'tile' || this.state_view() == 'list') {
      state.push('view='+this.state_view());
    }
    if (this.filter_categories().length > 0) {
      category_states = this.filter_categories().split('&')
      for (var i = 0; i < category_states.length; i++) {
        if (category_states[i].length > 0) {
          state.push(category_states[i]);
        }
      }
    }
    if (state.length > 0) {
      return state.join("&");
    } else {
      return '';
    }
  }

  this.setViewTiled = function() {
    app.resultViewModel.state_view('tile');
    window.location.hash = $.query.SET('view', app.resultViewModel.state_view());
  };

  this.setViewList = function() {
    app.resultViewModel.state_view('list');
    window.location.hash = $.query.SET('view', app.resultViewModel.state_view());
    reset_triggers();
  };

  this.get_url_state = function() {
    return $.query.parseNew('', location.hash).toString();
  };

  this.resultGridArray = ko.computed(function () {
      var rows = [], current = [];
      rows.push(current);
      for (var i = 0; i < this.paginated_results().length; i += 1) {
          result = this.paginated_results()[i];
          bg_class = (i%2 == 1) ? '' : 'result-alt-highlight';
          current.push({ result: '\
          <a href="' + result.link + '">\
            <div class="row result-desc-row">\
              <div class="col-md-12 col-sm-12 result-desc-col">\
                <div id="result-title_' + i + '" class="result-desc">\
                <h3>' + result.name + '</h3>\
                </div>\
              </div>\
            </div>\
            <div class="row result-img-row">\
              <div class="col-md-12 col-sm-12 result-img-col '+ bg_class + '" style="background-image: url('+ result.image +')">\
                <div class="result-img-content-wrapper">\
                  <p><b>' + result.category_name + '</b></p>\
                  '+ (result.description===null?'':'<p id="result-img_' + i + '">' + result.description + '</p>') + '\
                </div>\
              </div>\
            </div>\
          </a>'});
          if (((i + 1) % 3) === 0) {
              current = [];
              rows.push(current);
          }
      }
      return rows;
  }, this);

  this.loadResults = function(result) {
    filter_categories = ""
    for (var i=0; i < this.categories().length; i++) {
      category = this.categories()[i];
      filter_categories = filter_categories + "&" + category + "=true";
    }
    this.filter_categories(filter_categories)
    // app.resultViewModel.results(result.resultList);
    resize_to_fit();
  };

};
app.resultViewModel = new resultViewModel();

function resize_to_fit(){
    var titles = $('div.result-desc');
    for (var i = 0; i < titles.length; i++){
      var title = titles[i];
      var id = '#' + title.id;
      resize_title_to_fit($(id));
    }
    var descs = $('div.result-img-content-wrapper');
    for (var i = 0; i < descs.length; i++){
      var desc = descs[i];
      if (desc.children.length > 1) {
        var id = '#' + desc.children[1].id;
        resize_desc_to_fit($(id));
      }
    }
}

function resize_title_to_fit(self){
  var fontsize = self.children().first().css('font-size');
  self.children().first().css('fontSize', parseFloat(fontsize) - 1);
  if(self.height() >= self.parent().height()){
      resize_title_to_fit(self);
  }
}

function resize_desc_to_fit(self){
  if (self.height() >= self.parent().height()-self.siblings().height()){
    text_length = self.text().length;
    self.text(self.text().substring(0,text_length-10) + '...');
    resize_desc_to_fit(self);
  }
}

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

function show_map_results() {
  var features = [];

  //    Clear features from vector source
  vectorLayer.getSource().clear();
  //    Add results features to  vector source
  var place_results = app.resultViewModel.place_results();
  for (var i = 0; i < place_results.length; i++) {
    var record = place_results[i];
    var geom = JSON.parse(record.feature);
    if (geom) {
      // TODO: append record details to feature attributes/properties
      features.push({
        'id': record.id,
        'type': 'Feature',
        'geometry': geom,
        'properties': {
          'id': record.id,
          'row-id': 'results_row_places_' + record.id,
          'name': record.name,
          'image': record.image,
          'map_pin': record.map_pin,
          'description': record.description,
        }
      });
    }
  }
  
  const featureCollection = {
    'type': 'FeatureCollection',
    'crs': {
      'type': 'name',
      'properties': {
        'name': 'EPSG:3857',
      },
    },
    'features': features
  };
  
  var jsonFeatures = new ol.format.GeoJSON().readFeatures(featureCollection);
  vectorLayer.getSource().addFeatures(jsonFeatures);

  if (vectorLayer.getSource().getFeatures().length > 0) {
    setTimeout(function(){map.updateSize();}, 150);
    var geometry_extent = vectorLayer.getSource().getExtent();
    geometry_extent = buffer_extent(geometry_extent, 0.1);
    map.getView().fit(geometry_extent,map.getSize());
  } else {
    $("#map").hide();
  }

}

var set_triggers = function() {
  const filterForm = document.querySelector('#filter-form');
  filterForm.onsubmit = (e) => {
    filterForm.style.pointerEvents = 'none';
  };

  $("#filter-checkboxes").find('input').change(function(){
    $('#filter-form').submit();
  });
}

$(document).ready(function() {
  set_triggers();
});