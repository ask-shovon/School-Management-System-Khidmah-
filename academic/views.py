from django.shortcuts import render
from .forms import CreateClassForm


# Create your views here.
def dashboard(request):
    return render(request, 'academic/dashboard.html')


# create class
def create_class(request):
    print('get')
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