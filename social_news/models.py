from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=30)
    upvotes = models.IntegerField(default=0)
    users_liked = models.ManyToManyField(User)
    content = models.TextField(default="")
    user = models.ForeignKey(User, related_name='user_posts', blank=True, null=True)


class Comment(models.Model):
    content = models.TextField(default="")
    post = models.ForeignKey('Posts', related_name='comments', blank=True, null=True)
    user = models.ForeignKey(User, related_name='user_comments', blank=True, null=True )
