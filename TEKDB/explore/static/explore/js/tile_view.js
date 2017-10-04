var reset_tile_triggers = function() {
    setTimeout(function() {
      //Change Page
      $('.paginationjs-page').click(tile_page_click);
      //Change Items per Page
      // $('#results_table_length > label > select').change(change_items_per_page);
      //Change Search Filter
      // $('#results_table_filter > label > input').keyup(change_filter);
      //Change Sorting
      // $("#name_col").click(change_sort);
      // $("#category_col").click(change_sort);
      // $("#description_col").click(change_sort);
    }, 20);
}

var tile_page_click = function(event){
  page = event.currentTarget.children[0].text;
  window.location.hash = $.query.SET('page', page);
  app.resultViewModel.state_page(parseInt(page));
  reset_tile_triggers();
}

$(document).ready( function () {
  app.tilepagination = $('#pagination-container').pagination({
    dataSource: app.resultViewModel.results(),
    pageSize: app.resultViewModel.state_items_per_page(),
    pageNumber: app.resultViewModel.state_page(),
    pageRange: 1,
    callback: function(data, pagination) {
        app.resultViewModel.paginated_results(data);
    }
  });
  setTimeout(function() {
    reset_tile_triggers();
  }, 25);
} );
