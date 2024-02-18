from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from event.models import EventPost
from event.forms import EventPostForm
from .forms import UserProfileForm, UserDateForm
from .models import UserProfile, UserDate
import json
from django.core.serializers.json import DjangoJSONEncoder


@login_required
def profile(request):
    # Query for the user's own posts
    user_posts = EventPost.objects.filter(
        author=request.user,
        status=1).order_by('-created_on')

    suggested_posts = EventPost.objects.exclude(
        author=request.user).filter(status=1).order_by('-created_on')

    # Query for the user's dates
    user_dates = UserDate.objects.filter(user=request.user).order_by('date')

    # Preparing user_dates for FullCalendar
    user_dates_events = [
        {
            'title': user_date.title or "No Title",
            'start': user_date.date.strftime("%Y-%m-%d"),
            'allDay': True
        }
        for user_date in user_dates
    ]

    user_dates_json = json.dumps(user_dates_events, cls=DjangoJSONEncoder)

    # Calculate total budget
    total_budget = user_dates.aggregate(Sum('budget'))['budget__sum'] or 0

    return render(request, 'profiles/profile.html', {
        'user_posts': user_posts,
        'suggested_posts': suggested_posts,
        'user_dates': user_dates,
        'user_dates_json': user_dates_json,
        'total_budget': total_budget,
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
    """
    Display and process the profile form.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/update_profile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_user_date(request):
    initial_data = {}
    post_id = request.GET.get('post_id')

    if post_id:
        post = get_object_or_404(EventPost, pk=post_id)
        initial_data['title'] = post.event_name

    if request.method == 'POST':
        form = UserDateForm(request.POST)
        if form.is_valid():
            user_date = form.save(commit=False)
            user_date.user = request.user
            if post_id:
                user_date.post = post
            user_date.save()
            return redirect('profile')
    else:
        form = UserDateForm(initial=initial_data)

    return render(request, 'profiles/add_to_calendar.html', {'form': form})


@login_required
def delete_user_date(request, date_id):
    user_date = get_object_or_404(UserDate, id=date_id, user=request.user)

    if request.method == 'POST':
        user_date.delete()
        return redirect('profile')

    return render(request, 'profiles/confirm_delete_user_date.html', {
        'user_date': user_date
    })
