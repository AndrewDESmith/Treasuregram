$('button').on('click', function(event) {
  event.preventDefault();
  var element = $(this);
  $.ajax({
    url : '/like_treasure/',
    type : 'POST',
    // data-id = {{ treasure.id }} on the like <button> element
    data : { treasure_id: element.attr("data-id") },
    // Capture the returned likes from the like_treasure function in views.py, and use that value to update the button element:
    success : function(response) {
      element.html(' ' + response);
    }
  });
});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
  // These HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      // Will run for any POSTs or non-cross-domain requests:
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});
