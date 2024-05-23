from rest_framework import serializers
from .models import Student


#validators
def start_with_a(value):
    if value[0].lower() != 'a':
        raise serializers.ValidationError("Name should start with 'a'")

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50,validators= [start_with_a] )
    roll = serializers.IntegerField()
    city= serializers.CharField(max_length=50)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        print(instance.name)
        instance.name =validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll =validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()

    #field validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value
    
    #object validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm and ct:  # Ensure both name and city are present
            if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
                raise serializers.ValidationError("City must be ranchi")
        return data



        