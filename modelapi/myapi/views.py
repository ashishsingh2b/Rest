from django.shortcuts import render
from .models import Student
from.serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework.response import Response
import io
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data =request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer =StudentSerializer(pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            return Response(res)
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')