from django.core import serializers
from rest_framework import serializers
from .models import Users
from rest_framework.validators import UniqueValidator

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['name', 'email', 'student_number', 'nickname','password', 'sex', 'major', 
        'created_at', 'modified_at']
    name = serializers.CharField(max_length=45)
    email = serializers.CharField(max_length=45, validators=[UniqueValidator(queryset=Users.objects.all())])
    student_number = serializers.CharField(max_length=45, validators=[UniqueValidator(queryset=Users.objects.all())])
    nickname = serializers.CharField(max_length=45)
    password = serializers.CharField(max_length=45)
    sex = serializers.CharField(max_length=45)
    major = serializers.CharField(max_length=45)
    created_at = serializers.DateTimeField()
    modified_at = serializers.DateTimeField()