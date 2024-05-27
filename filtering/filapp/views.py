from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializers
from rest_framework.generics import ListAPIView
# Create your views here.

class Studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)