$(".input-group-append").click(function (e) {
  if ($("#rounded-input").val().trim() != "") {
    $("#nav-form").submit();
  }
});

$(".-tag").click(function (e) {
  e.preventDefault();
  $("#tag-input").val($(this).text().substring(1));
  $("#tag-form").submit();
});
