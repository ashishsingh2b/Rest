from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    #song = serializers.HyperlinkedIdentityField(view_name='song-detail')
    class Meta:
        model = Student
        fields = ['id','url','name','roll','city']
    