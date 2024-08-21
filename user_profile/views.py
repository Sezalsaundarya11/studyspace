from user_profile.models import Profiles
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny #, IsAuthenticated
from django.contrib.auth import authenticate
from user_profile.serializer import RegisterUserSerializer , LoginUserSerializer
# Create your views here.

def get_token(user):
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    return {
        'refresh': str(refresh),
        'access' : access_token
    }

class RegisterView(APIView):
    permission_classes = [AllowAny] 
    def post(self,request):
        register_data = request.data
        serializer = RegisterUserSerializer(data=register_data)

        if serializer.is_valid():
            user_obj = User.objects.create_user(
                username= register_data['username'],
                password=register_data['password']
            )
            Profiles.objects.create(
                user = user_obj,
                firstName= register_data['firstname'],
                lastName = register_data['lastname'],
                email = register_data['email']

            )
            token = get_token(user_obj)

            return Response({
            'message': 'User added',
            'token' : token
            }, status=201)
        
        else:
            return Response(serializer.errors, status=400)
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        login_data = request.data
        serializer = LoginUserSerializer(data=login_data)

        if serializer.is_valid():


            user = authenticate(
                username = login_data['username'],
                password = login_data['password']
            )
            if user is not None:
                token = get_token(user)
                return Response({
                    'token': token
                }, status=200)
            else:
                return Response(data='Invalid credentials', status=401)
            
        else:
            return Response(serializer.errors, status=400)


