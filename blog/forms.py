from django import forms
from blog.models import Post
from comments.models import Comment


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('contest', 'author', 'deleted', 'comments')


class CreatePostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('reply', 'author', 'post', 'comment_replied', 'creation_date', 'comment_level', 'deleted')
