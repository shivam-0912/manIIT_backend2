


from rest_framework import serializers
from canteen.models import canteen_model


class CanteenSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = canteen_model
        fields = '__all__'
        # depth=1# -*- coding: utf-8 -*-

