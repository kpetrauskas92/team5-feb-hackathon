from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def index(request):
    """
    Render the index page.
    """
    return render(request, 'index.html')


def about(request):
    """
    Render the about (dev_team) page.
    """
    return render(request, 'dev_team.html')


def tos(request):
    """
    Render the Terms of Service (TOS) page.
    """
    return render(request, 'tos.html')


def contact_us(request):
    """
    Handle the contact us form submission and render the contact us page.
    """
    # If the request method is POST, process the form submission
    if request.method == 'POST':
        # Create a contact form instance with the POST data
        contact_form = ContactForm(request.POST)
        # Check if the form is valid
        if contact_form.is_valid():
            # Save the form data to the database
            contact_form.save()
            # Add a success message
            messages.add_message(request, messages.SUCCESS,
                                 'Magic received! We will respond as soon '
                                 'as possible!')
            # Redirect to the index page
            return redirect('index')
    else:
        # If the request method is not POST, create a new empty contact form
        contact_form = ContactForm()
    # Render the contact us page with the contact form
    return render(request, 'contact_us.html', {'contact_form': contact_form})