from django.contrib import admin
# Register your models here.
from .models import RoomCategory, Room, Reserve, Hotel


class HotelModel(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(RoomCategory)
admin.site.register(Reserve)
admin.site.register(Hotel, HotelModel)
admin.site.register(Room)