# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from haystack.utils.geo import Point


class Parking(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def coordinates(self):
        return Point(self.longitude, self.latitude)

    def __str__(self):
        return "%s" % (self.name)



class Reserved(models.Model):
    parking = models.ForeignKey(Parking)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('parking', 'start')

    def __str__(self):
        return "{} {}".format(self.parking)


    def save(self, *args, **kwargs):
        try:
            Parking.objects.filter(id=self.parking.id).update(available=False)
        except Exception, e:
            print e
        super(Reserved, self).save(*args, **kwargs)