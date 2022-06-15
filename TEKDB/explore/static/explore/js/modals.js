$('#loginModal').on('shown.bs.modal', function () {
  $('#loginInput').focus()
  var loginForm = document.querySelector('#loginModal form');
  console.log(loginForm);
  loginForm.addEventListener('submit', function(event) {
    event.preventDefault();
    // account.signIn(event, this);
    /** 
     * 1. Write a test for this
     * then code:
     * 2. Make login AJAX request
     * 3. Added logic for better error message
     * 4. ...
     * */
  });
})
