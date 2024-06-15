from django.test import TestCase
from elements.models import Color, Brand, Person, Vehicle


class VehicleModelTest(TestCase):

    ''' Test relationships between models '''

    def setUp(self) -> None:
        ''' Set up the test case '''

        # Create colors
        self.color = Color.objects.create(name="Red")
        self.color2 = Color.objects.create(name="Blue")

        # Create brands
        self.brand = Brand.objects.create(name="Toyota")
        self.brand2 = Brand.objects.create(name="Ford")

        # Create people
        self.person = Person.objects.create(
            name="Charlie", email="charlie@test.com")

        self.person2 = Person.objects.create(
            name="Alice", email="alice@test.com")

        # Create vehicles
        self.vehicle = Vehicle.objects.create(
            plate="ABC123",
            brand=self.brand,
            color=self.color,
            person=self.person
        )

        self.vehicle2 = Vehicle.objects.create(
            plate="XYZ987",
            brand=self.brand2,
            color=self.color2,
            person=self.person2
        )

    def test_delete_person(self) -> None:
        ''' 
        Test that when a person is deleted, the vehicle are not deleted
        '''

        # Make sure that the vehicle has been created
        self.assertEqual(Vehicle.objects.count(), 2)

        # Delete the person
        self.person.delete()

        # Make sure that the other vehicle has not been deleted
        self.assertEqual(Vehicle.objects.count(), 1)

        # Make sure that the color and brand are still there
        self.assertEqual(Color.objects.count(), 2)
        self.assertEqual(Brand.objects.count(), 2)
    
    def test_delete_vehicle(self) -> None:
        ''' 
        Test that when a vehicle is deleted, the person is not deleted
        '''

        # Make sure that the vehicle has been created
        self.assertEqual(Vehicle.objects.count(), 2)

        # Delete the vehicle
        self.vehicle2.delete()

        # Make sure that the other vehicle has not been deleted
        self.assertEqual(Vehicle.objects.count(), 1)

         # Make sure that the color and brand are still there
        self.assertEqual(Person.objects.get(name="Alice"), self.person2)
