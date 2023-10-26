from rest_framework.status import *
from django.http import JsonResponse
from rest_framework.views import APIView

# Create your views here.
class TestView(APIView):
    def get(self, request):
        return JsonResponse({"message": "Its working"})




# import pymongo

# client = pymongo.MongoClient('mongodb+srv://mozzam:mozzam@latestcluster.wdjuvrc.mongodb.net/')
# dbname = client['Django_API']

# #Define Collection
# Usercollection = dbname['User']
# collection = dbname['Task']

# User_1={
#     "name": "Sammy",
#     "type" : "Shark"
# }

# collection.insert_one(User_1)

# user_details = Usercollection.find({})
