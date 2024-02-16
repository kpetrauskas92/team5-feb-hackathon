from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    fields = ('user', 'phone_number', 'first_name', 'last_name', 'image',)
    list_display = ('user', 'phone_number', 'first_name', 'last_name',)
    search_fields = ('user',)
