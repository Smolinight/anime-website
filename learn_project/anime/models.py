from django.db import models

# Create your models here.
class Anime(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    rating = models.FloatField()