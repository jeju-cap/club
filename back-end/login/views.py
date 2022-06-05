from django.shortcuts import render
from rest_framework import serializers
from django.core import serializers

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse
from .models import Users
from .serializer import UsersSerializer

'''@api_view(['GET'])
def get_api(request):
    posts = Users.objects.all()
    serailized_posts= PostSerializer(posts, many=True)
    return Response(serailized_posts.data)'''

@api_view(['POST'])
def signup_api(request):
    if request.method == 'GET':
        return HttpResponse(status=200)
    if request.method == 'POST':
        serializer = UsersSerializer(data = request.data, many=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data ,status=200)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)