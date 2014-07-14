window.ALL_PAGES = {
    home: function() {
    }
};

var $imageModal;

$(document).ready(function() {
    $imageModal = $('#image-modal');
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

    // using .on because if you change the DOM, stuff breaks.
    $(document).on('click', 'img:not(#banner)', function(e) {
        e.preventDefault();
        var elem = $(this);
        $imageModal.find('img').attr('src', elem.attr('src'));
        $imageModal.find('#permalink').attr('href', elem.attr('src'));
        $imageModal.modal();
    });

    // if control+enter
    $(document).on('keydown', 'textarea', function(e) {
        var elem = $(this);
        if ((e.keyCode == 10 || e.keyCode == 13) && e.ctrlKey) {
            // ugly way to go up three elements
            elem.parent().parent().parent().submit();
        }
    });

    //var cl = $('body').attr('class');
    //if cl and cl of ALL_PAGES then ALL_PAGES[cl]()
});
