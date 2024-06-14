from rest_framework import serializers
from .models import Infraction
from elements.models import Vehicle


class InfraccionSerializerSpanish(serializers.Serializer):
    """
    Serializer for the Spanish infraction fake model.
    """
    placa_patente = serializers.CharField(max_length=10, required=True)
    timestamp = serializers.DateTimeField(required=True)
    comentarios = serializers.CharField(max_length=255, required=True)


class InfractionSerializer(serializers.ModelSerializer):
    """ 
    Serializer for the Infraction model.
    """
    vehicle_plate = serializers.CharField(
        source='vehicle.plate', read_only=True)

    class Meta:
        model = Infraction
        fields = ['id', 'vehicle', 'vehicle_plate',
                  'timestamp', 'comments', 'officer']


class TrafficInfractionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Vehicle Infraction Report.
    """
    class Meta:
        model = Infraction
        fields = ['timestamp', 'comments']


class VehicleInfractionReportSerializer(serializers.ModelSerializer):
    """
    Serializer for the Vehicle Infraction Report.
    """
    infractions = TrafficInfractionSerializer(
        many=True, source='infraction_set')
    brand = serializers.CharField(source='brand.name')
    color = serializers.CharField(source='color.name')

    class Meta:
        model = Vehicle
        fields = ['plate', 'brand', 'color', 'infractions']


class EmailSerializer(serializers.Serializer):
    ''' 
    Serializer for the email field.
    '''
    email = serializers.EmailField()
