from django.shortcuts import render

# Create your views here.

def homepage(request):
    now = datetime.datetime.now()
        entry = Posts.objects.all()
        return render(request, 'homepg.html',{ 'title':entry[0].title, 'postlist':entry })
