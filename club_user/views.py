from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from club_user.models import club_user_model
from club_user.serializers import ClubUserSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi  
user_response = openapi.Response('Response', ClubUserSerializer)


 
@swagger_auto_schema(method='post', request_body=ClubUserSerializer,responses={200: user_response})
@api_view(['POST'])
def add(request, format=None):
    
    if request.method == 'POST':
        serializer =ClubUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response( status=status.HTTP_400_BAD_REQUEST)
    
    
@swagger_auto_schema(method='get',responses={200: user_response})    
@api_view(['GET'])
def user_specific(request, user_id, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        # user1=user.objects.get(user_id=user_id)
        clubs = club_user_model.objects.filter(user_id=user_id)
    except club_user_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClubUserSerializer(clubs,many=True)
        return Response(serializer.data)

@swagger_auto_schema(method='get',responses={200: user_response})    
@api_view(['GET'])
def club_specific(request, club_id, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        # user1=user.objects.get(user_id=user_id)
        users = club_user_model.objects.filter(club_id=club_id)
    except club_user_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =ClubUserSerializer(users,many=True)
        return Response(serializer.data)
    
    

@swagger_auto_schema(method='delete',request_body=None,)
 
@api_view(['DELETE'])
def delete(request, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        post1 = club_user_model.objects.get(user_id=request.data['user_id'],club_id=request.data['club_id'])
    except club_user_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'DELETE':
        post1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)