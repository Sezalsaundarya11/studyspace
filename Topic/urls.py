from django.urls import path
from Topic.views import ViewAllTopic, TopicView

urlpatterns = [
    path('getalltopic/', ViewAllTopic.as_view()),
    path('gettopic/', TopicView.as_view()),
    path('createtopic/', TopicView.as_view()),
    path('deletetopic/', TopicView.as_view())
] 