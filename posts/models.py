from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models

# Create your models here.
from django.forms import ModelForm


class Posts(models.Model):
    title = models.CharField(max_length=30)
    upvotes = models.IntegerField(default=0)
    users_liked = models.ManyToManyField(User)
    content = models.TextField(default="")


class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content']
