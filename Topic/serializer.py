from rest_framework import serializers

class CreateTopicPostSerailizer(serializers.Serializer):
    topicName = serializers.CharField(max_length=50)

    def validate(self,data):
        if isinstance(data,str):
            return data
        else:
            raise serializers.ValidationError(
                {
                    "TopicNameError" : "Not a valid string"
                }
            )