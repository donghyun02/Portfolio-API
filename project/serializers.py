from rest_framework import serializers

from project.models import Project, Slide


class SlideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slide()
        fields = ('id', 'project_name', 'image_url', 'description', 'order')

class ProjectSerializer(serializers.ModelSerializer):
    slides = SlideSerializer(many=True, read_only=True)

    class Meta:
        model = Project()
        fields = ('id', 'name', 'description', 'slides')