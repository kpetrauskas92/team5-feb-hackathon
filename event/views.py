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
    A view that displays a list of published EventPosts using
    Django's ListView.
    """
    template_name = "event/eventlist.html"
    paginate_by = 4

    def get_queryset(self):
        category_key = self.request.GET.get('category', '')

        if category_key == 'most_liked':
            # Filter to include only posts with at least one like and order by likes count
            queryset = EventPost.objects.filter(status=1).annotate(likes_count=Count('likes')).filter(likes_count__gt=0).order_by('-likes_count')
        else:
            queryset = EventPost.objects.filter(status=1)
            if category_key:
                queryset = queryset.filter(category=category_key)
            # Apply default ordering or maintain existing logic for other categories
            queryset = queryset.annotate(likes_count=Count('likes')).order_by('-created_on')  # Assuming default order is by creation time

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_choices'] = CATEGORY
        return context


def event_details(request, slug):
    if request.user.is_authenticated:
        eventpost = get_object_or_404(EventPost, slug=slug)

        if eventpost.status == 0 and (eventpost.author != request.user and not request.user.is_staff):
            raise Http404(
                "This event post is private and you do not have permission to view it.")
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
    event_post = get_object_or_404(EventPost, slug=slug)
    user = request.user
    liked, created = Like.objects.get_or_create(user=user, event_post=event_post)

    if not created:
        liked.delete()
        liked = False
    else:
        liked = True

    total_likes = event_post.likes.count()

    context = {
        'eventpost': event_post,
        'liked': Like.objects.filter(user=request.user,
                                     event_post=event_post).exists(),
        'total_likes': total_likes,
    }

    if 'HX-Request' in request.headers:
        html = render_to_string('likes/like_button.html', context=context, request=request)
        return HttpResponse(html)
    return redirect('event', slug=slug)


@login_required
def create_event_post(request):
    if request.method == 'POST':
        form = EventPostForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request,
                             'Your event post has been created successfully!')
            event_post = form.save(commit=False)
            event_post.author = request.user
            event_post.save()
            return redirect('event', slug=event_post.slug)
    else:
        form = EventPostForm(initial={'status': 0})
    return render(request, 'event/create_event_post.html', {'form': form})


@login_required
def update_event(request, slug):
    eventpost = get_object_or_404(EventPost, slug=slug)

    if request.user != eventpost.author:
        messages.error(request, 'You are not authorized to edit this event.')
        return redirect('event', slug=slug)

    if request.method == 'POST':
        form = EventPostForm(request.POST, request.FILES, instance=eventpost)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your event post has been updated successfully!')
            return redirect('event', slug=eventpost.slug)
    else:
        form = EventPostForm(instance=eventpost)

    return render(request, 'event/edit_event_post.html',
                  {'form': form,
                   'eventpost': eventpost})


@login_required
def delete_event(request, slug):
    eventpost = get_object_or_404(EventPost, slug=slug)

    if eventpost.author != request.user:
        messages.error(request, 'You are not authorized to delete this event.')
        return HttpResponseForbidden()

    if request.method == 'POST':
        eventpost.delete()
        messages.success(request,
                         'The event post has been deleted successfully.')
        return redirect('event_list')

    # Render the confirmation page for GET requests
    return render(request,
                  'event/confirm_delete_event.html', {'eventpost': eventpost})
