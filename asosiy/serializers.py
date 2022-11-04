from rest_framework.serializers import ModelSerializer
from .models import *

class TopicSer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class AudioSer(ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'
