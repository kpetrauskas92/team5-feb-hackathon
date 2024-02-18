from django import forms
from .models import UserProfile, UserDate


class UserProfileForm(forms.ModelForm):

    field_order = ['first_name', 'last_name', 'phone_number']

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'image':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False


class UserDateForm(forms.ModelForm):
    class Meta:
        model = UserDate
        fields = ['date', 'title', 'budget']
        help_texts = {
            'budget': 'Enter your budget (€).',
        }
        labels = {
            'budget': 'Cost (€)',
        }
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date',
                       'class': 'form-input px-4 py-3 rounded-full'}),
            'title': forms.TextInput(
                attrs={'class': 'form-input px-4 py-3 rounded-full'}),
            'budget': forms.NumberInput(
                attrs={'class': 'form-input px-4 py-3 rounded-full'}),
        }
