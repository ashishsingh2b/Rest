from django.shortcuts import render
from .serializers import SingerSerializer,SongSerializer
from .models import Song,Singer
from rest_framework import viewsets
# Create your views here.
class Singerview(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class  = SingerSerializer

class Songview(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer