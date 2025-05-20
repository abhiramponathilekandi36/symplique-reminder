from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReminderSerializer


# Create your views here.

class ReminderCreateView(APIView):
    def post(self,request):
        serializser = ReminderSerializer(data = request.data)
        if serializser.is_valid():
            serializser.save()
            return Response(serializser.data,status=status.HTTP_201_CREATED)
        return Response(serializser.errors,status=status.HTTP_400_BAD_REQUEST)