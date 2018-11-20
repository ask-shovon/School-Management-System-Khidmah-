from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import UserResgisterForm, UserLoginForm

# Create your views here.
def registration(request):
    if request.method == 'POST':
        forms = UserResgisterForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            try:
                # it dyamically use all sort of permission
                User.objects.create_user(username=username, password=password)

                return redirect('user-login')
            except:
                errmsg = "user already exist"
                context = {
                    'forms': forms,
                    'errmsg': errmsg,
                }
                return render(request, 'register.html', context)



        else:
            context = {'forms': forms}
            return render(request, 'register.html', context)


    forms = UserResgisterForm()
    context = {'forms':forms}
    return render(request,'register.html',context)

def user_login(request):
    if request.method == "POST":
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            # it is a buildin funciton
            user = authenticate(username=username, password=password)
            #it is a build in function
            if user:
                login(request, user)
                return HttpResponse("log in success")
            else:
                errmsg = "user name or password doesn't match"
                context = {
                    'forms': forms,
                    'errmsg': errmsg,
                }
                return render(request, 'user_login.html', context)


    forms = UserLoginForm()
    context = {'forms': forms}
    return render(request, 'register.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')