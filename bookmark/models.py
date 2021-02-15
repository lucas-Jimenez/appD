from django.db import models

# Create your models here.
class Bookmark(models.Model):
    url = models.CharField(max_length=100)