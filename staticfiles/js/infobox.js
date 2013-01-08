function addInfoboxNature() {
	var id = $(this).attr('id');
	var cookieName = 'infobox:'+id
	if($.cookie(cookieName) != null) {
		$(this).css('display', 'none');
		$.cookie(cookieName, '', { expires: 365, path: '/' });
	}
	else {
		var box = $(this);
		$(this).find("a.hide").click(function() {
    	    $.cookie(cookieName, '', { expires: 365, path: '/' });
    	    box.slideUp();
    	});
    	$(this).find("a.more").click(function() {
    	    $.cookie(cookieName, '', { expires: 365, path: '/' });
    	});

	}
}