from lwimw.models import Contest, user_can_vote
from django.utils import timezone


def common(request):
    contests = Contest.objects.order_by('-start')
    for contest in contests:
        contest.can_vote = request.user.is_authenticated() and user_can_vote(request.user, contest.submissions.all())
    if contests:
        current_contest = contests[0]
    else:
        current_contest = None
    current_contest = contests[0]
    #now = timezone.now()

    return locals()
