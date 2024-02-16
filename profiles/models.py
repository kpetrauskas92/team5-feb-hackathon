from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    phone_number = models.CharField(max_length=20, null=True, blank=True),
    first_name = models.CharField(max_length=100, null=True, blank=True),
    last_name = models.CharField(max_length=100, null=True, blank=True),
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.user.username
