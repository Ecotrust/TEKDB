

show_reftype_form = function(reftype) {
  $('.citation-book-form').hide();
  $('.citation-volume-form').hide();
  $('.citation-interview-form').hide();
  $('.citation-other-form').hide();
  switch(reftype) {
    case '---------':
      break;
    case 'Book':
      $('.citation-book-form').show();
      break;
    case 'Edited Volume':
      $('.citation-volume-form').show();
      break;
    case 'Interview':
      $('.citation-interview-form').show();
      break;
    case 'Other':
      $('.citation-other-form').show();
      break;
    default:
      $('.citation-other-form').show();
      break;
  }
}

show_reftype_form($('#id_referencetype option:selected').text());

// $( "form" ).submit(function( event ) {
//   event.preventDefault();
//   window.alert('submit!');
// });

// update_referencetype = function() {
$('#id_referencetype').change(function() {
  var reftype = $('#id_referencetype option:selected').text();
  show_reftype_form(reftype);
});

// $('[name="title"]').change(function(event) {
$('input, text, textarea').change(function(event) {
  new_val = event.currentTarget.value;
  name = event.currentTarget.name;
  $('[name="' + name + '"]').val(new_val);
  // window.alert('title change');
});
