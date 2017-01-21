from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.forms.models import ModelForm


# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=30)
    upvotes = models.IntegerField(default=0)
    users_liked = models.ManyToManyField(User)
    content = models.TextField(default="")


class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class Comment(models.Model):
    content = models.TextField(default="")
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'post']
