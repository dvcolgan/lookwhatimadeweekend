from lwimw.models import Contest, user_can_vote, Submission
from django.utils import timezone


def common(request):
    contests = Contest.objects.order_by('-start')
    current_contest = None
    if contests.exists():
        for contest in contests:
            contest.can_vote = (request.user.is_authenticated() and Submission.objects.filter(user=request.user).count() > 0)
        current_contest = contests[0]

    return locals()
