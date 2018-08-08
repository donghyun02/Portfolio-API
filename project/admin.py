from django.contrib import admin

# Register your models here.
from project.models import Project, Slide

admin.site.register(Slide)
admin.site.register(Project)
