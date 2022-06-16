$('#loginModal').on('shown.bs.modal', function () {
  $('#loginInput').focus()
  var loginForm = document.querySelector('#loginModal form');
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
        loginForm.append('Invalid username or password');
      }
    });
  });
})
