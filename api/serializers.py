from rest_framework import serializers
from academic.models import StudentClass


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = '__all__'
