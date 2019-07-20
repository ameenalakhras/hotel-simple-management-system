from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RoomCategory(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    available = models.BooleanField()

    def __str__(self):
        return self.name


class Reserve(models.Model):
    # from_time = models.DateTimeField()
    # to_time = models.DateTimeField()
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    paid = models.BooleanField()

    def __str__(self):
        return f"room {self.room.name} from {self.from_time} to {self.to_time}"
