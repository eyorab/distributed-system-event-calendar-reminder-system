from rest_framework import serializers
from .models import User
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']  # Add all required fields

    def create(self, validated_data):
        # Create and return a new User instance
        user = User.objects.create(**validated_data)
        return user