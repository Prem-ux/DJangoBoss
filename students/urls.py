from django.urls import path
from . import views

urlpatterns = [
    path("", views.ping, name="students_ping"),
    # path("students/", views.StudentListView.as_view(), name="student_list"),
    # path("students/<int:pk>/", views.StudentDetailView.as_view(), name="student_detail"),
    # path("students/create/", views.StudentCreateView.as_view(), name="student_create"),
    # path("students/<int:pk>/update/", views.StudentUpdateView.as_view(), name="student_update"),
    # path("students/<int:pk>/delete/", views.StudentDeleteView.as_view(), name="student_delete"),
]
