from rest_framework import serializers

class SlideSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'image_url', 'description', 'order')

class ProjectSerializer(serializers.ModelSerializer):
    slides = SlideSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'name', 'description', 'slides')