from django.shortcuts import render
from .serializer import SingerSerializer,SongSerializer
from .models import Song,Singer
from rest_framework import viewsets
# Create your views here.

class Singerviewset(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongViewset(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class=SongSerializer
