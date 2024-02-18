from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from event.models import EventPost
from event.forms import EventPostForm
from .forms import UserProfileForm
from .models import UserProfile


@login_required
def profile(request):
    # Query for the user's own posts
    user_posts = EventPost.objects.filter(author=request.user, status=1).order_by('-created_on')  # Assuming status=1 means published

    # Query for suggested posts (example: posts not authored by the user and are published)
    suggested_posts = EventPost.objects.exclude(author=request.user).filter(status=1).order_by('-created_on')

    return render(request, 'profiles/profile.html', {
        'user_posts': user_posts,
        'suggested_posts': suggested_posts
    })


@login_required
def create_event_post_from_profile(request):
    if request.method == 'POST':
        form = EventPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.status = 0
            new_post.save()
            return redirect('profile')
    else:
        form = EventPostForm(initial={'status': 0})
    return render(request, 'event/create_event_post.html', {'form': form})


@login_required
def update_profile(request):
    """ Display the profile from. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/update_profile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
