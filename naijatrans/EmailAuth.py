from naijatrans.models import UserLogin  # Adjust based on your project structure

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
        try:
            return UserLogin.objects.get(pk=user_id)  # Use your custom model
        except UserLogin.DoesNotExist:
            return None
