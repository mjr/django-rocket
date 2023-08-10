from django.db import models

from behaviors.behaviors import StoreDeleted, Timestamped
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


class Result(StoreDeleted, Timestamped):
    id = TimeflakePrimaryKeyBinary()
    name = models.CharField('nome', max_length=255)
    date = models.DateTimeField('data')
    first_place = models.CharField('primeiro lugar', max_length=255)
    second_place = models.CharField('segundo lugar', max_length=255)
    third_place = models.CharField('terceiro lugar', max_length=255)
    fourth_place = models.CharField('quarto lugar', max_length=255)
    fifth_place = models.CharField('quinto lugar', max_length=255)
    sixth_place = models.CharField('sexto lugar', max_length=255)
    seventh_place = models.CharField('sétimo lugar', max_length=255)
    eighth_place = models.CharField('oitavo lugar', max_length=255)
    ninth_place = models.CharField('nono lugar', max_length=255)
    tenth_place = models.CharField('décimo lugar', max_length=255)

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'resultado'
        verbose_name_plural = 'resultados'
        ordering = ('created',)

    def __str__(self):
        return self.name
