from django.shortcuts import render, redirect

from .models import StudentClass
from .forms import CreateClassForm


# Create your views here.
def dashboard(request):
    return render(request, 'academic/dashboard.html')


# create class
def create_class(request):
    if request.method == 'POST':
        forms = CreateClassForm(request.POST)
        if forms.is_valid():
            forms.save()
            context = {
                'msg': 'success',
                'forms': forms,
            }

            return render(request, 'academic/create_class.html', context)
        else:
            forms = CreateClassForm()
            context = {
                'msg': 'error',
                'forms': forms,
            }
            return render(request, 'academic/create_class.html', context)
    forms = CreateClassForm()
    context = {
        'forms': forms,
    }
    return render(request, 'academic/create_class.html', context)


def show_class_list(request):
    cls_list = StudentClass.objects.all()
    context = {
        'class_list': cls_list,
    }

    return render(request, 'academic/class_dashboard.html', context)


def delete_class(request, class_id):
    class_delete = StudentClass.objects.get(id=class_id)
    class_delete.delete()

    return redirect('class_list')


def edit_class(request, class_id):
    class_edit = StudentClass.objects.get(id=class_id)
    if request.method == 'POST':
        forms = CreateClassForm(request.POST, instance=class_edit)
        forms.save()

        return redirect('class_list')
    else:
        forms = CreateClassForm(instance=class_edit)
    context = {
        'forms': forms,
    }

    return render(request, 'academic/edit_class.html', context)
