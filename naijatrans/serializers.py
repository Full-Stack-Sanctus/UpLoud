from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model


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

        # Authenticate the user using email instead of username
        try:
            # Fetch the user by email
            user = get_user_model().objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")

        # Now authenticate the user by their username (email) and password
        user = authenticate(username=user.email, password=password)
        
        if user is None:
            raise serializers.ValidationError("Invalid email or password.")

        # Return the user instance (or tokens if needed)
        return {
            'email': email,
            'password': password,
            'refresh_token': str(RefreshToken.for_user(user)),
            'access_token': str(RefreshToken.for_user(user).access_token)
        }