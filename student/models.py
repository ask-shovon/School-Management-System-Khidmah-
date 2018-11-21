from django.db import models
from academic.models import StudentClass


# Create your models here.
class StudentInfo(models.Model):
    student_name = models.CharField(max_length=150)
    choice_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    student_gender = models.CharField(max_length=30, choices=choice_gender)
    student_photo = models.ImageField()
    student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    student_roll = models.IntegerField()
    student_section = models.CharField(max_length=30)

    def __str__(self):
        return self.student_name
