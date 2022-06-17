from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileAboutUpdateForm(forms.ModelForm):
    about = forms.CharField(
        required=True,
        max_length=195,
        widget=forms.Textarea( 
            attrs={
                "type": "text", 
                "placeholder": "Write something about yourself", 
                "class": "profile-input", 
                "id": "about",
                "rows": "3"
                }
            )
        )

    class Meta:
        model = Profile
        fields = ["about"]

class ProfileImageUpdateForm(forms.ModelForm):
    image = forms.ImageField(
        required=True, 
        widget=forms.FileInput(
            attrs={
                "type": "file",  
                "class": "update-image-input collapse", 
                "id": "image", 
                "accept": "image/*"
            }
        )
    )

    class Meta:
        model = Profile
        fields = ["image"]

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput( 
            attrs={
                "type": "text", 
                "class": "form-control", 
                "id": "username"
                }
            )
        )

    class Meta:
        model = User
        fields = ['username']