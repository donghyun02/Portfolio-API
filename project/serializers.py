from rest_framework import serializers

from project.models import Project, Slide


class SlideSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Slide
        fields = ('id', 'project_name', 'image', 'description', 'order')

class ProjectSerializer(serializers.ModelSerializer):
    slides = SlideSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'slides')
