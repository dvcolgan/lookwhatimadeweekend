window.ALL_PAGES = {
    home: function() {
    }
};

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var $imageModal;
var $deleteConfirmModal;

$(document).ready(function() {
    $imageModal = $('#image-modal');
    $deleteConfirmModal = $('#delete-modal');
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
        // Don't go to the image link.
        e.preventDefault();
        // Get the current element clicked
        var elem = $(this);
        // Find the image element in the modal.
        $imageModal.find('img').attr('src', elem.attr('src'));
        // Find the image's permalink
        $imageModal.find('#permalink').attr('href', elem.attr('src'));
        // Open the modal
        $imageModal.modal();
    });

    // if control+enter
    $(document).on('keydown', 'textarea', function(e) {
        // Get the text area.
        var elem = $(this);
        // if space is pressed along with control.
        if ((e.keyCode == 10 || e.keyCode == 13) && e.ctrlKey) {
            // ugly way to go up three elements and submit the form.
            elem.parent().parent().parent().submit();
        }
    });

    // open reply form
    $(document).on('click', '.reply', function(e) {
        e.preventDefault();
        // get the reply element clicked.
        var elem = $(this);
        // hide the reply button for no clutter
        elem.slideUp("fast", function() {
            // get the form container and show it.
            elem.next().slideDown("fast");
        });
    });

    // if the reply form is submitted
    $(document).on('submit', '#reply-form', function(e) {
        e.preventDefault();
        // the reply form container element
        var elem = $(this);
        // the reply form element
        var formElem = $(this).children(':first-child');
        // AJAX call to the reply url
        $.ajax({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    // Send the token to same-origin, relative URLs only.
                    // Send the token only if the method warrants CSRF protection
                    // Using the CSRFToken value acquired earlier
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            url: formElem.attr('action'),
            type: formElem.attr('method'),
            data: formElem.serialize(),
            crossDomain: false,
            success: function(data) {
                $('#comments').load(window.location.href + ' #comments');
            }
        });
    });

    $(document).on('click', '.delete', function(e) {
        // Don't go to the link
        e.preventDefault();
        // Get the current element clicked
        var elem = $(this);
        // Find set the id of the object to be deleted
        $deleteConfirmModal.find('#delete-confirm').attr('data-object-id', elem.attr('data-object-id'));
        // Find set the id of the object to be deleted
        $deleteConfirmModal.find('#delete-confirm').attr('data-object-url', elem.attr('data-object-url'));
        // Set the name of the object to be deleted
        $deleteConfirmModal.find('span.name').text(elem.attr('data-object-name'));
        // Open the modal
        $deleteConfirmModal.modal();
    });

    $(document).on('click', '#delete-confirm', function(e) {
        // Don't go to the link
        e.preventDefault();
        // Get the current element clicked
        var elem = $(this);
        // AJAX call to the delete url
        $.ajax({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    // Send the token to same-origin, relative URLs only.
                    // Send the token only if the method warrants CSRF protection
                    // Using the CSRFToken value acquired earlier
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            url: elem.attr('data-object-url'),
            type: 'POST',
            data: { 'id': elem.attr('data-object-id') },
            crossDomain: false,
            success: function(data) {
                location.reload();
            }
        });
        // Hide the modal
        $deleteConfirmModal.modal('hide');
    });

    //var cl = $('body').attr('class');
    //if cl and cl of ALL_PAGES then ALL_PAGES[cl]()
});
