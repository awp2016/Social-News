from django.http import HttpResponseRedirect
from django.shortcuts import render

from social_news.models import CommentForm, UserForm, PostForm, Posts


def add_comment(request, post_id):
    if request.method == 'POST':
        updated_data = request.POST.copy()
        updated_data.update({'post': post_id})
        form = CommentForm(data=updated_data)
        if form.is_valid():
            print('Success')
            form.save()
            return HttpResponseRedirect('/post/' + post_id)
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment.html', {'form': form, 'post_id': post_id})


def homepage(request):
    entries = Posts.objects.all()
    return render(request, 'homepage.html', {'entries': entries})


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserForm()
    return render(request, 'registration/register_user.html', {'form': form})


def add_post(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/plzlogin')
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request, 'add-post.html', {'form': form})


def get_post_by_id(request, post_id):
    post = Posts.objects.get(id=post_id)
    comments_list = post.comment_set.all()
    return render(request, 'view_post.html',
                  {'post': post, 'user_list': post.users_liked.all(), 'comments_list': comments_list})


def increase_by_one(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/plzlogin')
    else:
        entry = Posts.objects.get(id=1)
        if request.user not in entry.users_liked.all():
            entry.users_liked.add(request.user)
            entry.upvotes += 1
        entry.save()
        return HttpResponseRedirect('/')


def like_post(request, post_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/plzlogin')
    else:
        entry = Posts.objects.get(id=post_id)
        if request.user not in entry.users_liked.all():
            entry.users_liked.add(request.user)
            entry.upvotes += 1
        entry.save()
        return HttpResponseRedirect('/post/' + post_id)
