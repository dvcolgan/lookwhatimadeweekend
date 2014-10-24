from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy

from django.utils import timezone
from braces.views import LoginRequiredMixin
from lwimw.models import Contest
from .models import Theme, ThemeBump, Vote


def theme_dispatch(request):
    now = timezone.now()
    current_contest = Contest.objects.get_current()
    if (current_contest.get_contest_state(now) == 'before'):
        if (current_contest.get_theme_voting_state(now) == 'voting'):
            return redirect('theme_vote')
        else:
            return redirect('theme_bump')
    else:
        return redirect('home')


class ThemeBumpView(
        LoginRequiredMixin,
        DetailView):
    model = Theme

    def get_object(self):
        bumps = ThemeBump.objects.filter(user=self.request.user)
        themes = Theme.objects.filter(contest=Contest.objects.get_current()).exclude(bumps__in=bumps).order_by('?')
        if themes.count() > 0:
            return themes[0]
        else:
            return None


class ThemeCreateView(
        LoginRequiredMixin,
        CreateView):
    model = Theme
    fields = ('name',)
    success_url = reverse_lazy('theme_bump')

    def form_valid(self, form):
        form.instance.submitted_by = self.request.user
        form.instance.contest = Contest.objects.get_current()
        return super(ThemeCreateView, self).form_valid(form)


def theme_bump_submit(request, pk, direction):
    if request.method == 'POST':
        theme = get_object_or_404(Theme, pk=pk)
        bump, _ = ThemeBump.objects.get_or_create(theme=theme, user=request.user)
        if direction == 'up':
            bump.direction = 'up'
        if direction == 'down':
            bump.direction = 'down'
        bump.save()

    return redirect('theme_bump')
