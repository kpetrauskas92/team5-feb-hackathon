from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import EventPost, CATEGORY
from django.http import HttpResponseForbidden
from .forms import EventPostForm
from django.contrib import messages
from django.db.models import Count


class EventPostList(generic.ListView):
    """
    A view that displays a list of published EventPosts using
    Django's ListView.
    """
    queryset = EventPost.objects.filter(status=1)
    template_name = "event/eventlist.html"
    paginate_by = 4

    def get_queryset(self):
        category_key = self.request.GET.get('category', '')
        queryset = EventPost.objects.annotate(likes_count=Count('likes')).order_by('-likes_count')
        if category_key:
            queryset = queryset.filter(category=category_key)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_choices'] = CATEGORY
        return context


def event_details(request, slug):
    queryset = EventPost.objects.filter(status=1)
    eventpost = get_object_or_404(queryset, slug=slug)

    return render(request, 'event/event_details.html', {
        "eventpost": eventpost,
    })


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
