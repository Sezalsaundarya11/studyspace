from django.shortcuts import render
from room.models import Room
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class GetAllRoom(APIView):
    def get(self,request):
        room_names = Room.objects.all().values()
        return Response(data = room_names , status=200)
