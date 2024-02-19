from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import EventPost, Like, CATEGORY
from django.http import HttpResponseForbidden, Http404, HttpResponse
from django.template.loader import render_to_string
from .forms import EventPostForm
from django.contrib import messages
from django.db.models import Count


class EventPostList(generic.ListView):
    """
    A ListView for displaying EventPosts filtered by category. Supports
    filtering by 'most_liked' to show posts ordered by likes count, or by
    other categories as specified in the request. Pagination is applied to
    limit the number of posts per page.
    """
    template_name = "event/eventlist.html"
    paginate_by = 6

    def get_queryset(self):
        # Retrieves the category from the URL query parameters.
        category_key = self.request.GET.get('category', '')

        if category_key == 'most_liked':
            # Filter to include only posts with at least one like and order by
            # likes count
            queryset = EventPost.objects.filter(status=1).annotate(
                likes_count=Count('likes')).filter(likes_count__gt=0).order_by(
                    '-likes_count')
        else:
            queryset = EventPost.objects.filter(status=1)
            if category_key:
                queryset = queryset.filter(category=category_key)
            # Apply default ordering or maintain existing logic for other
            # categories
            queryset = queryset.annotate(likes_count=Count('likes')).order_by(
                '-created_on')  # Assuming default order is by creation time

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_choices'] = CATEGORY
        return context


# Function views below handle specific actions like viewing details, liking a
# post, and CRUD operations for EventPosts.
def event_details(request, slug):
    """
    Renders the details page for an EventPost identified by a slug. Ensures only
    authenticated users can view private posts and checks if the current user
    has liked the post, also providing the total likes count.
    """
    if request.user.is_authenticated:
        eventpost = get_object_or_404(EventPost, slug=slug)

        if eventpost.status == 0 and (eventpost.author != request.user and
                                      not request.user.is_staff):
            raise Http404(
                "This idea is private and you do not have permission to view it.")
    else:
        # For unauthenticated users, only fetch public (published) event posts
        eventpost = get_object_or_404(EventPost, slug=slug, status=1)

    # Check if the current user has liked this post
    if request.user.is_authenticated:
        user_like = Like.objects.filter(user=request.user,
                                        event_post=eventpost).exists()
    else:
        user_like = False

    # Count the total likes for the event post
    total_likes = eventpost.likes.count()

    return render(request, 'event/event_details.html', {
        "eventpost": eventpost,
        "liked": user_like,
        "total_likes": total_likes,
    })


@login_required
def like_event_post(request, slug):
    """
    Toggles the current user's like status for an EventPost and updates the
    like count, providing appropriate feedback. Supports HTMX requests for
    dynamic UI updates.
    """
    # Retrieve the EventPost or return 404 if not found.
    event_post = get_object_or_404(EventPost, slug=slug)
    # Get the current user from the request.
    user = request.user
    # Try to get or create a Like object for the user and event post.
    liked, created = Like.objects.get_or_create(user=user,
                                                event_post=event_post)

    if not created:
        # If the Like object already existed, the user is "unliking" the post.
        liked.delete()
        liked = False
        messages.info(request, 'You have unliked the post.')
    else:
        # If the Like object was created, the user has liked the post.
        liked = True
        messages.success(request, 'You have liked the post.')

    # Count the total likes for the event post again after the operation.
    total_likes = event_post.likes.count()

    # Prepare the context for rendering the template.
    context = {
        'eventpost': event_post,
        'liked': liked,
        'total_likes': total_likes,
    }

    # Check if the request is an HTMX request for dynamic UI updates.
    if 'HX-Request' in request.headers:
        # Render only the like button part of the template for HTMX requests.
        html = render_to_string('likes/like_button.html', context=context,
                                request=request)
        return HttpResponse(html)

    # For non-HTMX requests, redirect to the event detail page.
    return redirect('event', slug=slug)


@login_required
def create_event_post(request):
    """
    Handles the creation of a new EventPost by an authenticated user, providing
    feedback and rendering the appropriate form or redirecting upon successful
    post creation.
    """
    # Check if the form was submitted.
    if request.method == 'POST':
        # Bind the POST data and files to the EventPostForm.
        form = EventPostForm(request.POST, request.FILES)
        if form.is_valid():
            # If the form is valid, save the new EventPost but do not commit
            # immediately.
            event_post = form.save(commit=False)
            # Set the author of the post to the current user.
            event_post.author = request.user
            # Now save the EventPost to the database.
            event_post.save()
            messages.success(request, 'Your idea has been created '
                                      'successfully!')
            # Redirect to the detail view of the newly created post.
            return redirect('event', slug=event_post.slug)
        else:
            # If the form is invalid, display an error message.
            messages.error(request, 'There was an error with your submission. '
                                    'Please check the form for errors.')
    else:
        # If the request is a GET, instantiate a blank form.
        form = EventPostForm(initial={'status': 0})

    # Render the form template.
    return render(request, 'event/create_event_post.html', {'form': form})


@login_required
def update_event(request, slug):
    """
    Allows an authenticated user to update their own EventPost, validating
    permissions, handling form submissions, and providing feedback.
    """
    # Retrieve the EventPost to be updated or return 404 if not found.
    eventpost = get_object_or_404(EventPost, slug=slug)

    # Ensure the request user is the author of the post.
    if request.user != eventpost.author:
        messages.error(request, 'You are not authorized to edit this idea.')
        return redirect('event', slug=slug)

    # Check if the form was submitted.
    if request.method == 'POST':
        # Bind the POST data and files to the EventPostForm with the instance
        # to be updated.
        form = EventPostForm(request.POST, request.FILES, instance=eventpost)
        if form.is_valid():
            # Save the updated EventPost.
            form.save()
            messages.success(request, 'Your idea has been updated '
                                      'successfully!')
            return redirect('event', slug=eventpost.slug)
        else:
            # If the form is invalid, display an error message.
            messages.error(request, 'There was an error updating your idea. '
                                    'Please check the form for errors.')
    else:
        # For a GET request, instantiate the form with the EventPost instance
        # to be updated.
        form = EventPostForm(instance=eventpost)

    # Render the update form template.
    return render(request, 'event/edit_event_post.html', {
        'form': form, 'eventpost': eventpost})


@login_required
def delete_event(request, slug):
    """
    Allows an authenticated user to delete their own EventPost, ensuring proper
    authorization, and providing appropriate feedback upon deletion or access
    denial.
    """
    # Retrieve the EventPost to be deleted or return 404 if not found.
    eventpost = get_object_or_404(EventPost, slug=slug)

    # Ensure the request user is the author of the post.
    if eventpost.author != request.user:
        messages.error(request, 'You are not authorized to delete this idea.')
        return HttpResponseForbidden()

    # Check if the deletion was confirmed through a POST request.
    if request.method == 'POST':
        # Delete the EventPost.
        eventpost.delete()
        messages.success(request, 'The idea has been deleted successfully.')
        return redirect('event_list')

    # For a GET request, render the confirmation page for deleting the EventPost.
    return render(request, 'event/confirm_delete_event.html', {
        'eventpost': eventpost})
