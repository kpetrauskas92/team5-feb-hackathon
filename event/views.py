from django.shortcuts import render

# Create your views here.

def preview_event_details(request):
    # Dummy data to simulate what would come from an Event model
    event_context = {
        'title': 'Sample Event',
        'date': '2024-02-16',
        'location': 'Sample Location',
        'description': 'This is a sample description for a preview event.',
    }
    return render(request, 'event/event_details.html', {'event': event_context})

#def event_details(request, slug):
    #queryset = EventPost.objects.filter(status=1)
    #eventpost = get_object_or_404(queryset, slug=slug)
    #comments = eventpost.comments.all().order_by("-created_on")
    #comment_count = eventpost.comments.filter(approved=True).count()
    #comment_form = CommentForm()
 #   return render(request, 'event_details.html')

