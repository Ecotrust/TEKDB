// BIG MESSY STATE MANAGEMENT //

var reset_triggers = function() {
    setTimeout(function() {
      //Change Page
      $('.paginate_button').off('click');
      $('.paginate_button').click(page_click);
      //Change Items per Page
      $('#results_table_length > label > select').change(change_items_per_page);
      //Change Search Filter
      $('#results_table_filter > label > input').keyup(change_filter);
      //Change Sorting
      $("#name_col").click(change_sort);
      $("#category_col").click(change_sort);
      $("#description_col").click(change_sort);
    }, 20);
}

var page_click = function(event){
  page = event.target.text;
  console.log('page clicked: '+ page);
  if (isNaN(page)) {
    current_page = parseInt(app.resultViewModel.state_page());
    var max_page = app.datatable.page.info().pages;
    var min_page = 1;
    if (page == '«') {
      page = current_page-1;
    } else if (page == '»') {
      page = current_page+1;
    } else {
      page = current_page;
    }
  }
  if (page < min_page) {
    page = min_page;
  }
  if (page > max_page) {
    page = max_page;
  }
  window.location.hash = $.query.SET('page', page);
  app.resultViewModel.state_page(parseInt(page));
  reset_triggers();
}

var get_current_page = function() {
  return parseInt($('.paginate_button.current').text());
}

var change_items_per_page = function(event) {
  items_per_page = parseInt(event.target.value);
  app.resultViewModel.state_items_per_page(items_per_page);
  app.resultViewModel.state_page(get_current_page());
  window.location.hash = $.query.SET('items_per_page', items_per_page).SET('page', app.resultViewModel.state_page());
  reset_triggers();
}

var change_filter = function(event) {
  setTimeout(function() {
    filter = event.target.value;
    app.resultViewModel.state_page(get_current_page());
    window.location.hash = $.query.SET('page', app.resultViewModel.state_page());
    if (filter.length > 0) {
      app.resultViewModel.db_query(filter);
      window.location.hash = $.query.SET('filter', app.resultViewModel.db_query());
    } else {
      app.resultViewModel.db_query('*');
      window.location.hash = $.query.REMOVE('filter');
    }
    reset_triggers();
  }, 10);
}

var change_sort = function(event) {
  order = [];
  column_keys = ['name', 'category', 'description'];
  for (var i = 0; i < column_keys.length; i++){
    sort_class = $("#"+ column_keys[i]+"_col").attr('class');
    console.log(sort_class);
    if (sort_class == 'sorting_desc') {
      order.push([i+1, 'desc']);
    } else if (sort_class == 'sorting_asc') {
      order.push([i+1, 'asc']);
    }
  }
  app.resultViewModel.state_order(order);
  app.resultViewModel.state_page(get_current_page());
  window.location.hash = $.query.SET('page', app.resultViewModel.state_page());
  if (app.resultViewModel.state_order().length > 0) {
    window.location.hash = $.query.SET('order', app.resultViewModel.state_order());
  } else {
    window.location.hash = $.query.REMOVE('order');
  }
  reset_triggers();

}

$(document).ready( function () {
  if ($.query.get('page') != "") {
    app.resultViewModel.state_page($.query.get('page'));
  }
  if ($.query.get('items_per_page') != "") {
    app.resultViewModel.state_items_per_page(parseInt($.query.get('items_per_page')));
  }
  if ($.query.get('filter') != "") {
    app.resultViewModel.db_query($.query.get('filter'));
  }
  if ($.query.get('order') != "") {
    app.resultViewModel.state_order($.query.get('order'));
  }

  var results_per_page_options = [10, 25, 50, 100];
  if (results_per_page_options.indexOf(app.resultViewModel.state_items_per_page()) < 0) {
    results_per_page_options.push(app.resultViewModel.state_items_per_page());
  }
  results_per_page_options.sort(function(a, b){return a - b});
  /* displayStart takes the index of the record to show, not the page, 0-addressed */
  var display_start = (app.resultViewModel.state_page() - 1)*app.resultViewModel.state_items_per_page();
  var initial_filter = app.resultViewModel.db_query() == '*' ? '' : app.resultViewModel.db_query();

  app.datatable = $('#results_table').DataTable({
    "displayStart": display_start,
    "pageLength": app.resultViewModel.state_items_per_page(),
    "lengthMenu": results_per_page_options,
    // "search": {
    //   "search": initial_filter
    // },
    "order": app.resultViewModel.state_order(),
    "columnDefs": [
      { "orderable": false, "targets": 0 }
    ]
  });

  $('#pagination-container').append( $('#results_table_paginate') );
  $('#results_table_filter').detach();
  $('#results_table_length').append( $('#results_table_info') );

  //Set up initial state triggers
  reset_triggers();
} );
