from django.urls import path
from .views import profile, create_event_post_from_profile, update_profile

urlpatterns = [
    path('', profile, name='profile'),  # Assuming this is the main profile page
    path('create/', create_event_post_from_profile, name='create_event_post_from_profile'),  # URL for creating a draft post
    path('update_profile/', update_profile, name='update_profile'),
]
