from django.db import models
from django.contrib.auth.models import AbstractUser



class Person(models.Model):
    """
    Model that represents a person.
    """

    name = models.CharField(max_length=255)
    """name: Name of the person"""
    email = models.EmailField(unique=True)
    """email: Unique email address of the person"""

    def __str__(self):
        return self.name


class Brand(models.Model):
    """
    Model that represents a brand.
    """

    name = models.CharField(max_length=100, unique=True)
    """name: Unique name of the brand"""

    def __str__(self):
        return self.name


class Color(models.Model):
    """
    Model that represents a color.
    """

    name = models.CharField(max_length=50, unique=True)
    """name: Unique name of the color"""

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    """
    Model that represents a vehicle.
    """

    plate = models.CharField(max_length=50, unique=True)
    """plate: Unique plate number of the vehicle"""
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='brand')
    """brand: Brand of the vehicle"""
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, related_name='color')
    """color: Color of the vehicle"""
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='owner')
    """person: Owner of the vehicle"""

    def __str__(self):
        return f"{self.plate} - {self.brand}"


class Officer(AbstractUser):
    """
    Model that represents an officer.
    """  
    first_name = None
    last_name = None

    name = models.CharField(max_length=255, blank=False, null=False)
    """name: Name of the officer"""

    def __str__(self):
        return self.email

    class Meta:
        pass
