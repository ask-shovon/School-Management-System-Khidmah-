from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# school info model
class SchoolInfo(models.Model):
    school_name = models.CharField(max_length=150)
    school_phone = models.CharField(max_length=150)
    school_address = models.TextField(blank=True, null=True)
    school_photo = models.ImageField()

    # one to one relation with User model (User model is the main authority of a school
    school_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.school_name


# student class model
class StudentClass(models.Model):
    class_name = models.CharField(max_length=50, unique=True)
    class_no = models.IntegerField(unique=True)

    def __str__(self):
        return self.class_name


# Subject model
class Subject(models.Model):
    subject_name = models.CharField(max_length=50, unique=True)
    subject_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name 