from django import forms
from .models import ContactUs


class ContactForm(forms.ModelForm):
    """
    Form class for creating a contact form with 'name', 'email', and
    'message' fields.
    """
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message',)