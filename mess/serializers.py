

from rest_framework import serializers
from mess.models import mess_model,cancel_model


class MessSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = mess_model
        fields = '__all__'
        # depth=1# -*- coding: utf-8 -*-

class CancelSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = cancel_model
        fields = '__all__'
        # depth=1# -*- coding: utf-8 -*-
        