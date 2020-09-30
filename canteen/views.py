from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from canteen.models import canteen_model
from canteen.serializers import CanteenSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi 

user_response = openapi.Response('Response', CanteenSerializer)

@swagger_auto_schema(method='get',responses={200: user_response})
@swagger_auto_schema(method='post', request_body=CanteenSerializer,responses={200: user_response})
@api_view(['GET', 'POST'])
def canteen_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        canteens = canteen_model.objects.all()
        serializer = CanteenSerializer(canteens, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CanteenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='get',responses={200: user_response})
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(method='delete',request_body=None,)
@swagger_auto_schema(method='put', request_body=CanteenSerializer)      
@api_view(['GET', 'PUT', 'DELETE'])
def canteen_detail(request, canteen_id, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        canteen = canteen_model.objects.get(canteen_id=canteen_id)
    except canteen_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CanteenSerializer(canteen)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CanteenSerializer(canteen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        canteen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    