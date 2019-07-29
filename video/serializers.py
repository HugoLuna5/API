from rest_framework import serializers
from .models import Video
from django.contrib.auth.models import User

class UserSerializable(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email')

class VideoSerializer(serializers.ModelSerializer):
    user = UserSerializable(read_only=True)
    class Meta:
        model = Video
        fields = ('id','title','description', 'user')