from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)  # Assuming a reasonable max length for phone numbers

    def __str__(self):
        return f"{self.user.username}'s UserDetails"
