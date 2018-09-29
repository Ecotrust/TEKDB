$(document).ready(function() {
	setFilter();
	eqHeightBtns();
});

function setFilter() {
 	var category = $('#search-category-type')[0].value;
 	$('.btn-default').removeClass('selected');
 	$('#category-btn-'+category).addClass('selected');
}

function eqHeightBtns() {
    var highestBox = 0;
    $('.btn-group-justified .btn').each(function(){  
        if($(this).height() > highestBox){  
            highestBox = $(this).height();  
        }
    	});    
    $('.btn-group-justified .btn').height(highestBox);
}

/*This function runs when the users clicks the Search button.*/
function setCategoryType(category) {
	$('#search-category-type')[0].value = category;
    $('.selected').removeClass('selected');
    $('#category-btn-'+category).addClass('selected');
}