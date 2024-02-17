from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import EventPost

# Create your views here.

class EventPostList(generic.ListView):
    """
    A view that displays a list of published EventPosts using
    Django's ListView.
    """
    queryset = EventPost.objects.filter(status=1)
    template_name = "event/eventlist.html"
    paginate_by = 4


def event_details(request, slug):
    queryset = EventPost.objects.filter(status=1)
    eventpost = get_object_or_404(queryset, slug=slug)
    #comments = eventpost.comments.all().order_by("-created_on")
    #comment_count = eventpost.comments.filter(approved=True).count()
    #comment_form = CommentForm()
    return render(request, 'event_details.html',
        {
            "eventpost": eventpost,
            #"comments": comments,
            #"comment_count": comment_count,
            #"comment_form": comment_form,
        },
    )