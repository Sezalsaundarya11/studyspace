from django.urls import path
from room.views import GetAllRoom , RoomView

urlpatterns = [
    path('getallroom/', GetAllRoom.as_view()),
    path('createroom/', RoomView.as_view()),
    path('getsingleroom/', RoomView.as_view())
] 