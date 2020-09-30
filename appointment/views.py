

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from appointment.models import appointment_model
from appointment.serializers import AppointmentSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi  
user_response = openapi.Response('Response', AppointmentSerializer)

@swagger_auto_schema(method='post', request_body=AppointmentSerializer,responses={200: user_response})
@api_view(['POST'])
def add(request, format=None):
    
    if request.method == 'POST':
        serializer =AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response( status=status.HTTP_400_BAD_REQUEST)
    
    
@swagger_auto_schema(method='get',responses={200: user_response})    
@api_view(['GET'])
def fromview(request, user_id, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        # user1=user.objects.get(user_id=user_id)
        appointments = appointment_model.objects.filter(user_id1=user_id)
    except appointment_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointments,many=True)
        return Response(serializer.data)

@swagger_auto_schema(method='get',responses={200: user_response})    
@api_view(['GET'])
def toview(request, user_id, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        # user1=user.objects.get(user_id=user_id)
        appointments = appointment_model.objects.filter(user_id2=user_id)
    except appointment_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointments,many=True)
        return Response(serializer.data)
    

@swagger_auto_schema(method='get',responses={200: user_response})
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(method='delete',request_body=None,)
@swagger_auto_schema(method='put', request_body=AppointmentSerializer)    
@api_view(['GET', 'PUT', 'DELETE'])
def appoint(request, appointment_id, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        appointments = appointment_model.objects.get(appointment_id=appointment_id)
    except appointment_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointments)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AppointmentSerializer(appointments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        appointments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)