from django.urls import path
from .views import (EventPostList,
                    event_details,
                    create_event_post,
                    update_event,
                    delete_event,
                    like_event_post)

# This section of code is responsible for defining the URL patterns for an
# event management application built with Django.
# Each URL pattern is associated with a specific view that handles
# the request and response flow for different parts of the application
# related to events.

urlpatterns = [
    # URL pattern for viewing the details of a specific event.
    # The 'slug' is used as a unique identifier for each event to make URLs
    # more readable and SEO-friendly.
    path('event/<slug:slug>/', event_details, name='event'),

    # URL pattern for listing all event posts. It uses a class-based view
    # (EventPostList) to render the list.
    path('eventlist/', EventPostList.as_view(), name='event_list'),

    # URL pattern for creating a new event post. It directs to a view that
    # handles the form submission for new event creation.
    path('create/', create_event_post, name='create_event_post'),

    # URL pattern for updating an existing event post. Similar to the detail
    # view, it uses a 'slug' to identify the specific event to be updated.
    path('event/update/<slug:slug>/', update_event, name='update_event'),

    # URL pattern for deleting an existing event post. It also uses a 'slug'
    # to identify the specific event to be deleted.
    path('event/delete/<slug:slug>/', delete_event, name='delete_event'),

    # URL pattern for liking an event post. This allows users to like or
    # interact with an event post, identified by its 'slug'.
    path('like/<slug:slug>/', like_event_post, name='like_event_post'),
]

