from naijatrans.models import UserLogin  # Adjust based on your project structure

from django.contrib.auth import get_user_model

class EmailAuthBackend:
    """Authenticate using an email address."""
    
    def authenticate(self, request, username=None, password=None):
        try:
            # Check if the user exists with the provided email
            user = UserLogin.objects.get(email=username)  # Use your custom model
            # Check if the password matches
            if user.check_password(password):
                return user
        except UserLogin.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

