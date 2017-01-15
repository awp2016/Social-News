from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from posts.models import PostForm


def addpost(request):
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
