from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

CATEGORY = (("fodd_and_drink", "Food & Drink"),
              ("art_and_culture", "Art & Culture"),
              ("single_and_ready_to_mingle", "Single & ready to mingle"),
              ("adventure", "Adventure"),
              )

class EventPost(models.Model):
    """

    """
    author = models.ForeignKey(
        User, related_name="event_posts", on_delete=models.CASCADE
    )
    event_name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    desciption = models.TextField(max_length=10000, null=False, blank=False)
    category = models.CharField(max_length=50, choices=CATEGORY,
                                 default="Adventure", blank=False)
    location = models.CharField(max_length=300, null=False, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=100, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.event_name.replace(" ", "-")
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f'{self.event_name} | added by {self.author}'

