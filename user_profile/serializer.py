from rest_framework import serializers
from django.contrib.auth.models import User
from user_profile.models import Profiles
import re

class RegisterUserSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=50)
    lastname = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'firstname', 'lastname', 'email']

    
    def validate_username(self,value):
        if User.objects.filter(username = value).exists():
            raise serializers.ValidationError("A user with this username is already present")
        
        if len(value) < 6:
            raise serializers. ValidationError("Username must be 6 character long")
            
        return value
    
    
    
    def validate_email(self, value):
        if Profiles.objects.filter(email = value).exists():
            raise serializers.ValidationError("email id already present")
        return value
    

    
    def validate_password(self, password):
        if len(password) < 6:
            raise serializers.ValidationError(
                {
                    "Too short": "Password must contain 6 characters"
                }
            )
        if len(password) > 30:
            raise serializers.ValidationError(
                {
                    "Too long" : "Password cannot have more than 30 characters"
                }
            )
        
        if not re.search(r'[A-Z]', password):
            raise serializers.ValidationError(
                {
                    "Missing capital letter" : "Password must contain one capital letter"
                }
            )
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise serializers.ValidationError(
                {
                    "Missing special character" : "Password must contain one special charcater"
                }
            )
    
    def validate(self, data):
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        if not isinstance(firstname, str) or not firstname.isalpha():
            raise serializers.ValidationError(
                {
                    "ValueError": "Not a valid firstname"
                }
            )
        
        if not isinstance(lastname, str) or not lastname.isalpha():
            raise serializers.ValidationError(
                {
                    "ValueError" : "Not a valid lastname"

                }
            )
        return data
        

    # def create(self, validated_data):
    #     user_obj = User.objects.create_user(
    #         username= validated_data['username'],
    #         password= validated_data.pop('password')
    #         )
    #     Profiles.objects.create(
    #         user = user_obj,
    #         firstName= validated_data['firstname'],
    #         lastName = validated_data['lastname'],
    #         email = validated_data['email']

    #     )

    #     return user_obj
    
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required =True)
    password = serializers.CharField(write_only = True)


    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError("Username & password is mandatory")
        
        return data
        
        
    

    
        



        
    
    





       