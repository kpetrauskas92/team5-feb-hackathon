from django import forms
from .models import UserProfile, UserDate


class CustomClearableFileInput(forms.ClearableFileInput):
    template_name = 'custom_widgets/custom_clearable_file_input.html'


class UserProfileForm(forms.ModelForm):
    field_order = ['first_name', 'last_name', 'sex']

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'sex', 'image']
        widgets = {
            'image': CustomClearableFileInput(),
        }
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'sex': 'Sex',
            'image': 'Upload Image',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field in placeholders:
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]
                if field == 'image':
                    pass
                elif field == 'sex':
                    self.fields[field].empty_label = "Select Sex"
                else:
                    self.fields[field].widget.attrs['class'] = 'your-class-for-hiding-labels'



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

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        custom_classes = 'border-black rounded-0 profile-form-input'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = custom_classes
