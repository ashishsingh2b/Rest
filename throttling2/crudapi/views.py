from django.shortcuts import render
from .customauth import Mypermission
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
from .throttling import JackRateThrottle
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.

class Studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viwestu'

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

class StudentRetrive(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viwestu'

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'


  
# # ReadOnly Model Based
# class StudentViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
        



    





