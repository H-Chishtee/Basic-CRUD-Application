from django.urls import path
from .views import StudentDetailView, StudentListCreateView


urlpatterns = [
    path("student/", StudentListCreateView.as_view(), name="student-list-create"),
    path("student/<int:pk>/", StudentDetailView.as_view(), name="student-list-create"),
]
