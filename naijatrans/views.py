from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required  # This decorator ensures that the user must be logged in to access this view
def check_authentication(request):
    return JsonResponse({'isAuthenticated': True})  # User is authenticated

def check_authentication_anonymous(request):
    # Returns whether the user is authenticated without requiring login.
    is_authenticated = request.user.is_authenticated
    return JsonResponse({'isAuthenticated': is_authenticated})



@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login(request):
    # Authenticate the user
    
    serializer = LoginSerializer(data=request.data)  # Define the serializer here
    
    
    print("Incoming data:", request.data)  # Debugging line
  
    if serializer.is_valid():  # Check if the data is valid
        email = serializer.validated_data['email']  # Access validated data
        password = serializer.validated_data['password']

        user = authenticate(request, username=request.data['email'], password=request.data['password'])
        
        
        if user:  # If user is authenticated
            # Here, generate and return the token or user info
            return Response({'refresh': str(refresh),
            'access': str(refresh.access_token),
            'success': 'Logged in successfully'}, status=status.HTTP_200_OK)
            
        else:
            
            # Return error response for invalid credentials
            return Response({'non_field_errors': ['Invalid email or password.']}, status=status.HTTP_400_BAD_REQUEST)
    
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        




@api_view(['GET'])
def profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)
