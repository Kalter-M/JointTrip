from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# путещественник - водитель/пассажир
class Traveler(models.Model):
    # user_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    trip_passenger = models.ManyToManyField('Trip', through='TripPassenger')

    def __str__(self):
        return 'Username: %s; email: %s' % (
            self.user.username, self.email)


# поездка
class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)

    owner = models.ForeignKey(Traveler, on_delete=models.CASCADE)

    start_time = models.DateTimeField()
    duration = models.IntegerField(default=0)
    departure = models.CharField(max_length=255)
    arrival = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    number_of_seats = models.IntegerField(default=0)

    talk = models.BooleanField(default=False)
    smoke = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)

    passengers = models.ManyToManyField('Traveler', through='TripPassenger')


# пассажиры в поездке
class TripPassenger(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Traveler, on_delete=models.CASCADE)


# отзыв
class Review(models.Model):
    from_whom = models.ForeignKey(Trip, on_delete=models.CASCADE)
    to_whom = models.ForeignKey(Trip, on_delete=models.CASCADE)
    mark = models.IntegerField(validators={MinValueValidator(0),
                                           MaxValueValidator(5)})
    comment = models.CharField(max_length=255)
