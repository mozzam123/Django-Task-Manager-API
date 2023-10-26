from rest_framework.status import *
from django.http import JsonResponse
from rest_framework.views import APIView
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from .models import *
from .serializers import *
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class CreateUserView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        try:
            response = {"status": "success", "data": "",
                        "reason": "", "httpstatus":  HTTP_200_OK}
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                response['status'] = "success"
                response["data"] = serializer.data
                response['httpstatus'] = HTTP_201_CREATED
            else:
                print(serializer.error_messages)
                response['status'] = "seriaerror"
                response['reason'] = str(serializer.errors)
                response['httpstatus'] = HTTP_400_BAD_REQUEST
        except Exception as e:
            
            response['status'] = 'error'
            response['reason'] = str(e)
            response["httpstatus"] = HTTP_500_INTERNAL_SERVER_ERROR

        return JsonResponse(response, status=response.get("httpstatus"))


class GetAllUsersView(APIView):
    def get(self, request):
        try:
            response = {"status": "success", "data": "",
                        "reason": "", "httpstatus":  HTTP_200_OK}
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            response['status'] = "success"
            response["data"] = serializer.data
            response['httpstatus'] = HTTP_201_CREATED

            
        except Exception as e:
            response['status'] = 'error'
            response['reason'] = str(e)
            response["httpstatus"] = HTTP_500_INTERNAL_SERVER_ERROR
        return JsonResponse(response, status=response.get("httpstatus"))
