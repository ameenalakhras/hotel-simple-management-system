
from rest_framework import serializers
# from rest_framework.decorators import api_view, permission_classes
from reservation.models import  Room, Reserve


class RoomAvailableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'


class ReserveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserve
        fields = '__all__'