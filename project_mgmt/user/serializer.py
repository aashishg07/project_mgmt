
from rest_framework import serializers
from .models import MyUser


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type': 'password'}, write_only = True)

    class Meta:
        model = MyUser
        fields = ['email', 'name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("Password didn't match.")
        return attrs
    
    def create(self, validate_data):
        return MyUser.objects.create_user(**validate_data)
    

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model = MyUser
        fields = ['email', 'password']

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'name']

