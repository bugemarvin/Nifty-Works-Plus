from django.test import TestCase
from accounts.models import UserModel
from accounts.serializers import UserSerializer
from rest_framework.test import APIRequestFactory
from rest_framework.authtoken.models import Token
from accounts.auth.login_views import user_login
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserSerializerTest(TestCase):
    '''
        Test the UserSerializer class in accounts/serializers.py

        Test cases:
        - Test if the serializer is valid with valid data
        - Test if the serializer is invalid with invalid data
        - Test if the serializer creates a user object with the given data

        The UserSerializer class is responsible for validating and creating user objects.
        The test cases are testing the validation and creation of user objects.
    '''
    def setUp(self):
        self.valid_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        self.serializer = UserSerializer(data=self.valid_data)

    def test_serializer_valid_data(self):
        self.assertTrue(self.serializer.is_valid())

    def test_serializer_invalid_data(self):
        invalid_data = {
            'username': 'testuser',
            'email': 'invalid_email',
            'password': 'testpassword'
        }
        serializer = UserSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())

    def test_serializer_create_user(self):
        user = self.serializer.create(self.valid_data)
        self.assertIsInstance(user, UserModel)
        self.assertEqual(user.username, self.valid_data['username'])
        self.assertEqual(user.email, self.valid_data['email'])
        self.assertTrue(user.check_password(self.valid_data['password']))

class UserModelTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpassword'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('testpassword'))

    def test_user_str_representation(self):
        self.assertEqual(str(self.user), 'test@example.com')

class UserLoginTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.user_model = UserModel.objects.create(email='test@example.com')

    def test_user_login_with_username_password(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)

    def test_user_login_with_email_password(self):
        url = reverse('login')
        data = {'username': 'test@example.com', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)

    def test_user_login_with_invalid_credentials(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 401)
        self.assertIn('error', response.data)

class UserLogoutTestCase(APITestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_logout(self):
        response = self.client.post('/accounts/auth/logout/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Successfully logged out.'})
        self.assertFalse(self.user.auth_token)

    def test_user_logout_without_authentication(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/accounts/auth/logout/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {'detail': 'Authentication credentials were not provided.'})

class RegisterUserTestCase(APITestCase):
    def test_register_user_success(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserModel.objects.count(), 1)
        self.assertEqual(UserModel.objects.get().username, 'testuser')

    def test_register_user_invalid_data(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(UserModel.objects.count(), 0)
