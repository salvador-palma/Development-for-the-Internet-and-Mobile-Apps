$(document).ready(function() {

  $(window).scroll(function () {

    if ($(window).scrollTop() > 75) {
      $('#Header').addClass('Header-Simplified');
    }

    if ($(window).scrollTop() < 76) {
      $('#Header').removeClass('Header-Simplified');
    }
  });
});