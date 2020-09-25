from rest_framework import serializers
from user.models import user,authority


class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = user
        fields = '__all__'
        
class AuthoritySerializer(serializers.ModelSerializer):
   
    class Meta:
        model =authority
        fields =  '__all__'
       