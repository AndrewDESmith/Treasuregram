$('button').on('click', function(event) {
  event.preventDefault();
  var element = $(this);
  $.ajax({
    url : '/like_treasure/',
    type : 'GET',
    // data-id = {{ treasure.id }} on the like <button> element
    data : { treasure_id: element.attr("data-id") },
    // Capture the returned likes from the like_treasure function in views.py, and use that value to update the button element:
    success : function(response) {
      element.html(' ' + response);
    }
  });
});
