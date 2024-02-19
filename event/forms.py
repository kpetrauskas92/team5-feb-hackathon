from django import forms
from .models import EventPost

STATUS_CHOICES = (
    (0, "Private"),
    (1, "Public"),
)


class CustomClearableFileInput(forms.ClearableFileInput):
    template_name = 'custom_widgets/custom_clearable_file_input.html'


class EventPostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=STATUS_CHOICES,
                               widget=forms.Select(), required=True)

    class Meta:
        model = EventPost
        fields = ['event_name', 'status', 'description', 'category',
                  'location', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'image': CustomClearableFileInput()
        }
