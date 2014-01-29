ALL_PAGES =
    home: ->

$ ->
    $('.alert').slideDown()
    setTimeout (->
        $('.alert').slideUp()
    ), 4000

    now = new Date()
    contestYear = parseInt(now.getFullYear())
    contestEndMonth = parseInt(now.getMonth()) + 1
    if contestEndMonth > 11
        contestEndMonth = 0
        contestYear++

    endDate = new Date(contestYear, contestEndMonth, 1)

    $('#contest-timer').countdown
        until: endDate
    $('#judging-timer').countdown
        until: endDate

    cl = $('body').attr('class')
    if cl and cl of ALL_PAGES then ALL_PAGES[cl]()
