from rest_framework.views import APIView
from rest_framework.response import Response
from Topic.models import Topic
from room.models import Room
from Topic.serializer import CreateTopicPostSerailizer

# Create your views here.
class ViewAllTopic(APIView):
    def get(self,request):
        topic_data = Topic.objects.all().values()
        return Response(data = topic_data, status=200)
    
class TopicView(APIView):
    def get(self,request):
        topic_data = request.GET
        topic_obj = Topic.objects.get(
            name__iexact = topic_data['topicName']
        )
        room_obj = Room.objects.filter(
            topic = topic_obj
        ).values()

        return Response(data = room_obj, status=200)

    def post(self,request):
        topic_data = request.data
        serializer = CreateTopicPostSerailizer(data=topic_data)

        if serializer.is_valid():
            # print(serializer.validated_data)
            topic_obj = Topic.objects.filter(
                name__iexact = topic_data['topicName']
            )
            if topic_obj.exists():
                return Response(data='topic already present' ,status=200)
            else:
                Topic.objects.create(
                    name = topic_data['topicName']
                )
                return Response(data = 'topic added', status=200)
        else:
            return Response(serializer.errors, status=400)

        
        
    def delete(self, request):
        topic_data = request.GET
        print(topic_data)
        try:
            topic_obj=Topic.objects.get(
                id = topic_data['id']
            )
            topic_obj.delete()
        except Exception as e:
            return Response(data=str(e), status=404)
            

        return Response(data='succesfully deleted', status=200)

        

            
