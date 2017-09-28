
var medialink_text = $('.field-medialink').children().find("div").text();
if (medialink_text == '-' || medialink_text.indexOf($('.file-upload').find('a').attr('href')) >= 0) {
  $('.field-medialink').hide();
}
