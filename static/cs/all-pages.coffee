ALL_PAGES =
    home: ->

$ ->
    $('.alert').slideDown()
    setTimeout (->
        $('.alert').slideUp()
    ), 4000

    state = $('#countdown-timer').data('state')
    start_time = $('#countdown-timer').data('start')
    end_time = $('#countdown-timer').data('end')
    submission_time = $('#countdown-timer').data('submission')
    judging_time = $('#countdown-timer').data('judging')
    if state == 'before'
        $('#countdown-timer').countdown
            until: new Date(start_time)
    if state == 'during'
        $('#countdown-timer').countdown
            until: new Date(end_time)
    if state == 'submission'
        $('#countdown-timer').countdown
            until: new Date(submission_time)
    if state == 'judging'
        $('#countdown-timer').countdown
            until: new Date(judging_time)

    cl = $('body').attr('class')
    if cl and cl of ALL_PAGES then ALL_PAGES[cl]()
