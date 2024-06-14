from django.db.models import Prefetch

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Infraction, Vehicle
from .serializers import EmailSerializer, InfraccionSerializerSpanish, InfractionSerializer, VehicleInfractionReportSerializer

from infractions.permissions import IsInGroupPermission


class LoadInfractionView(APIView):
    """ 
    View to load an infraction into the database.
    """
    permission_classes = [IsAuthenticated, IsInGroupPermission]

    def post(self, request, *args, **kwargs) -> Response:
        """
        POST method to load an infraction into the database.

        Args:
            request: Request object.

        Returns:
            Response object.
        """
        try:
            data = request.data
            serializer_spanish = InfraccionSerializerSpanish(data=data)

            if not serializer_spanish.is_valid():
                return Response('Verifica tus datos', errors=serializer_spanish.errors, status=status.HTTP_400_BAD_REQUEST)

            validated_data = serializer_spanish.validated_data

            # Check if the vehicle exists
            vehicle = Vehicle.objects.filter(
                plate=validated_data.get('placa_patente')).first()

            # If the vehicle does not exist, return an error
            if not vehicle:
                return Response({"error": "Vehículo no encontrado"}, status=status.HTTP_404_NOT_FOUND)

            # Get the vehicle

            # Create the infraction
            infraction = Infraction(vehicle=vehicle,
                                    comments=validated_data.get('comentarios'),
                                    timestamp=validated_data.get('timestamp'),
                                    officer=request.user)
            infraction.save()

            serializer = InfractionSerializer(infraction)

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        # If an exception not handled occurs, return an internal server error
        except Exception as e:
            print(e)
            return Response({"error": f"Error interno, contacte al administrador"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GenerateReportView(APIView):
    """
    View to generate a report of the infractions of a person.
    """

    def get(self, request, *args, **kwargs) -> Response:
        """
        GET method to generate a report of the infractions of a person.

        Args:
            request: Request object.

        Returns:
                Response object.
        """
        try:
            serializer = EmailSerializer(data=request.query_params)
            # Check if the email is provided
            if not serializer.is_valid():
                return Response({"error": "Correo electrónico inválido"}, status=status.HTTP_400_BAD_REQUEST)

            # Get the vehicles of the person
            vehicles = Vehicle.objects.select_related('brand', 'color').filter(
                person__email=serializer.validated_data.get("email")).prefetch_related(
                Prefetch('infraction_set',
                         queryset=Infraction.objects.order_by('-timestamp'))
            )

            serializer = VehicleInfractionReportSerializer(vehicles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": f"Error interno, contacte al administrador"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)