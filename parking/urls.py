from django.conf.urls import url, include
from rest_framework import routers

from .views import ParkingSearchView

router = routers.DefaultRouter()
router.register("search", ParkingSearchView, base_name="parking-search")


urlpatterns = [
    url(r"api/v1/", include(router.urls)),
]

