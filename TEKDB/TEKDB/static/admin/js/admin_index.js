const importText = `
  This process will remove all data and files from your current 
  database and replace it with data from the provided zip file. 
  </br><br>
  This process CANNOT be undone. </br><br>
  It is recommended that you use the 'Export to .zip' button above to export 
  your current database status so that you may restore to your 
  present state, AND that you COORDINATE WITH IT professionals 
  prior to attempting this. </br><br>
  You will need to log in again using administrator credentials 
  as defined by the new data: your current account will cease to 
  exist.</br><br>
  Are you sure you understand and are prepared to take this risk?
`
const importInfoText = `The Import Database Tool is designed to support restoring your Traditional Knowledge Database back to a prior state. This is best used in conjunction with the 'Export Database' tool above. </br><br>
      To use the Import Database tool is simple: select a properly formatted zip file to upload and then click 'Import'. All of your data will be reverted back to the state it was when that zipfile was created. </br><br>
      This is VERY DANGEROUS! For this to work, all of the data currently 
      in your database, including your users, your records, and your page 
      contents will be removed, and then replaced. Also, any files 
      associated with your media records (images, audio, video, PDFs, 
      etc...) will be overwritten by any files of the same name included 
      in the zipped up backup file that you import.</br><br>
      If you wish to use this, it is recommended that you work with IT 
      professionals prior to undertaking this task. While IT cannot create 
      one of these import files for a prior state, they can help you 
      securely preserve any new zipped export files, and should be able 
      to create a system backup of your database to restore in the event 
      of complications while using this tool. </br><br>
      Note that a zipped backup file is easily created for your current 
      state with the 'Export to .zip' button above, but cannot be 
      created by hand. If you have not created any of these files, you 
      should not use this tool.`

const exportInfoText = `The Export Database Tool is designed to support saving the current 
        state of your Traditional Knowledge Database. This is best 
        used in conjunction with the 'Import Database' tool below. </br><br>

        To use the Export Database tool is simple: just press 'Export to 
        .zip' button and all of your data and media files will be collected 
        into a single zipfile and downloaded to your current computer.</br></br>

        This is VERY DANGEROUS! While keeping regular backups 
        of your database is crucial to preventing data loss from future 
        incidents, the exported file will contain ALL of your data in an  
        unencrypted format. These exported files  
        must be kept in a secure place and only shared via secure channels: 
        NOT BY EMAIL.</br></br>

        Please work with IT professionals to design 
        a safe and secure practice for regular backups, which may or may 
        not involve this tool.`

$(function () {
  const unexpectedError = (statusCode, statusMessage) => {
    return `<p class='text-danger'>Unexpected error occurred: ${statusCode}</p><p>${statusMessage}</p>`;
  };

  const showNextStepsSection = () => {
    $("#modalNextSteps").removeClass("hidden");
  }

  const showModalFooter = () => {
    $(".modal-footer").show();
  }

  const hideModalFooter = () => {
    $(".modal-footer").hide();
  }

  $("button#import-button").click(function (e) {
    e.preventDefault();
    showModalFooter();
    
    $("#modalTitle").text("Export Database Tool");
    $("#modalBody").html(importText);

    $("#continueImport").click(function () {
      form = $("#import-database-form");
      $.ajax({
        url: "/import_database/",
        data: new FormData(form[0]),
        type: "POST",
        processData: false,
        contentType: false,
        success: function (data, status) {
          if (
            data.hasOwnProperty("status_code") &&
            data.hasOwnProperty("status_message")
          ) {
            showNextStepsSection()
            
            if (data.status_code == 200) {
              $("#modalNextSteps").html(
                `<p class='text-success'>Import successful. You may now be logged out.</p>`
              );

              window.location.reload();
            } else {
              $("#modalNextSteps").html(
                `<p class='text-danger'>Import failed with error code ${data.status_code}.</p><p class='text-danger'>${data.status_message}</p>`
              );
            }
          } else {
            $("#modalNextSteps").html(
              unexpectedError(xhr.status, xhr.statusText)
            );
          }
        },
        error: function (xhr, desc, err) {
          $("#modalNextSteps").html(
            unexpectedError(xhr.status, xhr.statusText)
          );
        },
      });
    });
    $;
  });

  $("button#import-info").click(function (e) {
    hideModalFooter();
    $("#modalTitle").text("Import Database Tool");
    $("#modalBody").html(exportInfoText);
  });

  $("button#export-info").click(function (e) {
    hideModalFooter();
    $("#modalTitle").text("Export Database Tool");
    $("#modalBody").html(exportInfoText);
  });

  // Clear modal content on close
  $('#exportImportModal').on('hidden.bs.modal', function () {
    $("#modalTitle").text("");
    $("#modalBody").html("");
    $("#modalNextSteps").html("");
    $("#modalNextSteps").addClass("hidden");
});

});
