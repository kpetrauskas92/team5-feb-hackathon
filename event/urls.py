from django.urls import path
from .views import EventPostList

urlpatterns = [
    path('event/<slug:slug>/', event_details, name='event'),
    path('', views.EventPostList.as_view(), name='event_list'),
]