from user_profile.models import Profiles
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny #, IsAuthenticated
from django.contrib.auth import authenticate
from user_profile.serializer import RegisterUserSerializer
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
            print(serializer.validated_data)
            user_obj = serializer.save()
        


        # username_obj = User.objects.filter(
        #     username = register_data['username']
        # )
        # if username_obj.exists():
        #     return Response(data='user already present', status = 208)
        # else:
        #     user_obj = User.objects.create_user(
        #         username= register_data['username'],
        #         password=register_data['password']
        #     )
        #     Profiles.objects.create(
        #         user = user_obj,
        #         firstName= register_data['firstname'],
        #         lastName = register_data['lastname'],
        #         email = register_data['email']

        #     )
        #     # refresh =  RefreshToken.for_user(user_obj)
        #     # access_token = str(refresh.access_token)
            token = get_token(user_obj)

            return Response({
            'message': 'User added',
            # 'access': access_token,
            # 'refresh': str(refresh)
            'token' : token
            }, status=201)
        
        else:
            return Response(serializer.errors, status=400)
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        login_data = request.data

        user = authenticate(
            username = login_data['username'],
            password = login_data['password']
        )
        if user is not None:
            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }, status=200)
        else:
            return Response(data='Invalid credentials', status=401)


