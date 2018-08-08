from django.shortcuts import render
# Create your views here.
from rest_framework import generics

from project.models import Project, Slide
from project.serializers import ProjectSerializer, SlideSerializer


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SlideListCreateAPIView(generics.ListCreateAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer
