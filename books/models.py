from django.db import models

# Create your models here.
class books(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    isbn = models.PositiveIntegerField(default=9999999999)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    