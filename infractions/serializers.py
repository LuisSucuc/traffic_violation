from .models import Infraction
from elements.models import Vehicle
from rest_framework import serializers


class InfractionSerializer(serializers.ModelSerializer):
    """ 
    Serializer for the Infraction model.
    """
    vehicle_plate = serializers.CharField(source='vehicle.plate', read_only=True)

    class Meta:
        model = Infraction
        fields = ['id', 'vehicle', 'vehicle_plate', 'timestamp', 'comments', 'officer']


class TrafficInfractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraction
        fields = ['timestamp', 'comments']


class VehicleInfractionReportSerializer(serializers.ModelSerializer):
    infractions = TrafficInfractionSerializer(many=True)

    class Meta:
        model = Vehicle
        fields = ['plate', 'infractions']
