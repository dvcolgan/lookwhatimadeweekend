from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contests.models import Contest, Submission, Rating
from contests.forms import SubmissionForm, RatingForm
from blog.models import Post, PostComment
from util.functions import get_object_or_None


class HomeView(ListView):
    template_name = 'home.html'
    model = Post
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.order_by('-creation_date').filter(deleted=False)


class GuidelinesView(TemplateView):
    template_name = 'guidelines.html'


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'

    def dispatch(self, request, *args, **kwargs):
        if 'pk' not in kwargs:
            return redirect('profile', pk=request.user.pk)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['submissions'] = self.request.user.submissions.order_by('contest')
        context['posts'] = Post.objects.filter(author=self.request.user, deleted=False)
        context['comments'] = PostComment.objects.filter(author=self.request.user, deleted=False, post__deleted=False)
        return context


class IRCView(TemplateView):
    template_name = 'irc.html'


class ContestDetailView(DetailView):
    model = Contest

    def get_object(self):
        return get_object_or_404(Contest, **self.kwargs)


@login_required
def submission_edit(request, number):
    # You can't edit entries from the previous contests
    if int(number) != request.current_contest.number:
        return redirect('profile')
    # You can't edit entries after the contest is over
    else:
        state = request.current_contest.state
        if request.current_contest.state == 'after':
            return redirect('home')

    submission = get_object_or_None(Submission, user=request.user, contest=request.current_contest)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES, instance=submission)
        form.instance.user = request.user
        form.instance.contest = request.current_contest
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Submission updated successfully!')
            return redirect('submission_detail', number=request.current_contest.number, user_id=request.user.id)
    else:
        form = SubmissionForm(instance=submission)
    return render(request, 'contests/submission_form.html', locals())


def submission_detail(request, number, user_id):
    user_id = int(user_id)
    contest = get_object_or_404(Contest, number=number)
    submission = get_object_or_None(Submission, user=user_id, contest=contest)

    # If this is your submission and it doesn't exist yet, redirect to the edit page to make it
    if submission is None and user_id == request.user.pk:
        return redirect('submission_edit', number=contest.number)

    if submission is None and user_id != request.user.pk:
        raise Http404

    # If this is anther person's profile page, allow voting if you also have an entry
    can_vote = request.user.is_authenticated() and Submission.objects.filter(user=request.user).count() > 0 and submission.user != request.user

    if can_vote and submission.receive_ratings:
        rating = get_object_or_None(Rating, rater=request.user, submission=submission)
        if request.method == 'POST':
            rating_form = RatingForm(request.POST, instance=rating)
            rating_form.instance.rater = request.user
            rating_form.instance.submission = submission
            if rating_form.is_valid():
                rating_form.save()
                messages.add_message(request, messages.SUCCESS, 'Your rating has been recorded!')
                return redirect('submissions_list', number=contest.number)
        else:
            rating_form = RatingForm(instance=rating)

    return render(request, 'contests/submission_detail.html', locals())
