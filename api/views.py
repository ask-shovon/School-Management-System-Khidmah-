from django.shortcuts import render
# rest api response import
from rest_framework.decorators import api_view
from rest_framework.response import Response
#APIview for studentClassapi
from rest_framework.views import APIView
# status use for status code
from rest_framework import status

from django.contrib.auth.models import User
# serializer use for same as form
from .serializers import ClassSerializer
from academic.models import StudentClass


# Create your views here.
@api_view()
def check_user(request, user_name):
    # is_exist use if the user resided or not and it is use less time and return true/false
    isExist = User.objects.filter(username=user_name).exists()

    return Response({'status': isExist})


class StudentClassApi(APIView):
    def post(self, request):
        print(request.data)
        # for post request data=request.data
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'ok'}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class StudentClassListApi(APIView):

    def get(self, request):
        clslist = StudentClass.objects.all()
        #this serilizer user for object list to make json
        #if objects.all() many = Ture need, when get then no need many
        serializer = ClassSerializer(clslist, many=True)
        return Response(serializer.data)
