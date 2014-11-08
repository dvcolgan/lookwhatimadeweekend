from django import forms
from blog.models import *


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('contest', 'author', 'deleted', 'comments')


class CreatePostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        exclude = ('author', 'post', 'comment_replied', 'creation_date', 'comment_level', 'deleted')
