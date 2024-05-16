$(function () {
    $('DIV#red_header').click(function() {
        if ($('header').hasClass('red')) {
            $('headeer').removeClass('red');
             }
            else {
                $('header').addClass('red');

            }
        })
})