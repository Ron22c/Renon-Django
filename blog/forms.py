from django import forms
from blog import models

class PostForm(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = ('author', 'title', 'content')
        widgets = {
            'title': forms.TextInput(attrs = {'class': 'textinputclass'}),
            'content': forms.Textarea(attrs = {'class': 'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = models.Comment
        fields = ('author', 'content')
        widgets = {
            'author': forms.TextInput(attrs = {'class': 'textinputclass'}),
            'content': forms.Textarea(attrs = {'class': 'editable medium-editor-textarea postcontent'})
        }
