from django.urls import path, include
from .views import *

urlpatterns = [
    path('create-direction/', create_direction),
    path('get-direction/', get_direction),
    path('change-direction/<int:pk>/', change_direction),
    path('delete-direction/<int:pk>/', delete_direction),
    path('create-student/', create_student),
    path('get-students/', get_students),
    path('get-student/<int:pk>/', get_student),
    path('change-student/<int:pk>/', change_student),
    path('create-group/', create_group),
    path('get-groups/', get_groups ),
    path('get-group/<int:pk>/', get_group ),
    path('change-group/<int:pk>/', change_group ),
    path('add-student-to-group/<int:pk>/', add_student_to_group ),
    path('remove-student-in-group/<int:pk>/', remove_student_in_group ),
    path('create-region/', create_region ),
    path('get-region/', get_region ),
    path('change-region/<int:pk>/', change_region ),
    path('create-payment/', create_payment ),
    path('get-payment/', get_payment ),
    path('change-payment/<int:pk>/', change_payment ),
    path('get-payment-by-student/<int:pk>/', get_payment_by_student ),
    path('get-unpayment-student/', get_unpayment_student ),

]
