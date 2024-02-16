from django import forms
from .models import Post
# , User 
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
    username = forms.CharField(
        max_length=65,
        widget=forms.TextInput(attrs={'class': 'form-control custom-form-input'})
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control custom-form-input'})
    )


    
# class RegisterForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields = ['username','email','password1','password2'] 
class RegisterForm(UserCreationForm):
    #email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # email = forms.EmailField()
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Your e-mail", 'class': "form-control custom-form-input"})
    )
    password1 = forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','type':'password', 'name': 'password','placeholder':'Password'}),
    label='')
    password2 = forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','type':'password', 'name': 'password','placeholder':'Password'}),
    label='')
    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control custom-form-input', "placeholder": "Nombre de usuario",}),
            #'password1': forms.PasswordInput(attrs={'class': 'password1'}),
            
        }

# class AvatarFileUploadInput(forms.ClearableFileInput):
#     template_name = 'avatar.html'

# class UpdateProfileForm(forms.ModelForm):
#     class Meta:
#         model = User 
#         fields = ['name', 'username', 'avatar']
#         widgets = {"avatar": AvatarFileUploadInput}
        
        
class Write(forms.Form):
    title = forms.CharField(label="Titulo", max_length=100)
    