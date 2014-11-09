$(window).scroll(function() {
    if ($(".navbar").offset().top > 0) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
});

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Closes the Responsive Menu on Menu Item Click
//$('.navbar-collapse ul li a').click(function() {
//    $('.navbar-toggle:visible').click();
//});

$('.navbar-nav').hover(
  function() {
    header = $('.intro .intro-body .brand-heading .title')
    if ($('.navbar-nav').offset().left < header.offset().left + header.width()) {
      $('.intro .intro-body .brand-heading').hide();
    }
  }, function() {
    timeout = window.setTimeout(function () {
      $('.intro .intro-body .brand-heading').show();
    }, 500);
  }
);

