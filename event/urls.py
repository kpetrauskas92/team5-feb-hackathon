from django.urls import path
from .views import EventPostList, event_details, create_event_post, update_event

urlpatterns = [
    path('event/<slug:slug>/', event_details, name='event'),
    path('eventlist/', EventPostList.as_view(), name='event_list'),
    path('create/', create_event_post, name='create_event_post'),
    path('event/update/<slug:slug>/', update_event, name='update_event'),
]
