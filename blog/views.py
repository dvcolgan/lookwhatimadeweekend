from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from blog.forms import *
import json

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
            post.comments.add(form.instance)
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment has been added!')
            return redirect('post_detail', post_id=post.id)
    else:
        form = CreatePostCommentForm()
    return render(request, 'post_detail.html', locals())


@login_required
def post_delete(request):
    if request.method == 'POST' and request.is_ajax():
        post = get_object_or_404(Post, id=request.POST.get("id", ''))
        if post.author == request.user:
            post.deleted = True
            post.save()
            return HttpResponse(json.dumps({ 'post_deleted': post.id, "post_author": post.author.username }), content_type='application/json')
        return HttpResponse(json.dumps({ 'error': "You are not the creator of the post!" }), content_type='application/json')
    return HttpResponse(json.dumps({ 'error': "The request was not AJAX or a POST." }), content_type='application/json')


@login_required
def comment_reply(request):
    if request.method == 'POST' and request.is_ajax():
        author = request.user
        post = get_object_or_404(Post, id=request.POST.get("post", ''))
        comment_replied = get_object_or_404(PostComment, id=request.POST.get("comment_replied", ''))
        comment_level_int = int(request.POST.get("comment_level", ''))
        body = request.POST.get("body", '')
        if comment_level_int <= 12 and comment_level_int >= 6:
            comment_level = int(request.POST.get("comment_level", '')) - 1;
        else:
            comment_level = 6
        if author and post and comment_replied and comment_level and body:
            comment = PostComment.objects.create(author=author, post=post, comment_replied=comment_replied, body=body, comment_level=comment_level)
            post.comments.add(comment)
            post.save()
            return HttpResponse(json.dumps({ 'comment_author': author.username, 'comment_post': post.id }), content_type='application/json')
        return HttpResponse(json.dumps({ 'error': "One or more of the values was not filled." }), content_type='application/json')
    return HttpResponse(json.dumps({ 'error': "The request was not AJAX or a POST." }), content_type='application/json')


@login_required
def comment_delete(request):
    if request.method == 'POST' and request.is_ajax():
        comment = get_object_or_404(PostComment, id=request.POST.get("id", ''))
        if comment.author == request.user:
            comment.deleted = True
            comment.post.comments.remove(comment)
            comment.post.save()
            comment.save()
            return HttpResponse(json.dumps({ 'comment_deleted': comment.id, "comment_author": comment.author.username }), content_type='application/json')
        return HttpResponse(json.dumps({ 'error': "You are not the creator of the comment!" }), content_type='application/json')
    return HttpResponse(json.dumps({ 'error': "The request was not AJAX or a POST." }), content_type='application/json')
