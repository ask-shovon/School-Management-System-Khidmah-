from django.urls import path
from .views import *
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create_class/', create_class, name='create-class'),

]