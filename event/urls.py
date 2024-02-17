from django.urls import path
from .views import EventPostList, event_details

urlpatterns = [
    path('event/<slug:slug>/', event_details, name='event'),
    path('eventlist/', EventPostList.as_view(), name='event_list'),
]

