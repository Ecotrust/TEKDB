tileViewModel = function() {
  this.tilepagination = ko.observable();

  this.init_tilepagination = function() {
    app.tileViewModel.tilepagination($('#pagination-container').pagination({
      dataSource: app.resultViewModel.results(),
      pageSize: app.resultViewModel.state_items_per_page(),
      pageNumber: app.resultViewModel.state_page(),
      pageRange: 1,
      callback: function(data, pagination) {
          app.resultViewModel.paginated_results(data);
      }
    }));
  }

  this.reset_tilepagination = function() {
    if (app.tileViewModel && app.tileViewModel.tilepagination()) {
      app.tileViewModel.tilepagination().pagination('destroy');
    }
    app.tileViewModel.init_tilepagination();
  }

}
app.tileViewModel = new tileViewModel();

$(document).ready( function () {
  app.tileViewModel.init_tilepagination();
} );
