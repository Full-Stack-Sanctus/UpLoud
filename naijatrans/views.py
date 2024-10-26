from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


# Check Authentication: Ensures that the user must be logged in
@login_required
def check_authentication(request):
    return JsonResponse({'isAuthenticated': True})  # Return authenticated status

# Check Authentication for Anonymous Users: Returns authentication status without requiring login
def check_authentication_anonymous(request):
    is_authenticated = request.user.is_authenticated
    return JsonResponse({'isAuthenticated': is_authenticated})
    
    
    
    
    

# Register View: Registers a new user
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()  # Save user
        refresh = RefreshToken.for_user(user)  # Generate JWT tokens for the new user
        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    


    


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    
    if serializer.is_valid():
        user_data = serializer.validated_data  # Access validated data dictionary
        email = user_data['email']  # Extract validated email
        password = user_data['password']
        
        # Use the email for authentication
        user = authenticate(request, username=email, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)  # Create JWT tokens for the authenticated user
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'success': 'Logged in successfully'
            }, status=status.HTTP_200_OK)
        
        return Response({'non_field_errors': ['Invalid email or password.']}, status=status.HTTP_400_BAD_REQUEST)
    
    # If the serializer is not valid, return the errors
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








# Profile View: Returns the profile of the authenticated user
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Ensure user is authenticated
def profile(request):
    user = request.user  # Access the authenticated user
    serializer = UserSerializer(user)
    return Response(serializer.data)


