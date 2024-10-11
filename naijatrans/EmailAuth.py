from django.contrib.auth.models import User

class EmailAuthBackend:
    """Authenticate using an email address."""
    
    def authenticate(self, request, username=None, password=None):
        try:
            # Check if the user exists with the provided email
            user = User.objects.get(email=username)
            # Check if the password matches
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

