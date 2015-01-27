from contests.models import Contest, Submission


class CurrentContestMiddleware(object):
    def process_request(self, request):
        request.contests = Contest.objects.order_by('-number')
        for contest in request.contests:
            contest.can_vote = (request.user.is_authenticated() and Submission.objects.filter(user=request.user).count() > 0)
        try:
            request.current_contest = request.contests[0]
        except:
            request.current_contest = None
