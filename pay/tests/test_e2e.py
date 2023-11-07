import os, sys
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")

from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework import status
from ..models  import Pay
from ..serializers import PaysSerializer
from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
from django.urls import reverse
import json
from django.contrib.auth import get_user_model
User = get_user_model()

from faker import Faker
class PayAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.fake = Faker()
        # print(Faker().email())
        # print(Faker().password())
        self.email = Faker().email()
        self.password = Faker().password()
        self.user = User.objects.create_user(email='test@test.com', password='test')

    def authenticate_user(self):
        # print(self.email)
        login_data = {
            # "email": self.email,
            # "password": self.password
            "email": "test@test.com",
            "password": "test"
        }
        # Send a POST request to the authentication endpoint to obtain tokens
        response = self.client.post('/auth/login/', json.dumps(login_data), content_type='application/json')
        # print(response)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Parse the response JSON to get the tokens
        tokens = json.loads(response.content)
        return tokens


    def test_pay_list_get(self):
        tokens = self.authenticate_user()
        access_token = tokens['tokens']['access_token']
        authorization_header = f'Bearer {access_token}'

        url = reverse('pay_list')  # Replace 'pay_list' with the actual URL name
        response = self.client.get(url, HTTP_AUTHORIZATION=authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pay_list_post(self):
        tokens = self.authenticate_user()
        access_token = tokens['tokens']['access_token']
        authorization_header = f'Bearer {access_token}'
        data = {
            "date": "2023-11-06",
            "description": "staaaaring",
            "amount": "100",
            "category": "ONLINE_SERVICES"
        }
        url = reverse('pay_list')  # Replace 'pay_list' with the actual URL name
        # print(url)
        # http://localhost:8000/pay/pays/
        response = self.client.post(url, data, format='json', HTTP_AUTHORIZATION=authorization_header)
        # print(response)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

