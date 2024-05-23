from django.shortcuts import render

from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

#@api_view(['GET','POST','PUT','PATCH','DELETE'])
#Crud Model Based
# class StudentViewset(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
  
# ReadOnly Model Based
class StudentViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
        



    





