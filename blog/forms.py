from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'name': 'message',
        'class': 'form-control mb-10'
    }))

    class Meta:
        fields = ['content']
        model = Comment