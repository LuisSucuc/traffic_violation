from django.db import models
from elements.models import Vehicle, Officer


class Infraction(models.Model):
    """
    Model that represents an infraction.
    """
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    """vehicle: Vehicle that committed the infraction"""
    timestamp = models.DateTimeField()
    """timestamp: Date and time when the infraction was committed"""
    comments = models.TextField()
    """comments: Comments about the infraction"""
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE)
    """officer: Officer that reported the infraction"""

    def __str__(self):
        return f"Infraction for {self.vehicle.plate} at {self.timestamp}"
