from django.urls import path
from .views import preview_event_details

urlpatterns = [
    path('preview-event/', preview_event_details, name='preview_event'),
]