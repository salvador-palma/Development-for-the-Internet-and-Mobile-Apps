$(document).ready(function() {

  $(window).scroll(function () {

    console.log($(window).scrollTop());

    if ($(window).scrollTop() > 150) {
      $('#Header').addClass('Header-Simplified');
    }

    if ($(window).scrollTop() < 151) {
      $('#Header').removeClass('Header-Simplified');
    }
  });
});