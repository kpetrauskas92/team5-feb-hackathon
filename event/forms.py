from django import forms
from .models import EventPost


STATUS_CHOICES = (
    (0, "Private"),
    (1, "Public"),
)


class EventPostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=STATUS_CHOICES,
                               widget=forms.Select(), required=True)

    class Meta:
        model = EventPost
        fields = ['event_name', 'status', 'description', 'category',
                  'location', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
