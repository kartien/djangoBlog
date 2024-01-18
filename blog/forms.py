from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control custom-form-input'}),
            'image': forms.FileInput(attrs={'class': 'image-fluid'}),
            'content': forms.Textarea(attrs={'class': 'form-control custom-form-input'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control custom-form-input'}),
            'email': forms.TextInput(attrs={'class': 'form-control custom-form-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control custom-form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control custom-form-input'})
        }
class Write(forms.Form):
    title = forms.CharField(label="Titulo", max_length=100)
    