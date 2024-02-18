from django.db import models

# Create your models here.
class ContactUs(models.Model):
    """
    Model for handling contact form.

    Fields:
    - name: Sender's name.
    - email: Sender's email address.
    - message: Contact message content.
    - read: Boolean indicating if the message has been read, defaulting to
    False.

    The string representation includes the sender's name.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"