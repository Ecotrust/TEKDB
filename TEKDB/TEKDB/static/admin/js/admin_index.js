const importText = `
  This process will remove all data and files from your current 
  database and replace it with data from the provided zipfile. 
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
`;

const importInfoText = `The Import Database Tool is designed to support restoring your Traditional Knowledge Database back to a prior state. This is best used in conjunction with the 'Export Database' tool above. </br><br>
      To use the Import Database tool is simple: select a properly formatted zipfile to upload and then click 'Import'. All of your data will be reverted back to the state it was when that zipfile was created. </br><br>
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
      should not use this tool.`;

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
        not involve this tool.`;

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

$(function () {
  const unexpectedError = (statusCode, statusMessage = "") => {
    return `<p class='text-danger'>Unexpected error occurred: ${statusCode}</p><p class='text-danger'>${statusMessage}</p>`;
  };

  const showNextStepsSection = () => {
    $("#modalNextSteps").removeClass("hidden");
  };

  const showModalFooter = () => {
    $(".modal-footer").show();
  };

  const hideModalFooter = () => {
    $(".modal-footer").hide();
  };

  const resetModal = () => {
    $("#continueImport").html("Close");
    $("#closeModalButton").prop("disabled", false);
    $("#continueImport").one("click", function () {
      $("#exportImportModal").modal("hide");
    });
  };

  const clearExportStatusCookie = () => {
    document.cookie =
      "export_status=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
  };

  const clearExportErrorMessageCookie = () => {
    document.cookie =
      "export_error_message=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
  }

  const showErrorMessage = (message) => {
    $("#exportStatus")
      .removeClass("hidden")
      .html(`<p class='text-danger'>${message}</p>`);
  }

  const resetExportButton = (iframe, clear) => {
    $("#export-button").prop("disabled", false);
    $("#export-button").html("Export to .zip");
    iframe.remove();
    clear();
    clearExportStatusCookie();
    clearExportErrorMessageCookie();
  };

  $("button#import-button").click(function (e) {
    e.preventDefault();
    showModalFooter();

    $("#modalTitle").text("Import Database");
    $("#modalBody").html(importText);
    let showSpinner = true;
    $("#continueImport").one("click", function () {
      // prevent closing the modal after verifying import
      $("#exportImportModal").modal({
        backdrop: "static",
        keyboard: false,
      });

      // add spinner to the button
      // change button text to "Importing..."
      if (showSpinner) {
        $("#continueImport").html(
          `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Importing...`
        );
        $("#continueImport").prop("disabled", true);
        $("#closeModalButton").prop("disabled", true);
      }
      const form = $("#import-database-form");
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
            showNextStepsSection();
            $("#continueImport").prop("disabled", false);

            if (data.status_code == 200) {
              $("#modalNextSteps").html(
                `<p class='text-success'>Import successful. You may now be logged out.</p>`
              );
              showSpinner = false;
              $("#continueImport").html("Log out");
              $("#continueImport").one("click", function () {
                $.ajax({
                  url: "/logout/",
                  type: "POST",
                  headers: {'X-CSRFToken': csrftoken},
                  mode: 'same-origin',
                  success: function () {
                    // force reload to update to logged out state
                    location.reload(true);
                  },
                });
              });
            } else {
              $("#modalNextSteps").html(
                `<p class='text-danger'>Import failed with error code ${data.status_code}.</p><p class='text-danger'>${data.status_message}</p>`
              );
              showSpinner = false;
              resetModal();
            }
          } else {
            $("#modalNextSteps").html(unexpectedError(status));
            showSpinner = false;
            resetModal();
          }
        },
        error: function (xhr) {
          showNextStepsSection();
          let statusCode = xhr.responseJSON?.status_code || xhr.status;
          let statusMessage = xhr.responseJSON?.status_message || xhr.statusText;
          if (xhr.status === 0 || xhr.status === 502 || xhr.status === 503) {
            statusMessage =
              "The server could not process the request. This may be caused by insufficient disk space on the server. Please contact your IT team.";
          } else if (xhr.status === 507) {
            statusMessage =
              xhr.responseJSON?.status_message ||
              "Not enough disk space on the server to process the upload. Please contact your IT team.";
          } else if (xhr.status === 413) {
            statusMessage = "The uploaded file is too large for the server to accept.";
          }
          $("#modalNextSteps").html(unexpectedError(statusCode, statusMessage));
          $("#continueImport").prop("disabled", false);
          resetModal();
        },
      });
    });
  });

  $("button#import-info").click(function (e) {
    hideModalFooter();
    $("#modalTitle").text("Import Database Tool");
    $("#modalBody").html(importInfoText);
  });

  $("button#export-info").click(function (e) {
    hideModalFooter();
    $("#modalTitle").text("Export Database Tool");
    $("#modalBody").html(exportInfoText);
  });

  $("button#export-button").click(function (e) {
    e.preventDefault();

    // remove error message if present
    $("#exportStatus").addClass("hidden");

    // disable button and show spinner
    $("#export-button").prop("disabled", true);
    $("#export-button").html(
      `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Exporting...`
    );

    // set cookie to pending
    document.cookie = "export_status=pending; path=/";

    // create hidden iframe to trigger download
    const iframe = $("<iframe/>")
      .hide()
      .attr("src", "/export_database/")
      .appendTo("body");

    const maxPollMs = 1 * 60 * 1000; // 1 minute safety cap (probably way longer than needed)
    const startTime = Date.now();

    // poll cookie for export_status
    const checkStatus = setInterval(() => {
      const cookies = document.cookie.split(";").map((c) => c.trim());
      const exportStatus = cookies.filter((c) =>
        c.startsWith("export_status=")
      );

      if (
        exportStatus &&
        (exportStatus.includes("export_status=done") ||
          exportStatus.includes("export_status=error"))
      ) {
        resetExportButton(iframe, () => clearInterval(checkStatus));
        if (exportStatus.includes("export_status=error")) {
          // Get the error message from cookie
          const errorMsgCookie = cookies.find((c) =>
            c.startsWith("export_error_message=")
          );
          let errorMsg = "An error occurred during export.";
          if (errorMsgCookie) {
            errorMsg = decodeURIComponent(
              errorMsgCookie.split("=").slice(1).join("=")
            );
            // Clear the error message cookie
            clearExportErrorMessageCookie();
          }
          showErrorMessage(errorMsg);
        }
      } else {
        if (Date.now() - startTime > maxPollMs) {
          // timeout
          resetExportButton(iframe, () => clearInterval(checkStatus));
          showErrorMessage("Export timed out. Please try again.");
        }
      }
    }, 1000);
  });

  // Clear modal content on close; reset to default state
  $("#exportImportModal").on("hidden.bs.modal", function () {
    $("#modalTitle").text("");
    $("#modalBody").html("");
    $("#modalNextSteps").html("");
    $("#modalNextSteps").addClass("hidden");
    $("#continueImport").html("Continue");
    $("#continueImport").off("click");
  });
});
