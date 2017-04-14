# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

import factory
import models


class ParkingFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Parking

    name = factory.Faker('parking1')
    longitude = -122.3986678
    latitude = 37.7811378
    address = "514 Bryant St, San Francisco, CA 94107"
    city = "San Francisco"
    zip_code = "94107"
    available = factory.Iterator([True, False])



