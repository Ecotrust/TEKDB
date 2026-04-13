$("#loginModal").on("shown.bs.modal", function () {
  $("#loginInput").focus();
  var loginForm = document.querySelector("#loginModal form");
  const LOGIN_ERROR_MESSAGE = "Invalid username or password";
  loginForm.addEventListener("submit", function (event) {
    event.preventDefault();
    account.signIn(event, this, function (success) {
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
  changePasswordForm.addEventListener("submit", function (event) {
    event.preventDefault();
    account.changePassword(event, this, function (response) {
      if (response.success) {
        // clear any previous error messages
        const errorLists = document.querySelectorAll("#changePasswordModal ul");
        errorLists.forEach((list) => list.remove());
        const submitButton = changePasswordForm.querySelector('#changePasswordSubmit');
        const successMessage = document.createElement("p");
        successMessage.setAttribute("id", "changePasswordSuccessMessage");
        successMessage.textContent = "Password successfully changed!";
        successMessage.setAttribute("style", "color: green;");
        successMessage.setAttribute("class", "m-0");
        submitButton.after(successMessage);
        // reset form
        changePasswordForm.reset();
      } else {
        for (const elementId in response.data.data) {
          const errorList = document.createElement("ul");
          const erroredInput = document.querySelector(`#${elementId}`);
          erroredInput.after(errorList);
          erroredInput.setAttribute("style", "border-color: red;");
          if (response.data.data[elementId].length > 0) {
            for (const error in response.data.data[elementId]) {
              const listItem = document.createElement("li");
              listItem.textContent = response.data.data[elementId][error];
              errorList.appendChild(listItem);
            }
            
          }
        }
      }
    });
  });
});

$("#changePasswordModal").on("hidden.bs.modal", function () {
  const errorLists = document.querySelectorAll("#changePasswordModal ul");
  errorLists.forEach((list) => list.remove());
  // reset input border color
  const passwordInputs = document.querySelectorAll("#changePasswordModal input[type='password']");
  passwordInputs.forEach((input) => input.setAttribute("style", ""));

  // clear form
  document.querySelector("#changePasswordModal form").reset();
  // clear success message
  const successMessage = document.querySelector("#changePasswordSuccessMessage");

  if (successMessage) {
    successMessage.remove();
  }
});