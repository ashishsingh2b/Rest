from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

class Studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrive(RetrieveAPIView):
    queryset =Student.objects.all()
    serializer_class =  StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset =Student.objects.all()
    serializer_class =  StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset =Student.objects.all()
    serializer_class =  StudentSerializer

class StudentCreate(ListCreateAPIView):
    queryset =Student.objects.all()
    serializer_class =  StudentSerializer

class StudentRetriveUpdate(RetrieveUpdateAPIView):
    queryset =Student.objects.all()
    serializer_class =  StudentSerializer

class StudentRetriveDelete(RetrieveDestroyAPIView):
    queryset =Student.objects.all()
    serializer_class =  StudentSerializer

class StudentRetriveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset =Student.objects.all()
    serializer_class =  StudentSerializer

    
