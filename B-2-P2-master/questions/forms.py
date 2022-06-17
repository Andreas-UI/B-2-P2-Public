from django import forms
from django.contrib.auth.models import User
from pawn.fields import PawnFormField
from .models import Question, QuestionComment, ReplyComment
from taggit.forms import TagWidget

class QuestionForm(forms.ModelForm):

    title = forms.CharField(
        max_length=280, 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'class': 'text-control',
                'id': 'title', 
                "aria-describedby":"titleHelp",
                "autocomplete": "off",
                "oninput": "this.className = ''""",
            }
        ))

    summary = forms.CharField(
        max_length=380, 
        required=True, 
        widget=forms.Textarea(
            attrs={
                'class': 'text-control',
                'id': 'summary', 
                "aria-describedby":"summaryHelp",
                "autocomplete": "off",
                "oninput": "this.className = ''""",
            }
        ))

    class Meta:
        model = Question
        fields = ['title', 'tags', 'summary', 'category']

class QuestionUpdateForm(forms.ModelForm):
    summary = forms.CharField(
        max_length=380, 
        required=True, 
        widget=forms.Textarea(
            attrs={
                'class': 'text-control',
                'id': 'summary', 
                "aria-describedby":"summaryHelp",
                "autocomplete": "off",
                "rows": "3",
                "oninput": "this.className = ''""",
            }
        ))

    class Meta:
        model = Question
        fields = ['summary']

class QuestionCommentForm(forms.ModelForm):
    comment = PawnFormField()

    class Meta:
        model = QuestionComment
        fields = ['comment']
        widgets= {
            'tags' : TagWidget(attrs={'class':'text-control'}),
        }

class ReplyCommentForm(forms.ModelForm):
    reply = forms.CharField(
        max_length=380, 
        required=True, 
        widget=forms.Textarea(
            attrs={
                'class': 'text-control',
                'id': 'reply', 
                "aria-describedby":"replyHelp",
                "autocomplete": "off",
                "rows": "3",
                "oninput": "this.className = ''""",
            }
        ))

    class Meta:
        model = ReplyComment
        fields = ['reply']

class QuestionCommentEditForm(forms.ModelForm):
    comment = PawnFormField()

    class Meta:
        model = QuestionComment
        fields = ['comment']
        