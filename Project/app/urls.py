
from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/users/register', CreateUserView.as_view()),
    path('api/v1/users/getalluser', GetAllUsersView.as_view()),
    path('api/v1/users', GetUserView.as_view()),
    
]
