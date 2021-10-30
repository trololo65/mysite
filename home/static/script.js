var countg = 20;
function volna(count) {
	count++;
	
	if (count == 40) {
		return antiVolna(count);
	}
	
	$('.scroll').css('boxShadow', '0px 0px '+ count +'px 15px #fff');
	setTimeout(function() {
		volna(count);	
	}, 130);
}

function antiVolna(count) {
	count--;
	
			
	if (count == 20) {
		return volna(count)
	}
	$('.scroll').css('boxShadow', '0px 0px '+ count +'px 15px #fff');
	setTimeout(function() {
		antiVolna(count);
	}, 130);
}
volna(countg)

$('.scroll a').on('click', function() {
  var el = $(this);
  var dest = el.attr('href'); // получаем направление
  if (dest !== undefined && dest !== '') { // проверяем существование
    $('html').animate({
        scrollTop: $(dest).offset().top // прокручиваем страницу к требуемому элементу
      }, 500 // скорость прокрутки
    );
  }
  return false;
});