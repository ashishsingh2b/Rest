from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .mypagination import MypageNumberCurser
# Create your views here.

class Studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MypageNumberCurser

        



    





