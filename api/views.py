from reservation.models import Room, Reserve
from api.serializers import RoomAvailableSerializer, ReserveSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

import datetime


class RoomAvailableSet(viewsets.ModelViewSet):
    queryset = Room.objects.filter(available=True)
    serializer_class = RoomAvailableSerializer
    permission_classes = [IsAuthenticated]


class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ReserveSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):

        serializer = ReserveSerializer(data=request.data)
        if serializer.is_valid():
            requested_room_id = int(request.data["room"])
            requested_room = Room.objects.get(id=requested_room_id)
            date = datetime.datetime.strptime(request.data["date"], "%Y-%m-%d").date()

            try:
                room_already_taken = Reserve.objects.get(room=requested_room, date=date)
            except Reserve.DoesNotExist:
                room_already_taken = None

            if room_already_taken is None:
                requested_room.available = False # this one should be done when saved to database not here >> to be edited
                requested_room.save()

                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
