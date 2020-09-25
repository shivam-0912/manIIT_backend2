from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from club.models import club
from club.serializers import ClubSerializer
from user.models import user


    
@api_view(['GET', 'PUT', 'DELETE'])
def club_detail(request,pk, format=None):
    """
    Retrieve, update or delete a code item.
    """
    try:
        club1 =club.objects.get(club_id=pk)
    except club1.DoesNotExist:
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
 
@api_view(['GET', 'PUT', 'DELETE'])
def club_user_detail(request,pk, format=None):
    """
    Retrieve, update or delete a code item.
    """
    try:
        user1=user.objects.get(user_id=pk)
        club1 =club.objects.get(user_id=user1)
    except club1.DoesNotExist:
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