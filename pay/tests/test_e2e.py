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

class PayAPITestCase(TestCase):
    def setUp(self):
        login_data = {
            "email": "test@test.com",
            "password": "test"
        }
        
        # Send a POST request to the authentication endpoint to obtain tokens
        response = self.client.post('/auth/login/', json.dumps(login_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Parse the response JSON to get the tokens
        tokens = json.loads(response.content)
        return tokens



    # def test_pay_list_get(self):
        # url = reverse('pay_list')  # Replace 'pay_list' with the actual URL name
        # response = self.client.get(url)

        # self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pay_list_post(self):
        url = reverse('pay_list')  # Replace 'pay_list' with the actual URL name
        data = {'amount': 100, 'description': 'Test Pay'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_pay_detail_get(self):
        pay = Pay.objects.create(owner=self.user, amount=50, description='Test Pay')
        url = reverse('pay_detail', args=[pay.id])  # Replace 'pay_detail' with the actual URL name
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pay_detail_put(self):
        pay = Pay.objects.create(owner=self.user, amount=50, description='Test Pay')
        url = reverse('pay_detail', args=[pay.id])  # Replace 'pay_detail' with the actual URL name
        data = {'amount': 75, 'description': 'Updated Pay'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pay.refresh_from_db()
        self.assertEqual(pay.amount, 75)
        self.assertEqual(pay.description, 'Updated Pay')

    def test_pay_detail_delete(self):
        pay = Pay.objects.create(owner=self.user, amount=50, description='Test Pay')
        url = reverse('pay_detail', args=[pay.id])  # Replace 'pay_detail' with the actual URL name
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

