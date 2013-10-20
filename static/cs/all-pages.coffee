ALL_PAGES =
    home: ->

$ ->
    $('.alert').slideDown()
    setTimeout (->
        $('.alert').slideUp()
    ), 4000
    cl = $('body').attr('class')
    if cl and cl of ALL_PAGES then ALL_PAGES[cl]()
