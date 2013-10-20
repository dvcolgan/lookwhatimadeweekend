from django.shortcuts import render, get_object_or_404
from django.contrib import messages 
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import *
from django.shortcuts import _get_queryset
from lwimw.models import *
from lwimw.forms import *
from util.functions import *
from django.contrib.auth import authenticate, login
from django.contrib import messages

import random
import math
import ipdb

import datetime

def home(request):
    return render(request, 'home.html', locals())

def guidelines(request):
    return render(request, 'guidelines.html', locals())

def profile(request):
    return render(request, 'profile.html', locals())

def irc(request):
    return render(request, 'irc.html', locals())

def submission(request, number, user_id):
    user_id = int(user_id)
    contest = get_object_or_404(Contest, number=number)
    submission = get_object_or_None(Submission, user=user_id, contest=contest)
    if request.user.id == user_id:
        if request.method == 'POST':
            form = SubmissionForm(request.POST, instance=submission)
            form.instance.user = request.user
            form.instance.contest = contest
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Submission updated successfully!')
                return HttpResponseRedirect(reverse('submission', args=(contest.number,user_id)))
        else:
            form = SubmissionForm(instance=submission)

    return render(request, 'submission.html', locals())

def submissions_list(request, number):
    contest = get_object_or_404(Contest, number=number)
    return render(request, 'submissions_list.html', locals())
    
