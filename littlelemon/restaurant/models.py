from django.db import models
from rest_framework import serializers

class Menu(models.Model):
    ID = models.PositiveSmallIntegerField(primary_key=True, unique=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.PositiveIntegerField()
    BookingDate = models.DateTimeField()

class MenuItem(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.PositiveSmallIntegerField()