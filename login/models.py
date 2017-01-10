from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.forms.models import ModelForm


# Create your models here.
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
