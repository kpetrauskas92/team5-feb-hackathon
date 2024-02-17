from django.urls import path
from .views import event_details

urlpatterns = [
    path('event/<slug:slug>/', event_details, name='event'),

]