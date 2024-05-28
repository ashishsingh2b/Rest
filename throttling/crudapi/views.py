from django.shortcuts import render
from .customauth import Mypermission
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .throttling import JackRateThrottle

# Create your views here.

#@api_view(['GET','POST','PUT','PATCH','DELETE'])
#Crud Model Based
class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes =[SessionAuthentication]
    throttle_classes = [AnonRateThrottle,JackRateThrottle]
    permission_classes = [IsAuthenticatedOrReadOnly]
    #permission_classes=[IsAdminUser]
    #permission_classes=[IsAuthenticatedOrReadOnly]
    #permission_classes=[DjangoModelPermissions]
    #permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    #permission_classes = [Mypermission]


  
# # ReadOnly Model Based
# class StudentViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
        



    





