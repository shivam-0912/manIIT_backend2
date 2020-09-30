from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from club.models import club
from club.serializers import ClubSerializer
from user.models import user
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi  
user_response = openapi.Response('Response', ClubSerializer)
 
@swagger_auto_schema(method='get',responses={200: user_response})
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(method='delete',request_body=None,)
@swagger_auto_schema(method='put', request_body=ClubSerializer)     
@api_view(['GET', 'PUT', 'DELETE'])
def club_detail(request,pk, format=None):
    """
    Retrieve, update or delete a code item.
    """
    try:
        club1 =club.objects.get(club_id=pk)
    except club.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClubSerializer(club1)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClubSerializer(club1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        club1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
    
@swagger_auto_schema(method='get',responses={200: user_response})
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(method='delete',request_body=None,)
@swagger_auto_schema(method='put', request_body=ClubSerializer) 
@api_view(['GET', 'PUT', 'DELETE'])
def club_user_detail(request,pk, format=None):
    """
    Retrieve, update or delete a code item.
    """
    # try:
    #     user1=user.objects.get(user_id=pk)
    # except user.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        club1 =club.objects.get(user_id=pk)
    except club.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClubSerializer(club1)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClubSerializer(club1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        club1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)