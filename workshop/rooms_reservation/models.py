from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=False)


class Reservation(models.Model):
    date = models.DateField()
    comment = models.CharField(max_length=64)
    room_id = models.ForeignKey(Room)
