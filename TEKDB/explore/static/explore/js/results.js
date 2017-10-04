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
    if (app.tileViewModel && app.tileViewModel.tilepagination()){
      app.tileViewModel.tilepagination().pagination(newPage);
    }
    if (app.hasOwnProperty('datatable')) {
      app.datatable.page(newPage-1).draw('page');
    }
  });

  this.state_items_per_page.subscribe(function(new_ipp){
    if (app.tileViewModel) {
      app.tileViewModel.reset_tilepagination();
    }
  });

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
    if (state.length > 0) {
      return state.join("&");
    } else {
      return '';
    }
  }

  this.setViewTiled = function() {
    app.resultViewModel.state_view('tile');
  };

  this.setViewList = function() {
    app.resultViewModel.state_view('list');
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
