from django.urls import path
from .views import index, about, tos, contact_us

urlpatterns = [
    path('', index, name='index'),
    path('dev_team/', about, name='dev_team'),
    path('tos/', tos, name='tos'),
    path('contact_us/', contact_us, name='contact_us'),
]
