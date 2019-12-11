loadInlineTables = function(model, id) {
  url = "/tekdb/" + model + "/" + id + "/get_related";
  $.ajax(
    {
      type: "GET",
      url: url,
      data: {},
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      cache: false,
      success: function(data) {
        for (var i = 0; i < data.length; i++){
          relationship = data[i];
          inline_table = $('#inline_table_' + relationship.data.model);
          inline_table.html('');
          html = '';
          if (relationship.data.rows.length > 0) {
            html = '<tr>';
            // Start columns on index 1 - ignore id column
            for (var col_idx = 1; col_idx < relationship.data.columns.length; col_idx++) {
              html += '<th>' + relationship.data.columns[col_idx] + '</th>';
            }
            html += '<th class="change-col">Edit</th>'
            html += '<th class="delete-col">Delete</th>'
            html += '</tr>';
            for (var row_idx = 0; row_idx < relationship.data.rows.length; row_idx++) {
              row = relationship.data.rows[row_idx];
              html += '<tr class="relationship-row">';
              // Start cells on index 1 - ignore id column
              for (var cell_idx = 1; cell_idx < row.length; cell_idx++) {
                cell = row[cell_idx];
                html += '<td>' + cell + '</td>';
              }
              html += '<td class="change-col">'
              html += '<a title="Change selected '+ relationship.title + '" data-toggle="modal" data-target="#inlineFormModal" onclick="loadFormModal(\''+ relationship.data.module + '\', \'' + relationship.data.model + '\', \'' + row[0] + '\', \'edit\', \'' + model + '\', \'' + id + '\', \'' + relationship.data.fk_field_id + '\')"><img src="/static/admin/img/icon-changelink.svg" alt="Change"></a>'
              html += '</td>'
              html += '<td class="delete-col">'
              html += '<a title="Delete selected '+ relationship.title + '" data-toggle="modal" data-target="#inlineFormModal" onclick="loadFormModal(\''+ relationship.data.module + '\', \'' + relationship.data.model + '\', \'' + row[0] + '\', \'delete\', \'' + model + '\', \'' + id + '\', \'' + relationship.data.fk_field_id + '\')"><img src="/static/admin/img/icon-deletelink.svg" alt="Delete"></a>'
              html += '</td>'
              html += '</tr>';
            }
          }
          inline_table.html(html);
        }
      },
      error: function(msg){
        alert(msg.responseText);
      }
    }
  );
}

iframeButtonClicked = function (model, id) {
  // hide the modal
  if ($('#inlineFormModal').hasClass('in')){
    $('#inlineFormModal').modal('toggle');
  }
  setTimeout(function() {
    // Give the record half a second to save before reloading tables.
    loadInlineTables(model, id);
  }, 500);
}

loadFormModal = function(module, model, id, action, base_model, base_id, fk_field_id) {
  html = '<iframe id="popup-iframe-form" style="width: 100%; height: 350px;" src="/admin/' + module + '/' + model + '/';
  if (action == 'add') {
     html += 'add';
  } else if (action == 'edit'){
     html += id + '/change';
  } else if (action == 'delete') {
     html += id + '/delete';
  }
  html +='/?_popup=1"></iframe>';
  $('#form-modal-body').html(html);
  $('#popup-iframe-form').load(function(){
      if (action != 'delete') {
        if (action == 'add') {
          $('#popup-iframe-form').contents().find('#id_' + fk_field_id).parent().replaceWith('<input name="' + fk_field_id + '" id="id_' + fk_field_id + '" value="' + base_id + '"></input>');
        }
        // If below only shown for 'add', users could move relationships to new records
        // For now I'm not sure this feature is intuitive or desired.
        $('#popup-iframe-form').contents().find('#id_' + fk_field_id).hide();
        $('#popup-iframe-form').contents().find('.field-box.field-' + fk_field_id).hide();
        all_buttons = $('#popup-iframe-form').contents().find('.submit-row input');
      } else {
        all_buttons = $('#popup-iframe-form').contents().find('form div').children(':not([type="hidden"])');
      }
      all_buttons.attr('data-toggle', 'modal');
      all_buttons.attr('data-target', '#inlineFormModal');
      all_buttons.on('click', function(){iframeButtonClicked(base_model, base_id);});
  });
}
