from django import forms


class PostForm(forms.Form):
    title = forms.CharField(label='Post Name', max_length=40)
    upvotes = forms.IntegerField(label='Post Upvotes')
