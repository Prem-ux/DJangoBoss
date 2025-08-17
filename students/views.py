from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing student instances.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Uncomment the following methods to restrict permissions
    # def get_permissions(self):
    #     if self.action in ['create', 'update', 'partial_update', 'destroy']:
    #         return [IsAdminUser()]
    #     return super().get_permissions()
