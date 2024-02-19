from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import EventPost

# Register your models here.

@admin.register(EventPost)
class EventPostAdmin(ModelAdmin):
    """
    Admin interface for managing EventPost entries.
    Includes capabilities for listing, searching, and filtering Event Posts.
    """

    list_display = ('event_name', 'author', 'status', 'category',)
    search_fields = ['event_name', 'category']
    list_filter = ('status', 'category',)
    prepopulated_fields = {'slug': ('event_name',)}
