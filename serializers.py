from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from hospital.models import *


class docterSerializer(serializers.ModelSerializer):
    class Meta:
        model=docter
        fields="__all__"
class patientSerializer(serializers.ModelSerializer):
    class Meta:
        model=patient
        fields="__all__"

class appointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=appointment
        fields="__all__"


