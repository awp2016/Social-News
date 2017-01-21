from django import forms
from django.contrib.auth.models import User

from social_news.models import Comment, Posts


class PostForm(forms.Form):
    title = forms.CharField(label='Post Name', max_length=40)
    upvotes = forms.IntegerField(label='Post Upvotes')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'post']


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content']
