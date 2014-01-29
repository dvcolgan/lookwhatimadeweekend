ALL_PAGES =
    home: ->

$ ->
    $('.alert').slideDown()
    setTimeout (->
        $('.alert').slideUp()
    ), 4000

    state = $('#countdown-timer').data('state')
    startTime = $('#countdown-timer').data('start')
    endTime = $('#countdown-timer').data('end')
    submissionTime = $('#countdown-timer').data('submission')
    judgingTime = $('#countdown-timer').data('judging')

    if state == 'before'
        $('#countdown-timer').countdown
            until: new Date(startTime)
    if state == 'during'
        $('#countdown-timer').countdown
            until: new Date(endTime)
    if state == 'submission'
        $('#countdown-timer').countdown
            until: new Date(submissionTime)
    if state == 'judging'
        $('#countdown-timer').countdown
            until: new Date(judgingTime)

    cl = $('body').attr('class')
    if cl and cl of ALL_PAGES then ALL_PAGES[cl]()
