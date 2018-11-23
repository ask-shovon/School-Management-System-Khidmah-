from django.urls import path
from .views import check_user

urlpatterns = [
    path('check/user/<user_name>', check_user, name='check_user'),

]