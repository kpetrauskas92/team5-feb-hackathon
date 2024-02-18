from django import forms
from .models import EventPost


class EventPostForm(forms.ModelForm):
    class Meta:
        model = EventPost
        fields = ['event_name', 'description', 'category',
                  'location', 'image', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'status': forms.HiddenInput(),
        }
