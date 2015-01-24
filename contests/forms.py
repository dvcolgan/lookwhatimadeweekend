from django import forms
from contests.models import Submission, Rating


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        exclude = ('contest', 'user', 'images')


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ('rater', 'submission')
