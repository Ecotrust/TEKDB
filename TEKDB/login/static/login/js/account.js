// using jQuery to get CSRF Token
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

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

var account = {
    signIn: function(event, form, callback) {
        var formData = $(form).serialize();
        var url = '/login_async/'; // default form action url
        $.ajax({
            url: url,
            type: 'POST',
            data: formData,
            dataType: 'json',
            success: function(response) {
                if (response.success === true) {
                    console.log('%csuccessfully signed in user', 'color:green;');
                    callback(true);
                    // main.auth.success(response);
                } else {
                    console.log('%cerror with sign in credentials: %o', 'color: red;', response);
                }
            },
            error: function(response) {
                console.log('%cerror with sign in request submission: %o', 'color: red', response);
            }
        });
    },
    logOut: function() {
        $.ajax({
            url: '/account/logout_async/',
            success: function (response) {
                alert('You have been signed out of your account')
                document.location.reload();
            },
            error: function(response) {
                console.log('%cerror while logging out user', 'color:red');
            }
        })
    },
    register: function(event, form) {
        var formData = $(form).serialize();
        var url = '/account/register_login_async/';
        $.ajax({
            url: url,
            type: 'POST',
            data: formData,
            dataType: 'json',
            success: function (response) {
                console.log('%csuccessfully registered in user', 'color:green;');
                if (response.success === true) {
                    main.auth.success(response);
                } else {
                    document.querySelector('#registration-error').innerHTML = `${response.error}. Please update then submit`;
                }
            },
            error: function(response) {
                console.log('%cerror registering in user', 'color:red;');
            }
        })
    },
    success: function(data) {
        var docLocation = document.location.pathname;
        // set new csrf token'
        if (docLocation.includes('app')) {
            csrftoken = getCookie('csrftoken');
            if (app) {
                $('#nav-load-save').removeClass('hide');
                $('#subnav-sign-in-modal').addClass('hide');
            }
        }
        $('#login-modal').modal('hide');
        // show alert
        $('body').prepend(`<div class="alert alert-success fade show" role="alert" style="position: fixed; top: 30px; left: 50%; padding: 1em 1.5em; transform: translate(-50%,0); min-width: 20%; z-index: 9999; text-align: center; font-size: 1em;">Success! <br />Welcome Back ${data.username}</div>`);
        window.setTimeout(function() {
            $('.alert').alert('close');
        }, 5000);
        // menu navicon hide login  &
        // add account link + sign out link
        $('#menu #sign-in-modal').before(`<a href="/account/" class="list-group-item list-group-item-action">${data.username}</a><button id="sign-out" data-action="sign-out" class="list-group-item list-group-item-action">Sign out</button>`);
        $('#menu #sign-in-modal').css('display', 'none');
        // Hide top nav login and create account button
        $('.username-wrap #sign-in-modal-2').before(`<a id="topnav-account-link" href="/account/" class="btn btn-link account-action">
            <i class="svg_icon"><img src="/static/ucsrb/img/icon/i_user_blue.svg" /></i>${data.username}</a>`);
        $('.username-wrap #sign-in-modal-2').css('display', 'none');
        // hide submenu login
        $('#subnav-sign-in-modal').addClass('d-none');
    }
};