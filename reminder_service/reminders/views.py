from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Reminder
from .serializers import ReminderSerializer
from .mongodb import MongoDBClient
# from reminder_service.reminder_service.consumer import ReminderConsumer

mongo_client = MongoDBClient()
collection = mongo_client.get_collection("reminders")

class ReminderAPIView(APIView):
    def post(self, request):
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            collection.insert_one(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        reminders = collection.find()
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)
