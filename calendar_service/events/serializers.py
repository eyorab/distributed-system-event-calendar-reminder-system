from rest_framework import serializers
from datetime import datetime
from .mongodb import MongoDBClient

mongo_client = MongoDBClient()
collection = mongo_client.get_collection("events")


class EventSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    description = serializers.CharField(max_length=1000)
    category = serializers.ChoiceField(choices=["work", "personal"])
    # user_id = serializers.CharField(max_length=255)
    
    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("Ending times must be after starting times")
        if data['start_date'] < datetime.now(data['start_date'].tzinfo):
            raise serializers.ValidationError("Starting time must be in the future")
        if data['title'] in [event['title'] for event in collection.find({})]:
            raise serializers.ValidationError("Title is aleardy existed")
        return data
