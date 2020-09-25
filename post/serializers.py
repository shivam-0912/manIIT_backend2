from rest_framework import serializers
from post.models import user_post,club_post
from user.serializers import UserSerializer
from club.serializers import ClubSerializer
from user.models import user
from club.models import club
class UserPostSerializer(serializers.ModelSerializer):
    # user_id=serializers.PrimaryKeyRelatedField(queryset=user.objects.all())
    # user_id=UserSerializer(read_only=False)
   
    class Meta:
        model = user_post
        fields = '__all__'
        depth=1
        
class ClubPostSerializer(serializers.ModelSerializer):

    class Meta:
        model =club_post
        fields =  '__all__'
        depth=1
       # -*- coding: utf-8 -*-

class UserPost2Serializer(serializers.ModelSerializer):
    user_id=serializers.PrimaryKeyRelatedField(queryset=user.objects.all())

   
    class Meta:
        model = user_post
        fields = '__all__'
        depth=1
        
class ClubPost2Serializer(serializers.ModelSerializer):
    club_id=serializers.PrimaryKeyRelatedField(queryset=club.objects.all())
    class Meta:
        model =club_post
        fields =  '__all__'
        depth=1
       # -*- coding: utf-8 -*-

