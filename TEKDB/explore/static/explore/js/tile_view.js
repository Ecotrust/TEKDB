var reset_tile_triggers = function() {
    setTimeout(function() {
      //Change Page
      // managed by datatables pagination handlers
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
