from django.urls import path
from .views import index, about, tos, contact_us

# Define URL patterns for the application
urlpatterns = [
    # URL pattern for the home page, calls the 'index' view function
    path('', index, name='index'),
    # URL pattern for the 'dev_team' page, calls the 'about' view function
    path('dev_team/', about, name='dev_team'),
    # URL pattern for the 'tos' (Terms of Service) page, calls the 'tos' view function
    path('tos/', tos, name='tos'),
    # URL pattern for the 'contact_us' page, calls the 'contact_us' view function
    path('contact_us/', contact_us, name='contact_us'),
]
