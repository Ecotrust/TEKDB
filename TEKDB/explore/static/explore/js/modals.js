$('#loginModal').on('shown.bs.modal', function () {
  $('#loginInput').focus()
  $(this).find('input[type="submit"]').on('submit', function(event) {
    event.preventDefault();
    /** 
     * 1. Write a test for this
     * then code:
     * 2. Make login AJAX request
     * 3. Added logic for better error message
     * 4. ...
     * */
  });
})
