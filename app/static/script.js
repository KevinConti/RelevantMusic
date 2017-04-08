$(document).ready(function(){

    //Logic for when a button is clicked
    //1) Button most transition to top-center
    //2) All currently visible buttons dissapear (except clicked)
    //3) User's view returns to the top of the page
    //4) New buttons are displayed
    $("button").click(function(){
        //Hide all buttons except clicked button
        //TODO do this all at once, this is silly
        $(this).addClass('selected');
        var allOptionButtons = $('button.optionBlock');
        var allMusicButtons = $('button.musicBlock');
        $(allOptionButtons).each(function() {
            if ($(this).hasClass('selected') === false){
                $(this).fadeOut("slow", function(){
                    $(this).hide();
                });
            }
        });
        $(allMusicButtons).each(function() {
            if ($(this).hasClass('selected') === false){
                $(this).fadeOut("slow", function(){
                    $(this).hide();
                });
            }
        });
        //Bring 'selected' button to center
        if ($('#firstRow').children() > 0){
            var killChildren = $('#firstRow').children();
            $(killChildren).each(function() {
                $(this).removeClass('selected');
            });
            //TODO: Kill them somehow or put them somewhere gently
            //Don't forget to use the .each method! Also it will be $(killChildren)
        }
        var divWrapper = $('.selected').parent();
        $('#middleColumn').replaceWith($(divWrapper));
        $('divWrapper').children($('.selected')).attr('id', 'middleColumn');

    });

});
