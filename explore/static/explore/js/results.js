function resultViewModel() {
  this.results = ko.observableArray([]);
  this.categories = ko.observableArray(['all']);
  this.db_query = ko.observable('*');
  this.resultGridArray = ko.computed(function () {
      var rows = [], current = [];
      rows.push(current);
      for (var i = 0; i < this.results().length; i += 1) {
          result = this.results()[i];
          bg_class = (i%2 == 1) ? '' : 'result-alt-highlight';
          current.push({ result: '\
          <a href="' + result.link + '">\
            <div class="row result-img-row">\
              <div class="col-md-12 col-sm-12 result-img-col '+ bg_class + '">\
                <img src="' + result.image + '"/>\
              </div>\
            </div>\
            <div class="row result-desc-row">\
              <div class="col-md-12 col-sm-12 result-desc-col">\
                <h3>' + result.name + '</h3>\
                <p>' + result.type + '</p>\
                <div class="result-desc">\
                  <p>' + result.description + '</p>\
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

  this.loadResults = function() {
    filter_categories = ""
    for (var i=0; i < this.categories().length; i++) {
      category = this.categories()[i];
      filter_categories = filter_categories + "&" + category + "=true";
    }
    $.ajax(
      {
        url: '/query?query=' + this.db_query() + filter_categories,
        success: function(result) {
          app.resultViewModel.results(result.resultList);
        },
        error: function(result) {
          window.alert('error!');
        }
      }
    );
  };

};
app.resultViewModel = new resultViewModel();
ko.applyBindings(app.viewModel);
