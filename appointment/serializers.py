

from rest_framework import serializers
from appointment.models import appointment_model


class AppointmentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = appointment_model
        fields = '__all__'
        # depth=1