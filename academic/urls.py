from django.urls import path
from .views import *
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create_class/', create_class, name='create-class'),
    path('class_list/', show_class_list, name='class_list'),
    path('class_delete/<int:class_id>', delete_class, name='class_delete'),
    path('class_edit/<int:class_id>', edit_class, name='class_edit'),

]