from django import forms
from .models import ContactUs


class ContactForm(forms.ModelForm):
    """
    Form class for creating a contact form with 'name', 'email', and
    'message' fields.
    """
    # Meta class to define metadata options for the form
    class Meta:
        # Specifies the model to be used for the form
        model = ContactUs
        # Specifies the fields from the model to include in the form
        fields = ('name', 'email', 'message',)