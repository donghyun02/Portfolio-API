from django.db import models

# Create your models here.
class Slide(models.Model):
    project_name = models.CharField(max_length=50, default="")
    image = models.ImageField(blank=True, default="")
    description = models.TextField()
    order = models.PositiveIntegerField()

    def __str__(self):
        return '{}: {}'.format(self.project_name, self.order)

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slides = models.ManyToManyField(Slide, blank=True)

    def __str__(self):
        return self.name
