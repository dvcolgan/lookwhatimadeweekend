from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from blog.forms import *

# Create your views here.
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
            return redirect('profile')
    else:
        form = CreatePostForm()
    return render(request, 'post_create.html', locals())

@login_required
def post_edit(request, post_id):
    current_contest = RequestContext(request)['current_contest']
    post = get_object_or_404(Post, id=post_id)
    if post.author.pk != request.user.pk:
        return redirect('home')
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES, instance=post)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your post has updated successfully!')
            return redirect('profile')
    else:
        form = CreatePostForm(instance=post)
    return render(request, 'post_edit.html', locals())

def post_detail(request, post_id):
    current_contest = RequestContext(request)['current_contest']
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CreatePostCommentForm(request.POST)
        form.instance.author = request.user
        form.instance.post = post
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment has been added!')
            return redirect('post_detail', post_id=post.id)
    else:
        form = CreatePostCommentForm()
        comments = PostComment.objects.all().select_related().filter(post=post)
    return render(request, 'post_detail.html', locals())