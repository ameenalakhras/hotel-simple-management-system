# from rest_framework import routers
# from api.views import RoomAvailableSet, ReserveViewSet
#
# router = routers.DefaultRouter()
#
# router.register(r'available_rooms', RoomAvailableSet)
# router.register(r'reserve', ReserveViewSet)
#
# urlpatterns = router.urls

from django.urls import path
from reservation import views

urlpatterns = [
    path("hello/", views.send_message)
]
