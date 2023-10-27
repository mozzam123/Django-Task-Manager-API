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


@method_decorator(csrf_exempt, name='dispatch')
class GetUserView(APIView):
    def get(self, request):
        try:
            response = {"status": "success", "data": "",
                        "reason": "", "httpstatus":  HTTP_200_OK}
            params = request.query_params
            queryset = User.objects.get(username=params.get('username'))
            serializer = UserSerializer(queryset)
            response['status'] = "success"
            response["data"] = serializer.data
            response['httpstatus'] = HTTP_201_CREATED

        except User.DoesNotExist:
            response['status'] = 'Failed'
            response['reason'] = "User does not exist"
            response["httpstatus"] = HTTP_404_NOT_FOUND

        except Exception as e:
            response['status'] = 'error'
            response['reason'] = str(e)
            response["httpstatus"] = HTTP_500_INTERNAL_SERVER_ERROR
        return JsonResponse(response, status=response.get("httpstatus"))


class CreateTaskView(APIView):
    def post(self, request):
        try:
            response = {"status": "success", "data": "",
                        "reason": "", "httpstatus":  HTTP_200_OK}

            data = request.data
            serializer = TaskSerializer(data=data)
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


class GetAllTaskView(APIView):
    def get(self, request):
        try:
            response = {"status": "success", "data": "",
                        "reason": "", "httpstatus":  HTTP_200_OK}
            queryset = Task.objects.all()
            serializer = TaskSerializer(queryset, many=True)
            response['status'] = "success"
            response["data"] = serializer.data
            response['httpstatus'] = HTTP_201_CREATED

        except Exception as e:
            response['status'] = 'error'
            response['reason'] = str(e)
            response["httpstatus"] = HTTP_500_INTERNAL_SERVER_ERROR

        return JsonResponse(response, status=response.get("httpstatus"))


class GetTaskView(APIView):
    def get(self, request):
        try:
            response = {"status": "success", "data": "",
                        "reason": "", "httpstatus":  HTTP_200_OK}
            params = request.query_params
            queryset = Task.objects.get(title=params.get('title'))
            serializer = TaskSerializer(queryset)
            if queryset:
                response['status'] = "success"
                response["data"] = serializer.data
                response['httpstatus'] = HTTP_201_CREATED

        except Task.DoesNotExist:
            response['status'] = "Failed"
            response["reason"] = "Task does not found"
            response['httpstatus'] = HTTP_200_OK

        except Exception as e:
            response['status'] = 'error'
            response['reason'] = str(e)
            response["httpstatus"] = HTTP_500_INTERNAL_SERVER_ERROR

        return JsonResponse(response, status=response.get("httpstatus"))


class DeleteTaskView(APIView):
    def get(self, request):
        try:
            response = {"status": "success", "data": "",
                        "reason": "", "httpstatus":  HTTP_200_OK}
            params = request.query_params
            queryset = Task.objects.get(title=params.get('title'))
            queryset.delete()
            response['status'] = "success"
            response["data"] = "deleted succesfull"
            response['httpstatus'] = HTTP_200_OK

        except Task.DoesNotExist:
            response['status'] = "Failed"
            response["reason"] = "Task does not found"
            response['httpstatus'] = HTTP_200_OK

        except Exception as e:
            response['status'] = 'error'
            response['reason'] = str(e)
            response["httpstatus"] = HTTP_500_INTERNAL_SERVER_ERROR

        return JsonResponse(response, status=response.get("httpstatus"))
