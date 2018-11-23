from django.shortcuts import render
# rest api response import
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User

# Create your views here.
@api_view()
def check_user(request, user_name):
    # is_exist use if the user resided or not and it is use less time and return true/false
    isExist = User.objects.filter(username=user_name).exists()

    return Response({'status': isExist})
