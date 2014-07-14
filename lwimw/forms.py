from django import forms
from lwimw.models import *


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        exclude = ('contest', 'user')


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ('rater', 'submission')


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('contest', 'author')


class CreatePostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        exclude = ('author', 'post', 'comment_replied', 'creation_date', 'comment_level')
