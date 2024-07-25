from room.models import Room
from Topic.models import Topic
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class GetAllRoom(APIView):
    def get(self,request):
        room_names = Room.objects.all().values()
        return Response(data = room_names , status=200)

class RoomView(APIView):
    def get(self,request):
        room_data = request.GET
        room_name = Room.objects.filter(
            id = room_data['id']
        ).values()
        return Response(data=room_name, status=200)


    def post(self,request):
        room_data = request.data
        topic_obj = Topic.objects.get(
            name=room_data['topic']
        )

        Room.objects.create(
            name = room_data["roomName"],
            description = room_data['roomDesc'],
            topic = topic_obj 
        )

        return Response(data = 'added', status=200)
    


        