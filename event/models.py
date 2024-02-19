from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))

CATEGORY = (
    ("food_and_drink", "Food & Drink"),
    ("art_and_culture", "Art & Culture"),
    ("single_and_ready_to_mingle", "Single & ready to mingle"),
    ("adventure", "Adventure"),
)


class EventPost(models.Model):
    """
    A model representing an event post in the application.

    Methods:
        save: Overrides the save method to automatically generate a unique
        slug if it is not provided.
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="event_posts",
        on_delete=models.CASCADE
    )
    event_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    category = models.CharField(
        max_length=50, choices=CATEGORY, default="adventure"
    )
    location = models.CharField(max_length=300, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        """
        Overrides the save method to ensure a unique slug is generated for each
        event post if it is not explicitly set.
        """
        if not self.slug:
            original_slug = slugify(self.event_name)
            unique_slug = original_slug
            num = 1
            while EventPost.objects.filter(slug=unique_slug).exists():
                unique_slug = '{}-{}'.format(original_slug, num)
                num += 1
            self.slug = unique_slug
        super(EventPost, self).save(*args, **kwargs)

    class Meta:
        # Orders posts by creation date, with the most recent first.
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns a string representation of the EventPost, including the event
        name and the author's username.
        """
        return f'{self.event_name} | added by {self.author.username}'


class Like(models.Model):
    """
    Model representing a user's like on an event post. Tracks who liked what
    and when.

    Attributes:
        user: Reference to the user who liked an event post.
        event_post: Reference to the liked event post.
        created_at: Timestamp of when the like was made.

    Constraints:
        - A user can like a specific event post only once.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='liked_posts',
        on_delete=models.CASCADE
    )
    event_post = models.ForeignKey(
        EventPost,
        related_name='likes',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevents duplicate likes for the same post by the same user.
        unique_together = ('user', 'event_post')
