from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import RegistrationSerializer, LoginSerializer, ProfileSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from .models import MyUser



# Create your views here.
class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg': 'Registered successfully!!!'}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            return Response({'msg': 'Login successful.'}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': "Email or password didn't match"})
        
class ProfileView(APIView):
    def get(self, request, pk):
        try:
            user_profile = MyUser.objects.get(pk=pk)
        except MyUser.DoesNotExist:
            return Response({'msg': f"Id {pk} doesn't exist."})
        serializer = ProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
