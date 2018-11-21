from django.contrib import admin
from .models import *


# admin panel modify
class SchoolInfoAdmin(admin.ModelAdmin):
    list_display = (
        'school_name',
        'school_phone',
        'school_address',
        'school_photo',
        'school_user',
    )


class StudentClassAdmin(admin.ModelAdmin):
    list_display = (
        'class_name',
        'class_no',
    )


class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'subject_name',
        'subject_class',
    )


# Register your models here.
admin.site.register(SchoolInfo, SchoolInfoAdmin)
admin.site.register(StudentClass, StudentClassAdmin)
admin.site.register(Subject, SubjectAdmin)
