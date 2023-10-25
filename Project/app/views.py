from rest_framework.status import *
from django.http import JsonResponse
from rest_framework.views import APIView

# Create your views here.
class TestView(APIView):
    def get(self, request):
        return JsonResponse({"message": "Its working"})