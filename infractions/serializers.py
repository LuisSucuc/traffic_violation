from rest_framework import serializers
from .models import Infraction


class InfractionSerializer(serializers.ModelSerializer):
    """ 
    Serializer for the Infraction model.
    """
    vehicle_plate = serializers.CharField(source='vehicle.plate', read_only=True)

    class Meta:
        model = Infraction
        fields = ['id', 'vehicle', 'vehicle_plate', 'timestamp', 'comments']
