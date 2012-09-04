/*
 * Based on jQuery Lightbox plugin
 */

function showLightboxFunc(lightbox, overlay) {
	return function() {
	// Get page sizes
	var arrPageSizes = ___getPageSize();
	// Style overlay and show it
	overlay.css({
		opacity:			'0.8',
		width:				arrPageSizes[0],
		height:				arrPageSizes[1]
	}).fadeIn();
	// Get page scroll
	var arrPageScroll = ___getPageScroll();
	// Calculate top and left offset for the jquery-lightbox div object and show it
	lightbox.css({
		//display:			'block',
		top:	arrPageScroll[1] + (arrPageSizes[3] / 10),
		left:	arrPageScroll[0] + arrPageSizes[0] / 2 - lightbox.width() / 2
	}).slideDown();
	// Assigning click events in elements to close overlay
	overlay.click(function() {
		overlay.fadeOut();
		lightbox.hide();
	});
	lightbox.find('a.close').click(function() {
		overlay.fadeOut();
		lightbox.hide();
		return false;
	});
	
	// If window was resized, calculate the new overlay dimensions
	$(window).resize(function() {
		// Get page sizes
		var arrPageSizes = ___getPageSize();
		// Style overlay and show it
		overlay.css({
			width:		arrPageSizes[0],
			height:		arrPageSizes[1]
		});
		// Get page scroll
		var arrPageScroll = ___getPageScroll();
		// Calculate top and left offset for the jquery-lightbox div object and show it
		lightbox.css({
			top:	arrPageScroll[1] + (arrPageSizes[3] / 10),
			left:	arrPageScroll[0] + arrPageSizes[0] / 2 - lightbox.width() / 2
		});
	});
	
	// Refresh IFrames within lightbox
	lightbox.find( 'iframe' ).attr( 'src', function ( i, val ) { return val; });

	return false;
	}
} 

/**
 / THIRD FUNCTION
 * getPageSize() by quirksmode.com
 *
 * @return Array Return an array with page width, height and window width, height
 */
function ___getPageSize() {
	var xScroll, yScroll;
	if (window.innerHeight && window.scrollMaxY) {	
		xScroll = window.innerWidth + window.scrollMaxX;
		yScroll = window.innerHeight + window.scrollMaxY;
	} else if (document.body.scrollHeight > document.body.offsetHeight){ // all but Explorer Mac
		xScroll = document.body.scrollWidth;
		yScroll = document.body.scrollHeight;
	} else { // Explorer Mac...would also work in Explorer 6 Strict, Mozilla and Safari
		xScroll = document.body.offsetWidth;
		yScroll = document.body.offsetHeight;
	}
	var windowWidth, windowHeight;
	if (self.innerHeight) {	// all except Explorer
		if(document.documentElement.clientWidth){
			windowWidth = document.documentElement.clientWidth; 
		} else {
			windowWidth = self.innerWidth;
		}
		windowHeight = self.innerHeight;
	} else if (document.documentElement && document.documentElement.clientHeight) { // Explorer 6 Strict Mode
		windowWidth = document.documentElement.clientWidth;
		windowHeight = document.documentElement.clientHeight;
	} else if (document.body) { // other Explorers
		windowWidth = document.body.clientWidth;
		windowHeight = document.body.clientHeight;
	}	
	// for small pages with total height less then height of the viewport
	if(yScroll < windowHeight){
		pageHeight = windowHeight;
	} else { 
		pageHeight = yScroll;
	}
	// for small pages with total width less then width of the viewport
	if(xScroll < windowWidth){	
		pageWidth = xScroll;		
	} else {
		pageWidth = windowWidth;
	}
	arrayPageSize = new Array(pageWidth,pageHeight,windowWidth,windowHeight);
	return arrayPageSize;
};
/**
 / THIRD FUNCTION
 * getPageScroll() by quirksmode.com
 *
 * @return Array Return an array with x,y page scroll values.
 */
function ___getPageScroll() {
	var xScroll, yScroll;
	if (self.pageYOffset) {
		yScroll = self.pageYOffset;
		xScroll = self.pageXOffset;
	} else if (document.documentElement && document.documentElement.scrollTop) {	 // Explorer 6 Strict
		yScroll = document.documentElement.scrollTop;
		xScroll = document.documentElement.scrollLeft;
	} else if (document.body) {// all other Explorers
		yScroll = document.body.scrollTop;
		xScroll = document.body.scrollLeft;	
	}
	arrayPageScroll = new Array(xScroll,yScroll);
	return arrayPageScroll;
};
