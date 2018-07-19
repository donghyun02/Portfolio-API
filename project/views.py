from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response

from project.models import Project, Slide
from project.serializers import ProjectSerializer, SlideSerializer


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SlideListCreateAPIView(generics.ListCreateAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer
    parser_classes = (MultiPartParser, )

    def create(self, request, *args, **kwargs):
        print(request.data['image'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
