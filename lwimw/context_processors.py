from lwimw.models import *

def common(request):
    current_contest_state = Contest.objects.get_current_contest_state()
    current_contest = Contest.objects.latest()
    return locals()
