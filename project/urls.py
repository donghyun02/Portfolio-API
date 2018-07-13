from django.urls import path

from project import views

urlpatterns = [
    path('projects/', views.ProjectListCreateAPIView.as_view()),
]