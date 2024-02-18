from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'dev_team.html')


def tos(request):
    return render(request, 'tos.html')


def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS,
                                    'Magic received! We will respond as soon '
                                    'as possible!')
            return redirect('index')
    else:
        contact_form = ContactForm()
    return render(request, 'contact_us.html', {'contact_form': contact_form})