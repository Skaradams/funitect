from django.db import models
from django.contrib.auth.models import User

__all__ = ('Item',)


class Item(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

