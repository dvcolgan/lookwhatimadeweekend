window.ALL_PAGES = {
    home: function() {
    }
};

$(document).ready(function() {
    $('.alert').slideDown();
    setTimeout(function() {
        $('.alert').slideUp();
    }, 4000);

    var state = $('#countdown-timer').data('state');
    var startTime = $('#countdown-timer').data('start');
    var endTime = $('#countdown-timer').data('end');
    var submissionTime = $('#countdown-timer').data('submission');
    var judgingTime = $('#countdown-timer').data('judging');

    if (state === 'before') {
        $('#countdown-timer').countdown({
            until: new Date(startTime)
        });
    }
    if (state === 'during') {
        $('#countdown-timer').countdown({
            until: new Date(endTime)
        });
    }
    if (state === 'submission') {
        $('#countdown-timer').countdown({
            until: new Date(submissionTime)
        });
    }
    if (state === 'judging') {
        $('#countdown-timer').countdown({
            until: new Date(judgingTime)
        });
    }

    //var cl = $('body').attr('class');
    //if cl and cl of ALL_PAGES then ALL_PAGES[cl]()
});
