if ($(window).width() <= 1230){
  console.log('small');
}
/*
$(window).scroll(function(){
  var wScroll = $(this).scrollTop();
  if(wScroll < 1110){
    $('.imagediv.one').css('background-position', 'top -' + wScroll/3 + 'px center');
  }
  if(wScroll > 700){
    $('.imagediv.two').css('background-position', 'top -' + (-1200 + wScroll) /4 + 'px center');
  }
  if(wScroll > 1780){
    $('.imagediv.three').css('background-position', 'top -' + (-2300 + wScroll) /1.5 + 'px center');
  }
  console.log(wScroll);
});
*/

$(function() {
  $('a[href*="#"]:not([href="#"])').click(function() {
    if (location .pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});
