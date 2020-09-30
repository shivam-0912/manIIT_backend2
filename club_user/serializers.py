from rest_framework import serializers
from club_user.models import club_user_model


class ClubUserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = club_user_model
        fields = '__all__'
        # depth=1