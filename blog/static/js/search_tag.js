// function searchTag(tag) {
//   $("#tag-input").val(tag);
//   $("#tag-form").submit(function (e) {
//     e.preventDefault();
//   });
//   return false;
// }

$(".-tag").click(function (e) {
  console.log("hereeee");
  e.preventDefault();
  console.log($(this).text());
  $("#tag-input").val($(this).text().substring(1));
  $("#tag-form").submit();
});
