from django import forms
from .models import StudentClass


class CreateClassForm(forms.ModelForm):
    class Meta:
        model = StudentClass
        fields = '__all__'