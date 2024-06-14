from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from elements.models import Vehicle, Person, Officer, Color, Brand
from infractions.models import Infraction
import datetime


class GenerateReportViewTests(APITestCase):

    def setUp(self) -> None:
        '''
            Set up the test case
        '''

        self.officer = Officer.objects.create_user(
            username='testuser', password='testpassword')
        
        self.person = Person.objects.create(
            name="John Doe", email="john@example.com")

        self.color = Color.objects.create(name="Red")

        self.brand = Brand.objects.create(name="Toyota")
        
        self.vehicle = Vehicle.objects.create(
            plate="ABC123", person=self.person,
            color=self.color, brand=self.brand)
        
        self.infraction = Infraction.objects.create(
            vehicle=self.vehicle,
            timestamp=datetime.datetime.now(),
            comments='Speeding',
            officer=self.officer
        )

        self.client = APIClient()

    def test_generate_report_success(self) -> None:
        '''
            Test that an infraction report can be generated successfully
        '''

        url = reverse('generar_informe')
        response = self.client.get(
            url, {'email': 'john@example.com'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['plate'], 'ABC123')
        self.assertEqual(len(response.data[0]['infractions']), 1)
        self.assertEqual(
            response.data[0]['infractions'][0]['comments'], 'Speeding')

    def test_generate_report_invalid_email(self) -> None:
        '''
            Test that an error is returned when an invalid email is provided
        '''

        url = reverse('generar_informe')
        response = self.client.get(
            url, {'email': 'invalid-email'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Invalid email')

    def test_generate_report_email_not_provided(self) -> None:
        '''
            Test that an error is returned when the email is not provided
        '''

        url = reverse('generar_informe')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Email is required')
