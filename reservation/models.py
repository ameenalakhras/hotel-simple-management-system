from django.db import models
from django.contrib.auth.models import User
from mail.views import send_mail
from hotel_management.settings import DEFAULT_FROM_EMAIL, WEBSITE_NAME
from django.template.loader import render_to_string

class SoftDeleteModel(models.Model):
    deleted = models.BooleanField()


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


class Reserve(SoftDeleteModel):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    paid = models.BooleanField()

    def delete(self):
        self.deleted = True

        to_email = self.guest.email
        from_email = DEFAULT_FROM_EMAIL
        subject = f"your reservation at {WEBSITE_NAME} is cancelled "

        context = {
            "WEBSITE_NAME": WEBSITE_NAME,
            "self": self
        }
        html_content = render_to_string("mail/reservation_cancelled.html", context=context)

        send_mail(to_emails=to_email, subject=subject, html_content=html_content, from_email=from_email)
        self.save()

    def __str__(self):
        return f"room {self.room.name} for {self.guest.username} at {self.date_time}"

# >>> import uuid
# >>> uuid.uuid4()