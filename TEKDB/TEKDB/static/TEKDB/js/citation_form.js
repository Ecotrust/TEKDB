show_reftype_form = function(reftype) {
  $('.citation-form-fieldset h2').html(reftype);
  switch(reftype) {
    case '---------':
      $('.citation-form-fieldset h2').html("Select a 'Reference type' to contine.");
      $('.form-row.field-title').hide();
      $('.form-row.field-authorprimary.field-authorsecondary').hide();
      $('.form-row.field-date').hide();
      $('.form-row.field-year').hide();
      $('.form-row.field-publisher.field-publishercity').hide();
      $('.form-row.field-seriestitle').hide();
      $('.form-row.field-seriesvolume.field-serieseditor').hide();
      $('.form-row.field-intervieweeid.field-interviewerid').hide();
      $('.form-row.field-placeofinterview').hide();
      $('.form-row.field-journal.field-journalpages').hide();
      $('.form-row.field-preparedfor').hide();
      $('.form-row.field-referencetext').hide();
      $('.form-row.field-rawcitation').hide();
      $('.form-row.field-comments').hide();
      break;
    case 'Book':
      $('.form-row.field-title').show();
      $('.form-row.field-authorprimary.field-authorsecondary').show();
      $('.form-row.field-date').hide();
      $('.form-row.field-year').show();
      $('.form-row.field-publisher.field-publishercity').show();

      $('.form-row.field-seriestitle').hide();
      $('.form-row.field-seriesvolume.field-serieseditor').hide();
      $('.form-row.field-intervieweeid.field-interviewerid').hide();
      $('.form-row.field-placeofinterview').hide();
      $('.form-row.field-journal.field-journalpages').hide();
      $('.form-row.field-preparedfor').hide();

      $('.form-row.field-referencetext').show();
      $('.form-row.field-rawcitation').hide();
      $('.form-row.field-comments').show();

      break;
    case 'Edited Volume':
      $('.form-row.field-title').show();
      $('.form-row.field-authorprimary.field-authorsecondary').show();
      $('.form-row.field-date').hide();
      $('.form-row.field-year').show();
      $('.form-row.field-publisher.field-publishercity').show();
      $('.form-row.field-seriestitle').show();
      $('.form-row.field-seriesvolume.field-serieseditor').show();

      $('.form-row.field-intervieweeid.field-interviewerid').hide();
      $('.form-row.field-placeofinterview').hide();
      $('.form-row.field-journal.field-journalpages').hide();
      $('.form-row.field-preparedfor').hide();

      $('.form-row.field-referencetext').show();
      $('.form-row.field-rawcitation').hide();
      $('.form-row.field-comments').show();
      break;
    case 'Interview':
      $('.form-row.field-title').hide();
      $('.form-row.field-authorprimary.field-authorsecondary').hide();
      $('.form-row.field-publisher.field-publishercity').hide();
      $('.form-row.field-seriestitle').hide();
      $('.form-row.field-seriesvolume.field-serieseditor').hide();

      $('.form-row.field-intervieweeid.field-interviewerid').show();
      $('.form-row.field-date').hide();
      $('.form-row.field-year').show();
      $('.form-row.field-placeofinterview').show();

      $('.form-row.field-journal.field-journalpages').hide();
      $('.form-row.field-preparedfor').hide();

      $('.form-row.field-referencetext').show();
      $('.form-row.field-rawcitation').hide();
      $('.form-row.field-comments').show();
      break;
    case 'Raw Data':
      $('.form-row.field-title').show();
      $('.form-row.field-date').show();
      $('.form-row.field-authorprimary.field-authorsecondary').show();

      $('.form-row.field-publisher.field-publishercity').hide();
      $('.form-row.field-seriestitle').hide();
      $('.form-row.field-seriesvolume.field-serieseditor').hide();
      $('.form-row.field-intervieweeid.field-interviewerid').hide();
      $('.form-row.field-year').hide();
      $('.form-row.field-placeofinterview').hide();
      $('.form-row.field-journal.field-journalpages').hide();
      $('.form-row.field-preparedfor').hide();

      $('.form-row.field-referencetext').show();
      $('.form-row.field-rawcitation').hide();
      $('.form-row.field-comments').show();
      break;
    default:
      $('.form-row.field-title').show();
      $('.form-row.field-authorprimary.field-authorsecondary').show();
      $('.form-row.field-date').hide();
      $('.form-row.field-year').show();
      $('.form-row.field-publisher.field-publishercity').show();
      $('.form-row.field-seriestitle').show();
      $('.form-row.field-seriesvolume.field-serieseditor').show();

      $('.form-row.field-intervieweeid.field-interviewerid').hide();
      $('.form-row.field-placeofinterview').hide();

      $('.form-row.field-journal.field-journalpages').show();
      $('.form-row.field-preparedfor').show();
      $('.form-row.field-referencetext').show();
      $('.form-row.field-rawcitation').hide();
      $('.form-row.field-comments').show();
      break;
  }
}

show_reftype_form($('#id_referencetype option:selected').text());

$('#id_referencetype').change(function() {
  var reftype = $('#id_referencetype option:selected').text();
  show_reftype_form(reftype);
});
