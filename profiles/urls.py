from django.urls import path
from .views import (profile,
                    create_event_post_from_profile,
                    update_profile,
                    add_user_date,
                    delete_user_date)

urlpatterns = [
    path('', profile,
         name='profile'),
    path('create/', create_event_post_from_profile,
         name='create_event_post_from_profile'),
    path('update_profile/', update_profile,
         name='update_profile'),
    path('add_date/', add_user_date,
         name='add_user_date'),
    path('delete_date/<int:date_id>/', delete_user_date,
         name='delete_user_date'),
]
