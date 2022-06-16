
$('#loginModal').on('shown.bs.modal', function () {
  $('#loginInput').focus()
  var loginForm = document.querySelector('#loginModal form');
  console.log(loginForm);
  loginForm.addEventListener('submit', function(event) {
    event.preventDefault();
    var signIn = account.signIn(event, this, function(success) {
      if (success) {
        $('#loginModal').modal('hide');
        const exploreLink = document.querySelector('.nav-explore')
        exploreLink.classList.remove('disabled');
        exploreLink.href = '/explore';
        exploreLink.click();
        
      } else {
        document.querySelector('#login-error').innerHTML = 'Invalid username or password';
      }
    });
    /** 
     * 1. Write a test for this
     * then code:
     * 2. Make login AJAX request
     * 3. Added logic for better error message
     * 4. ...
     * */
  });
})
