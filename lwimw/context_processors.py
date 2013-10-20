from lwimw.models import *

def common(request):
    current_contest = Contest.objects.latest()
    return locals()
