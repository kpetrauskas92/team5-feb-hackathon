from django import forms
from .models import EventPost, Comment


class EventPostForm(forms.ModelForm):
    class Meta:
        model = EventPost
        fields = ['event_name', 'description', 'category',
                  'location', 'image', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'status': forms.HiddenInput(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'style': 'height: 75px;'}),
        }
