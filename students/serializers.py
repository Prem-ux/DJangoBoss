from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"  # Include all fields from the Student model

    # def validate_email(self, value):
    #     """
    #     Check that the email is valid.
    #     """
    #     if not value or "@" not in value:
    #         raise serializers.ValidationError("Invalid email address.")
    #     return value

    # def validate_name(self, value):
    #     """
    #     Check that the name is not empty.
    #     """
    #     if not value.strip():
    #         raise serializers.ValidationError("Name cannot be empty.")
    #     return value
