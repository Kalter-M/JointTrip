from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
    User_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    cash = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return 'Username: %s; email: %s' % (
            self.username, self.email)


class Lot(models.Model):
    name = models.CharField(max_length=50)
    account = models.ForeignKey(Account, default=1, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    ended = models.DateTimeField(auto_now=True)
    minUsers = models.IntegerField(default=0)
    maxUsers = models.IntegerField(default=1000000)
    usersJoin = models.IntegerField(default=0)