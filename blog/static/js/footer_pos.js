$(window).resize(function () {
  if ($("body").height() + 200 > $(window).height()) {
    $("footer").removeClass("fixed-bottom");
    $(".content").removeClass("padding-for-footer");
  } else {
    $("footer").addClass("fixed-bottom");
    $(".content").addClass("padding-for-footer");
  }
});

$(document).ready(function () {
  if ($("body").height() + 200 > $(window).height()) {
    $("footer").removeClass("fixed-bottom");
    $(".content").removeClass("padding-for-footer");
  } else {
    $("footer").addClass("fixed-bottom");
    $(".content").addClass("padding-for-footer");
  }
});
