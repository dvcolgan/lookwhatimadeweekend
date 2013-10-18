ALL_PAGES =
    home: ->

$ ->
    cl = $('body').attr('class')
    if cl and cl of ALL_PAGES then ALL_PAGES[cl]()
