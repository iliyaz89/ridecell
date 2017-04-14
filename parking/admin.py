# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models

# Register your models here.
myModels = [models.Parking, models.Reserved]

admin.site.register(myModels)