from reservation.models import Room, Reserve
from api.serializers import RoomAvailableSerializer, ReserveSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

import datetime
# from restProject.serializers import IsOwnerOrReadOnly#, IsMadeOrReadOnly
# from userInfo.serializers import ContactInfoSerializer, OfferSerializer
# from userInfo.models import ContactInfo, Offer
# from django.db.utils import IntegrityError


class RoomAvailableSet(viewsets.ModelViewSet):
    queryset = Room.objects.filter(available=True)
    serializer_class = RoomAvailableSerializer
    permission_classes = [IsAuthenticated]


    def get(self, request):
        serializer = RoomAvailableSerializer(self.queryset, many=True)
        return Response(serializer.data)


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
            import ipdb; ipdb.set_trace()
            requested_room_id = int(request.data["room"])
            requested_room = Room.objects.get(id=requested_room_id)
            date = datetime.datetime.strptime(request.data["date"], "%Y-%m-%d").date()

            room_not_availiable = Reserve.objects.filter(room=requested_room, date=date).exists()

            if not room_not_availiable:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class ContactInfoViewSet(viewsets.ModelViewSet):
#     queryset = ContactInfo.objects.all()
#     serializer_class = ContactInfoSerializer
#     permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]#, IsMadeOrReadOnly]
#     def get(self, request):
#         serializer = ContactInfoSerializer(self.queryset, many=True)
#         return Response(serializer.data)
#
#
# class OfferViewSet(viewsets.ModelViewSet):
#     queryset = Offer.objects.all()
#     serializer_class = OfferSerializer
#     permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
#     def get(self, request):
#         serializer = OfferSerializer(self.queryset, many=True)
#         return Response(serializer.data)
