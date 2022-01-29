from django.db import models
import uuid
import os
from django.utils import timezone
from datetime import datetime
now = timezone.now
from django.contrib.auth.models import User
from django.conf import settings

def images_path():
    return os.path.join(settings.MEDIAFILES_LOCATION, 'media')

class Post(models.Model):
    """ A unique post for users to share """
    user = models.ForeignKey(User, related_name='calendars', on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    description = models.TextField()
    unique_id = models.UUIDField(default=uuid.uuid4, max_length=100, unique=True, primary_key=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    deleted_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.name
