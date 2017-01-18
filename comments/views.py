from django.http import HttpResponseRedirect
from django.shortcuts import render

def add_comment(request,post_id):
    if request.method == 'POST':
        updated_data = request.POST.copy()
        updated_data.update({'post': post_id})
        form = CommentForm(data = updated_data)
        if form.is_valid():
            print('Success')
            form.save()
            return HttpResponseRedirect('/post/'+post_id)
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment.html', {'form': form,'post_id' : post_id})