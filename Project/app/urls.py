
from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/users/getalluser', TestView.as_view()),
]
