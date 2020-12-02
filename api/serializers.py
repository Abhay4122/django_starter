from dajngo.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
