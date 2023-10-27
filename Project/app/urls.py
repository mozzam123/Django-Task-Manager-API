
from django.urls import path
from .views import *

urlpatterns = [
    # Users
    path('api/v1/users/register', CreateUserView.as_view()),
    path('api/v1/users/getalluser', GetAllUsersView.as_view()),
    path('api/v1/users', GetUserView.as_view()),

    # Task
    path('api/v1/tasks/createtask', CreateTaskView.as_view()),
    path('api/v1/tasks/getalltask', GetAllTaskView.as_view()),
    path('api/v1/tasks/gettask', GetTaskView.as_view()),
    path('api/v1/tasks/deletetask', DeleteTaskView.as_view()),

]
