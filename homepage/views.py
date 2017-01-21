import datetime

from django.shortcuts import render

from posts.models import Posts


def homepage(request):
    now = datetime.datetime.now()
    entry = Posts.objects.all()
    return render(request, 'homepage.html', {'title': entry[0].title, 'postlist': entry})
