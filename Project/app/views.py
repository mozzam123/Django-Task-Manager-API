from rest_framework.status import *
from django.http import JsonResponse
from rest_framework.views import APIView

# Create your views here.
class TestView(APIView):
    def get(self, request):
        return JsonResponse({"message": "Its working"})




import pymongo

client = pymongo.MongoClient('mongodb+srv://mozzam:mozzam@latestcluster.wdjuvrc.mongodb.net/')
dbname = client['Django']

#Define Collection
collection = dbname['mascot']

mascot_1={
    "name": "Sammy",
    "type" : "Shark"
}

collection.insert_one(mascot_1)

mascot_details = collection.find({})

for r in mascot_details:
    print(r['name'])