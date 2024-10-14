from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


class UserLoginTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='testpassword'
        )
        self.client = APIClient()

    def test_login(self):
        url = reverse('login')  # Make sure this matches your login view's URL name
        data = {
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }

        # Post request to login
        response = self.client.post(url, data, format='json')

        # Debugging: Print response data
        print(response.data)
        
        # Check if login was successful
        self.assertEqual(response.status_code, 200)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)
