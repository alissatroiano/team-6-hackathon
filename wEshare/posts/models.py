from datetime import datetime
from django.conf import settings
import uuid
from django.db import models
from django.utils import timezone
now = timezone.now
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    """ An instance of a post """
    description = models.CharField(max_length=1000,blank=True, primary_key=True)
    unique_id = models.UUIDField(default=uuid.uuid4, max_length=100, unique=True) # removed primary_key=True
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    # publishing_date = models.DateTimeField(default = timezone.now)

    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'
        ordering = ['-date_published']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description
