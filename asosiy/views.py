from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class AudiosApiView(APIView):
    def get(self, request):
        all_audios = Audio.objects.all()
        ser = AudioSer(all_audios, many=True)
        return Response(ser.data)

class TopicsApiView(APIView):
    def get(self, request):
        all_topics = Topic.objects.all()
        ser = TopicSer(all_topics, many=True)
        return Response(ser.data)

class TopicAudiosApiView(APIView):
    def get(self, request, pk):
        all_audios = Audio.objects.filter(topic__id=pk)
        ser = AudioSer(all_audios, many=True)
        return Response(ser.data)


