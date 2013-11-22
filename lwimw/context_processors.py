from lwimw.models import *
from django.utils import timezone

def common(request):
    contests = Contest.objects.order_by('-year', '-month')
    current_contest = contests[0]
    now = timezone.now()
    if current_contest.year != now.year or current_contest.month != now.month:
        next_year = current_contest.year
        next_month = current_contest.month + 1
        if next_month > 12:
            next_year += 1
            next_month = 1

        contests = Contest.objects.order_by('-year', '-month')
        current_contest = Contest.objects.create(
            number=current_contest.number + 1,
            theme='Announced Soon',
            month=next_month,
            year=next_year,
        )

    for contest in contests:
        contest.user_can_vote = len(contest.submissions.filter(user=request.user)) > 0
        contest.user_has_or_can_create_entry = (
            current_contest.year == contest.year and
            current_contest.month == contest.month
        ) or contest.user_can_vote

    return locals()
