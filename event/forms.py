from django import forms
from .models import EventPost

STATUS_CHOICES = (
    (0, "Private"),
    (1, "Public"),
)


class CustomClearableFileInput(forms.ClearableFileInput):
    template_name = 'custom_widgets/custom_clearable_file_input.html'


class EventPostForm(forms.ModelForm):
    """
    A Django form for creating and updating EventPost objects.

    This form includes all necessary fields for an EventPost and customizes the
    'status' field to use a dropdown select widget, ensuring the user must make
    a choice. The 'description' field is customized with a Textarea widget to
    improve user experience by providing a larger area for text input.

    """
    # Custom field definition for 'status' to ensure it uses a select widget
    # and is required.
    status = forms.ChoiceField(choices=STATUS_CHOICES,
                               widget=forms.Select(), required=True)

    class Meta:
        model = EventPost
        fields = ['event_name', 'status', 'description', 'category',
                  'location', 'image']
         # Custom widget settings for fields to enhance UI. For example,
         # increasing the size of the 'description' textarea.
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'image': CustomClearableFileInput()
        }
