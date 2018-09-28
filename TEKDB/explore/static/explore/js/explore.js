  function setCategoryType(category) {
    $('#search-category-type')[0].value = category;
    $('.selected').removeClass('selected');
    $('#category-btn-'+category).addClass('selected');
  }