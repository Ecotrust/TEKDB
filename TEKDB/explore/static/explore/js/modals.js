const LOGIN_MODAL_ID = "loginModal";
const LOGIN_INPUT_ID = "loginInput";
const loginForm = document.querySelector(`#${LOGIN_MODAL_ID} form`);
const LOGIN_ERROR_MESSAGE = "Invalid username or password";

$(`#${LOGIN_MODAL_ID}`).on("shown.bs.modal", function () {
  $(`#${LOGIN_INPUT_ID}`).focus();
});

loginForm.addEventListener("submit", function (event) {
  event.preventDefault();
  account.signIn(event, this, function (success) {
    if (success) {
      $(`#${LOGIN_MODAL_ID}`).modal("hide");
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

const CHANGE_PASSWORD_MODAL_ID = "changePasswordModal";
const CHANGE_PASSWORD_SUCCESS_ID = "changePasswordSuccessMessage";
const CHANGE_PASSWORD_SUCCESS_MESSAGE = "Password successfully changed!";
const changePasswordForm = document.querySelector(`#${CHANGE_PASSWORD_MODAL_ID} form`);

changePasswordForm.addEventListener("submit", function (event) {
  event.preventDefault();
  account.changePassword(event, this, function (response) {
    if (response.success) {
      // clear any previous error messages
      const errorLists = document.querySelectorAll(`#${CHANGE_PASSWORD_MODAL_ID} ul`);
      if (errorLists.length) {
          errorLists.forEach((list) => list.remove());
      }
      // clear any previous success message
      const previousSuccessMessage = document.querySelector(`#${CHANGE_PASSWORD_SUCCESS_ID}`);
      if (!previousSuccessMessage) {
        // display success message
        const successMessage = document.createElement("p");
        successMessage.setAttribute("id", `${CHANGE_PASSWORD_SUCCESS_ID}`);
        successMessage.textContent = CHANGE_PASSWORD_SUCCESS_MESSAGE;
        successMessage.setAttribute("style", "color: green;");
        successMessage.setAttribute("class", "m-0");

        // insert success message after submit button
        const submitButton = changePasswordForm.querySelector('#changePasswordSubmit');
        submitButton.after(successMessage);
      }
      
      // reset form
      changePasswordForm.reset();
    } else {
      // display error messages
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

$(`#${CHANGE_PASSWORD_MODAL_ID}`).on("hidden.bs.modal", function () {
  // clear error messages
  const errorLists = document.querySelectorAll(`#${CHANGE_PASSWORD_MODAL_ID} ul`);
  errorLists.forEach((list) => list.remove());
  // reset input border color
  const passwordInputs = document.querySelectorAll(`#${CHANGE_PASSWORD_MODAL_ID} input[type='password']`);
  passwordInputs.forEach((input) => input.setAttribute("style", ""));
  // clear form
  document.querySelector(`#${CHANGE_PASSWORD_MODAL_ID} form`).reset();
  // clear success message
  const successMessage = document.querySelector(`#${CHANGE_PASSWORD_SUCCESS_ID}`);

  if (successMessage) {
    successMessage.remove();
  }
});