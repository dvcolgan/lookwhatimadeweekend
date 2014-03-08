from lwimw.models import Contest, user_can_vote, Submission
from django.utils import timezone


def common(request):
    contests = Contest.objects.order_by('-start')
    for contest in contests:
        contest.can_vote = request.user.is_authenticated() and user_can_vote(request.user, Submission.objects.all())
    current_contest = contests[0]
    #now = timezone.now()

    return locals()
