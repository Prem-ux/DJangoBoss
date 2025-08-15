from django.db import models

# Create your models here.
class Student(models.Model):
    # first_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # date_of_birth = models.DateField()
    # enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name