from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib import messages 
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.db.models import Sum, Avg, Count
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import *
from django.shortcuts import _get_queryset
from lwimw.models import *
from lwimw.forms import *
from util.functions import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied

import random
import math
import ipdb

import datetime

def home(request):
    current_contest = RequestContext(request)['current_contest']
    post_list = Post.objects.order_by('-creation_date')
    paginator = Paginator(post_list, 20)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'home.html', locals())

def guidelines(request):
    return render(request, 'guidelines.html', locals())

@login_required
def profile(request, user_id=None):
    if user_id == None:
        return HttpResponseRedirect(reverse('profile', args=(request.user.id,)))
    user = get_object_or_404(User, id=user_id)
    submissions = user.submissions.order_by('contest')
    posts = Post.objects.filter(author=user)
    return render(request, 'profile.html', locals())

def irc(request):
    return render(request, 'irc.html', locals())

@login_required
def submission_edit(request, number):
    current_contest = RequestContext(request)['current_contest']
    contest = get_object_or_404(Contest, number=number)
    if contest.pk != current_contest.pk:
        raise PermissionDenied
    else:
        state == contest.get_contest_state(timezone.now())
        if state != 'during' and state != 'submitting':
            raise PermissionDenied
    submission = get_object_or_None(Submission, user=request.user, contest=contest)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES, instance=submission)
        form.instance.user = request.user
        form.instance.contest = contest
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Submission updated successfully!')
            return HttpResponseRedirect(reverse('submission_detail', args=(contest.number, request.user.id)))
    else:
        form = SubmissionForm(instance=submission)
    return render(request, 'submission_edit.html', locals())

def submission_detail(request, number, user_id):
    user_id = int(user_id)
    contest = get_object_or_404(Contest, number=number)
    submission = get_object_or_None(Submission, user=user_id, contest=contest)
    current_contest_state = contest.get_contest_state(timezone.now())
    if submission is None:
        return HttpResponseRedirect(reverse('submission_edit', args=(contest.number,)))
    # If this is anther person's profile page, allow voting if you also have an entry
    if request.user.is_authenticated():
        your_submission = get_object_or_None(Submission, user=request.user, contest=contest)
    else:
        your_submission = None
    can_vote = (your_submission is not None and submission.id != your_submission.id)
    if can_vote and submission.receive_ratings:
        rating = get_object_or_None(Rating, rater=request.user, submission=submission)
        if request.method == 'POST':
            rating_form = RatingForm(request.POST, instance=rating)
            rating_form.instance.rater = request.user
            rating_form.instance.submission = submission
            if rating_form.is_valid():
                rating_form.save()
                messages.add_message(request, messages.SUCCESS, 'Your rating has been recorded!')
                return HttpResponseRedirect(reverse('submissions_list', args=(contest.number,)))
        else:
            rating_form = RatingForm(instance=rating)

    return render(request, 'submission_detail.html', locals())

def submissions_list(request, number):
    contest = get_object_or_404(Contest, number=number)

    submissions = contest.submissions.annotate(num_ratings=Count('ratings')).order_by('num_ratings')

    if request.user.is_authenticated():
        your_submission = get_object_or_None(Submission, user=request.user, contest=contest)
    else:
        your_submission = None
    can_vote = (your_submission != None)

    return render(request, 'submissions_list.html', locals())

@login_required
def post_list(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'post_list.html', locals())
    
    
@login_required
def post_create(request):
    current_contest = RequestContext(request)['current_contest']
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        form.instance.contest = current_contest
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your post has been published!')
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = CreatePostForm()
    return render(request, 'post_create.html', locals())

@login_required
def post_edit(request, post_id):
    current_contest = RequestContext(request)['current_contest']
    post = get_object_or_404(Post, id=post_id)
    if post.author.pk != request.user.pk:
        raise PermissionDenied
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES, instance=post)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your post has updated successfully!')
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = CreatePostForm(instance=post)
    return render(request, 'post_edit.html', locals())

def post_detail(request, post_id):
    current_contest = RequestContext(request)['current_contest']
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', locals())
