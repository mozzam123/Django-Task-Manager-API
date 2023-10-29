
from django.urls import path
from .views import *

urlpatterns = [
    # Users
    path('api/users/register', CreateUserView.as_view()),
    path('api/users/getalluser', GetAllUsersView.as_view()),
    path('api/users', GetUserView.as_view()),

    # Task
    path('api/tasks/createtask', CreateTaskView.as_view()),
    path('api/tasks/getalltask', GetAllTaskView.as_view()),
    path('api/tasks/gettask', GetTaskView.as_view()),
    path('api/tasks/deletetask', DeleteTaskView.as_view()),

]
