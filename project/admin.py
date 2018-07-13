from django.contrib import admin

# Register your models here.
from project.models import Slide, Project

admin.site.register(Slide)
admin.site.register(Project)