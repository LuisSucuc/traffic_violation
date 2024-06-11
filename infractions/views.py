from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Infraction, Vehicle
from .serializers import InfractionSerializer


class LoadInfractionView(APIView):
    """ 
    View to load an infraction into the database.
    """

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
