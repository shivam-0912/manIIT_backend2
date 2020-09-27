from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
import random
import math
from manIIT.settings import EMAIL_HOST_USER
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import user,authority
from user.serializers import UserSerializer,AuthoritySerializer,LoginSerializer
    
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi    
                
# send_mail("manIIT", random_str, EMAIL_HOST_USER,[ email_id])

@swagger_auto_schema(method='post', request_body=UserSerializer)
@api_view(['POST'])
def signup(request, format=None):
      if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            digits = [i for i in range(0, 10)]
            random_str = ""
    
            for i in range(6):
                index = math.floor(random.random() * 10)
                random_str += str(digits[index])
            serializer.save()
            newdict={'otp':random_str}
            newdict.update(serializer.data)
            return Response(newdict, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



user_response = openapi.Response('Response', UserSerializer)
@swagger_auto_schema(method='post', request_body=LoginSerializer,responses={200: user_response})
@api_view(['POST'])
def login(request, format=None):
    """
    List all code items, or create a new item.
    """
   
    try:
        user1= user.objects.get(email_id=request.data['email_id'],password=request.data['password'],activation=True)
    except user1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

      
    serializer = UserSerializer(user1)
    return Response(serializer.data)


@swagger_auto_schema(method='get',responses={200: user_response})
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(method='delete',request_body=None,)
@swagger_auto_schema(method='put', request_body=UserSerializer)    
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request,pk, format=None):
    """
    Retrieve, update or delete a code item.
    """
    try:
        user1 =user.objects.get(user_id=pk)
    except user1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user1)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
