from django.contrib import admin
from .models import *


# admin panel modifier
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = (
        'student_name',
        'student_gender',
        'student_photo',
        'student_class',
        'student_roll',
        'student_section',
    )


# Register your models here.
admin.site.register(StudentInfo, StudentInfoAdmin)