from django.db import models

# Create your models here.
class Slide(models.Model):
    image_url = models.TextField()
    description = models.TextField()
    order = models.PositiveIntegerField()

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slides = models.ManyToManyField(Slide)
