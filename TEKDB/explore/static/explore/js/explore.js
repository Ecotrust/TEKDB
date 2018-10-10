$(document).ready(function() {
	setFilter();
    matchHeight();
});

function setFilter() {
 	var category = $('#search-category-type')[0].value;
 	$('.btn-default').removeClass('selected');
 	$('#category-btn-'+category).addClass('selected');
}

//This function makes the All button the same height as the others, even though it has no icon."
function matchHeight() {
    // var btnheight = $('.btn-group-justified').height();
    // $('#category-btn-all').height(btnheight);
    $('#category-btn-all').height(25);
    $('.form-control').height(25);
    $('.btn-secondary').height(25);
}


/*
function eqHeightBtns() {
    var highestBox = 0;
    $('.btn-group-justified .btn').each(function(){  
        if($(this).height() > highestBox){  
            highestBox = $(this).height();  
        }
    	});    
    $('.btn-group-justified .btn').height(highestBox);
}
*/

/*This function runs when the users clicks the Search button.*/
function setCategoryType(category) {
	$('#search-category-type')[0].value = category;
    $('.selected').removeClass('selected');
    $('#category-btn-'+category).addClass('selected');
}