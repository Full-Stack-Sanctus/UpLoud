from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Serializer for user login
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Assuming you're using Django's built-in User model
        fields = ['id', 'email', 'password']

# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Assuming you're using Django's built-in User model
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user and hash the password
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

# Serializer for login


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError("Email and password are required.")

        # Authenticate the user using email as the username
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid email or password.")

        # Return the user instance, not a dictionary
        return user  # Ensure this returns the user instance
