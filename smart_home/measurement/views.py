from django.shortcuts import render
from rest_framework import viewsets

from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorSerializer


# Create your views here.
class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
