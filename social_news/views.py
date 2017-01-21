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
            return HttpResponseRedirect('/homepage/')
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
            return HttpResponseRedirect('/homepage')
    else:
        form = PostForm()
    return render(request, 'addpost.html', {'form': form})
