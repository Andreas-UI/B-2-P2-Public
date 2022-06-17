from django import forms
from django.contrib.auth.models import User
from .models import Community

class CommunityForm(forms.ModelForm):
    community_name = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'class': 'text-control',
                'id': 'community_name', 
                "aria-describedby":"community_nameHelp",
                "autocomplete": "off",
                "oninput": "this.className = ''""",
            }
        ))

    description = forms.CharField(
        max_length=380, 
        required=True, 
        widget=forms.Textarea(
            attrs={
                'class': 'text-control',
                'id': 'description', 
                "aria-describedby":"descriptionHelp",
                "autocomplete": "off",
                "oninput": "this.className = ''""",
                "rows": "4", 
            }
        ))

    class Meta:
        model = Community
        fields = ['community_name', 'description', 'category']

class CommunityDescriptionUpdateForm(forms.ModelForm):
    description = forms.CharField(
        required=True,
        max_length=195,
        widget=forms.Textarea( 
            attrs={
                "type": "text", 
                "id": "description",
                "rows": "3"
                }
            )
        )

    class Meta:
        model = Community
        fields = ["description"]

class CommunityImageUpdateForm(forms.ModelForm):
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
        model = Community
        fields = ["image"]

