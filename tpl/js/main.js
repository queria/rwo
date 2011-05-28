$(document).ready( function () {
	var masstoggle = false;
	var prepare_toggle_button = function(button, items) {
		button.click( function () {
			masstoggle = true;
			if( $(this).hasClass('selected') ) {
				$(this).removeClass('selected');
				items.removeAttr('checked');
			} else {
				$(this).addClass('selected');
				items.attr('checked', 'checked');
			}
			masstoggle = false;
			$('.filters').submit();
			return false;
		});
	};
	var colorize_button = function(button, items) {
		var checked = true;
		items.each( function() {
			if(!$(this).attr('checked')) {
				checked = false;
			}
		});
		if(checked) {
			button.addClass('selected');
		}
	};

	$('.filters .classes').append('<ul><li><a href="#" id="ToggleDefence">Defence</a></li>'
			+'<li><a href="#" id="ToggleMelee">Melee</a></li><li><a href="#" id="ToggleMissile">Missile</a></li>'
		+'</ul>');
	$('.filters .runes h4').each(function () {
		$(this).html('<a href="#">'+($(this).html())+'</a>');
	});
	$('.filters .runes ul').each( function () {
		prepare_toggle_button(
			$('a', $(this)),
			$('input', $(this)));
		colorize_button(
			$('a', $(this)),
			$('input', $(this)));
	});
	var classes = ['Defence', 'Melee', 'Missile'];
	for(var i=0; i<classes.length; ++i) {
		prepare_toggle_button( $('#Toggle'+classes[i]), $('.classes .'+classes[i]));
		colorize_button( $('#Toggle'+classes[i]), $('.classes .'+classes[i]));
	}
	$('.filters input').change(function () {
		$('.filters').submit();
	});
});

