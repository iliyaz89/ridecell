# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializer
from drf_haystack.viewsets import HaystackViewSet
from drf_haystack.filters import HaystackGEOSpatialFilter

from .models import Parking
from .search_indexes import ParkingIndex


class DistanceSerializer(serializers.Serializer):
    m = serializers.FloatField()
    km = serializers.FloatField()


class ParkingSerializer(HaystackSerializer):
    class Meta:
        index_classes = [ParkingIndex]
        fields = [
            "text", "address", "city", "zip_code", "autocomplete"
        ]

    def get_distance(self, obj):
        if hasattr(obj, "distance"):
            return DistanceSerializer(obj.distance, many=False).data


class ParkingSearchView(HaystackViewSet):
    index_models = [Parking]
    serializer_class = ParkingSerializer
    filter_backends = [HaystackGEOSpatialFilter]
