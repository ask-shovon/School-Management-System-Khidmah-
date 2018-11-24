from django import forms
from .models import StudentClass


class CreateClassForm(forms.ModelForm):
    class Meta:
        model = StudentClass
        fields = '__all__'

        widgets = {
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'class_no': forms.NumberInput(attrs={'class': 'form-control'})
        }