from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    plate = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='vehicles')

    def __str__(self):
        return f"{self.plate} - {self.brand}"


class Officer(models.Model):
    name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name