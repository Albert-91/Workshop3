from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=False)

    def __str__(self):
        return "Nazwa: {}, Pojemność: {}, Dostępność rzutnika: {}".format(self.name, self.capacity, self.projector)


class Reservation(models.Model):
    date = models.DateField()
    comment = models.CharField(max_length=64)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return "Nazwa sali: {}, Data: {}, Komentarz: {}".format(self.room_id, self.date, self.comment)

