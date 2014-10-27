$(function() {
    $('.theme-vote a.up').click(function(e) {
        e.preventDefault();
        var $vote = $(this).parent();
        $prev = $vote.prev();
        if ($prev.hasClass('theme-vote')) {
            console.log($prev);
            $vote.detach();
            $vote.insertBefore($prev);
        }
    })

    $('.theme-vote a.down').click(function(e) {
        e.preventDefault();
        var $vote = $(this).parent();
        $next = $vote.next();
        if ($next.hasClass('theme-vote')) {
            console.log($next);
            $vote.detach();
            $vote.insertAfter($next);
        }
    })
});