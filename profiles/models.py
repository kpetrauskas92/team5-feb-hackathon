from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from event.models import EventPost
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator
import decimal


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.user.username


class UserDate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    post = models.ForeignKey(EventPost, on_delete=models.CASCADE,
                             blank=True, null=True)
    date = models.DateField()
    title = models.CharField(max_length=255, blank=True, null=True)
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(decimal.Decimal('0.01'))],
        blank=True,
        null=True,
        help_text="Budget in euros (€)"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'date', 'title')
        ordering = ['date']

    def __str__(self):
        return f"{self.title or 'Event'} on {self.date} by {self.user.username}"
