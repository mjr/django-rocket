from django.db import models

from simple_history.models import HistoricalRecords
from timeflake.extensions.django import TimeflakePrimaryKeyBinary


class Item(models.Model):
    id = TimeflakePrimaryKeyBinary()
    name = models.CharField(max_length=255)

    history = HistoricalRecords()


class InstagramAccount(models.Model):
    id = TimeflakePrimaryKeyBinary()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    history = HistoricalRecords()
