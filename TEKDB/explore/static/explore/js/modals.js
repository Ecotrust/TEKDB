$("#loginModal").on("shown.bs.modal", function () {
  $("#loginInput").focus();
  var loginForm = document.querySelector("#loginModal form");
  const LOGIN_ERROR_MESSAGE = "Invalid username or password";
  loginForm.addEventListener("submit", function (event) {
    event.preventDefault();
    var signIn = account.signIn(event, this, function (success) {
      if (success) {
        $("#loginModal").modal("hide");
        const exploreLink = document.querySelector(".nav-explore");
        exploreLink.classList.remove("disabled");
        exploreLink.href = "/explore";
        exploreLink.click();
      } else {
        if (!loginForm.innerHTML.includes(LOGIN_ERROR_MESSAGE)) {
          loginForm.append(LOGIN_ERROR_MESSAGE);
        }
      }
    });
  });
});

$("#changePasswordModal").on("shown.bs.modal", function () {
  $("#currentPasswordInput").focus();
  var changePasswordForm = document.querySelector("#changePasswordModal form");
  const CHANGE_PASSWORD_ERROR_MESSAGE = "Error changing password";
  changePasswordForm.addEventListener("submit", function (event) {
    event.preventDefault();
    account.changePassword(event, this, function (success) {
      if (success) {
        $("#changePasswordModal").modal("hide");
        alert("Password changed successfully");
      } else {
        if (!changePasswordForm.innerHTML.includes(CHANGE_PASSWORD_ERROR_MESSAGE)) {
          changePasswordForm.append(CHANGE_PASSWORD_ERROR_MESSAGE);
        }
      }
    });
  });
});