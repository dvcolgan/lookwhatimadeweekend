$(function() {
    $('.theme-vote a.up').click(function(e) {
        e.preventDefault();
        var $vote = $(this).parent();
        $prev = $vote.prev();
        if ($prev.hasClass('theme-vote')) {
            $vote.detach();
            $vote.insertBefore($prev);
        }
    })

    $('.theme-vote a.down').click(function(e) {
        e.preventDefault();
        var $vote = $(this).parent();
        $next = $vote.next();
        if ($next.hasClass('theme-vote')) {
            $vote.detach();
            $vote.insertAfter($next);
        }
    })

    $('a.save-vote').click(function(e) {
        e.preventDefault();
        var $self = $(this);

        // Make an ordered list of theme ids
        var themes = [];
        $('.theme-vote').each(function(i) {
            $theme = $(this);
            themes.push($theme.attr('id'));
        });

        // POST the order of the themes to the server
        $self.addClass("disabled")
        $.ajax('/themes/vote-submit/', {
            type: 'post',
            dataType: 'text/json',
            data: {'themes': themes},
            complete: function() {
                $self.removeClass("disabled");
            }
        });
    });
});