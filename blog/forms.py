from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class Write(forms.Form):
    title = forms.CharField(label="Titulo", max_length=100)
    