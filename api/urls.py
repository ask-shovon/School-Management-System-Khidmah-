from django.urls import path
from .views import *

urlpatterns = [
    path('check/user/<user_name>', check_user, name='check_user'),
    path('add-class', StudentClassApi.as_view()),
    path('class-list/', StudentClassListApi.as_view()),

]