from django.shortcuts import render

from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

# Create your views here.

#@api_view(['GET','POST','PUT','PATCH','DELETE'])
#Crud Model Based
class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes =[SessionAuthentication]
    #permission_classes = [IsAuthenticated]
    #permission_classes=[IsAdminUser]
    #permission_classes=[IsAuthenticatedOrReadOnly]
    #permission_classes=[DjangoModelPermissions]
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]


  
# # ReadOnly Model Based
# class StudentViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
        



    





