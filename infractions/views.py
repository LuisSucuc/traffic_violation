from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Infraction, Vehicle
from .serializers import InfractionSerializer
from .serializers import VehicleInfractionReportSerializer
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


class LoadInfractionView(APIView):
    """ 
    View to load an infraction into the database.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        POST method to load an infraction into the database.
        """
        try: 
            data = request.data
            plate = data.get('placa_patente')
            timestamp = data.get('timestamp')
            comments = data.get('comentarios')

            # Check if the vehicle exists
            vehicle_query = Vehicle.objects.filter(plate=plate)

            # If the vehicle does not exist, return an error
            if not vehicle_query.exists():
                return Response({"error": "Vehículo no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            
            # Get the vehicle
            vehicle = vehicle_query.first()

            # Create the infraction
            infraction = Infraction(
                vehicle=vehicle, timestamp=timestamp, comments=comments)
            infraction.save()

            # Return the infraction
            serializer = InfractionSerializer(infraction)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        # If an exception not handled occurs, return an internal server error
        except Exception as e:
            return Response({"error": f"Internal server error: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GenerateReportView(APIView):
    """
    View to generate a report of the infractions of a person.
    """
    def get(self, request, *args, **kwargs):
        email = request.query_params.get('email')
        # Check if the email is provided
        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Validate the email
        try:
            validator = EmailValidator()
            validator(email)
        except ValidationError:
            return Response({"error": "Invalid email"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Get the vehicles of the person
        vehicles = Vehicle.objects.filter(
            person__email=email).prefetch_related('infraction_set')
        
        # Create the report data
        report_data = [
            {
                'plate': vehicle.plate,
                'infractions': vehicle.infraction_set.all()
            }
            for vehicle in vehicles
        ]

        serializer = VehicleInfractionReportSerializer(report_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
            

            