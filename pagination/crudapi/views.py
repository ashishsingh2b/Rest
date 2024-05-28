from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView

# Create your views here.

class Studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
        



    





