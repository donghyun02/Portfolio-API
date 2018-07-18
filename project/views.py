from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response

from project.models import Project
from project.serializers import ProjectSerializer


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
