from django.db import models


# Create your models here.
class Slide(models.Model):
    project = models.ForeignKey("Project", related_name="slides", on_delete=models.CASCADE, default="")
    image = models.ImageField(blank=True, default="")
    description = models.TextField()
    order = models.PositiveIntegerField()

    def __str__(self):
        return '{}: {}'.format(self.project.name, self.order)

    @property
    def project_name(self):
        return self.project.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    url = models.TextField(default="", blank=True)

    def __str__(self):
        return self.name
