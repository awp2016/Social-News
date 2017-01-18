from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

#TODO: Link with post FK

class Comment (models.Model):
    content = models.TextField (default = "")

class CommentForm (ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
