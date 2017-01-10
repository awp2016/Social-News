from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from login.models import UserForm


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/homepage/')
    else:
        form = UserForm()
    return render(request, 'registration/register_user.html', {'form': form})