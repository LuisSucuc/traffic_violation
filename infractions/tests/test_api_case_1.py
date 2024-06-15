from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import Group
from elements.models import Vehicle, Person, Officer, Color, Brand
import datetime
from rest_framework_simplejwt.tokens import RefreshToken


class CreateInfractionViewTests(APITestCase):

    def setUp(self) -> None:
        '''
            Set up the test case
        '''
        # Create a user, a group and add the user to the group
        self.officer = Officer.objects.create_user(
            username='testuser', password='testpassword')
        self.group = Group.objects.create(name='Operational Officer')
        self.officer.groups.add(self.group)

        self.color = Color.objects.create(name="Red")

        self.brand = Brand.objects.create(name="Toyota")


        self.person = Person.objects.create(
            name="John Doe", email="john@example.com")
        
        self.vehicle = Vehicle.objects.create(
            plate="ABC123", person=self.person,
            color=self.color, brand=self.brand)

        # Create a client and authenticate the user
        self.client = APIClient()
        self.refreshToken = RefreshToken.for_user(self.officer)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.refreshToken.access_token}')

    def test_create_infraction_success(self) -> None:
        '''
            Test that an infraction can be created successfully
        '''
        url = reverse('cargar_infraccion')

        data = {
            'placa_patente': 'ABC123',
            'timestamp': datetime.datetime.now().isoformat(),
            'comentarios': 'Speeding'
        }

        response = self.client.post(url, data, format='json')
        # Verify the response
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertIn('id', response.data)
        self.assertEqual(response.data['vehicle'], self.vehicle.id)
        self.assertEqual(response.data['comments'], 'Speeding')
        self.assertEqual(response.data['officer'], self.officer.id)

    def test_load_infraction_vehicle_not_found(self) -> None:
        '''
            Test that an infraction cannot be created if the vehicle is not found
        '''
        url = reverse('cargar_infraccion')
        data = {
            'placa_patente': 'XYZ789',
            'timestamp': datetime.datetime.now().isoformat(),
            'comentarios': 'Speeding'
        }

        response = self.client.post(url, data, format='json')
        # Verify the response
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Vehículo no encontrado')
