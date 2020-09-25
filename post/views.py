from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.models import club_post,user_post
from post.serializers import ClubPostSerializer,UserPostSerializer,ClubPost2Serializer,UserPost2Serializer
from user.models import user
from club.models import club

department={
    1:"cse",
    2:"mnc",
    3:"trical",
    
    
    4:"tronix",
    5:"civil",
    6:"mst",
    7:"cera",
    8:"meta",
    9:"mining",
    }
       
@api_view(['GET', 'POST'])
def user_post_view(request, format=None):
    # """
    # List all code snippets, or create a new snippet.
    # """
    # if request.method == 'GET':
    #     post1 = user_post.objects.filter(allin=1).order_by('start')
    #     serializer = UserPost2Serializer(post1, many=True)
    #     return Response(serializer.data)
    if request.method == 'POST':
        serializer =UserPost2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response( status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_post_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        post1 = user_post.objects.get(user_post_id=pk)
    except post1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserPostSerializer(post1)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserPostSerializer(post1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
       
@api_view(['GET', 'POST'])
def club_post_view(request, format=None):
    # """
    # List all code snippets, or create a new snippet.
    # """
    # if request.method == 'GET':
    #     post1 = club_post.objects.filter(allin=1).order_by('start')
    #     serializer = ClubPostSerializer(post1, many=True)
    #     return Response(serializer.data)

     if request.method == 'POST':
        serializer =ClubPost2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     else:
        return Response( status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def club_post_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        post1 = club_post.objects.get(club_post_id=pk)
    except post1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClubPostSerializer(post1)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClubPostSerializer(post1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def UserSpecificPost(request, user_id, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        # user1=user.objects.get(user_id=user_id)
        post1 = user_post.objects.filter(user_id=user_id)
    except post1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserPostSerializer(post1,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def ClubSpecificPost(request, club_id, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        club1=club.objects.get(club_id=club_id)
        post1 = club_post.objects.filter(club_id=club1)
    except post1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClubPostSerializer(post1,many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def UserStudentPost(request, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        
        post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)
    except post1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserPostSerializer(post1,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def UserProfPost(request, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        
        post1 = user_post.objects.filter(allin=2) | user_post.objects.filter(allin=3)
    except post1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserPostSerializer(post1,many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def ClubStudentPost(request, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        
        post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)
    except post1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClubPostSerializer(post1,many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def ClubProfPost(request, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        
        post1 = club_post.objects.filter(allin=2) | club_post.objects.filter(allin=3)
    except post1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClubPostSerializer(post1,many=True)
        return Response(serializer.data)
        
@api_view(['GET'])
def DeptSpecificStudentUserPost(request,dept_id, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
   
    try:
        if(dept_id==1):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(cse=1) | user_post.objects.filter(cse=3)
        elif(dept_id==2):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(mnc=1) | user_post.objects.filter(mnc=3)
        elif(dept_id==3):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(trical=1) | user_post.objects.filter(trical=3)
        elif(dept_id==4):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(tronix=1) | user_post.objects.filter(tronix=3)
        elif(dept_id==5):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(civil=1) | user_post.objects.filter(civil=3)
        elif(dept_id==6):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(mst=1) | user_post.objects.filter(mst=3)
        elif(dept_id==7):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(cera=1) | user_post.objects.filter(cera=3)
        elif(dept_id==8):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(meta=1) | user_post.objects.filter(mining=3)
        elif(dept_id==9):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(mining=1) | user_post.objects.filter(mining=3)
 
    except post1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserPostSerializer(post1,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def DeptSpecificProfUserPost(request,dept_id, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
   
    try:
        if(dept_id==1):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(cse=2) | user_post.objects.filter(cse=3)
        elif(dept_id==2):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(mnc=2) | user_post.objects.filter(mnc=3)
        elif(dept_id==3):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(trical=2) | user_post.objects.filter(trical=3)
        elif(dept_id==4):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(tronix=2) | user_post.objects.filter(tronix=3)
        elif(dept_id==5):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(civil=2) | user_post.objects.filter(civil=3)
        elif(dept_id==6):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(mst=2) | user_post.objects.filter(mst=3)
        elif(dept_id==7):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(cera=2) | user_post.objects.filter(cera=3)
        elif(dept_id==8):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(meta=2) | user_post.objects.filter(mining=3)
        elif(dept_id==9):
             post1 = user_post.objects.filter(allin=1) | user_post.objects.filter(allin=3)|user_post.objects.filter(mining=2) | user_post.objects.filter(mining=3)
 
    except post1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserPostSerializer(post1,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def DeptSpecificStudentClubPost(request,dept_id, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
   
    try:
        if(dept_id==1):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(cse=1) | club_post.objects.filter(cse=3)
        elif(dept_id==2):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(mnc=1) | club_post.objects.filter(mnc=3)
        elif(dept_id==3):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(trical=1) | club_post.objects.filter(trical=3)
        elif(dept_id==4):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(tronix=1) | club_post.objects.filter(tronix=3)
        elif(dept_id==5):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(civil=1) | club_post.objects.filter(civil=3)
        elif(dept_id==6):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(mst=1) | club_post.objects.filter(mst=3)
        elif(dept_id==7):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(cera=1) | club_post.objects.filter(cera=3)
        elif(dept_id==8):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(meta=1) | club_post.objects.filter(mining=3)
        elif(dept_id==9):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(mining=1) | club_post.objects.filter(mining=3)
 
    except post1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClubPostSerializer(post1,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def DeptSpecificProfClubPost(request,dept_id, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
   
    try:
        if(dept_id==1):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(cse=2) | club_post.objects.filter(cse=3)
        elif(dept_id==2):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(mnc=2) | club_post.objects.filter(mnc=3)
        elif(dept_id==3):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(trical=2) | club_post.objects.filter(trical=3)
        elif(dept_id==4):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(tronix=2) | club_post.objects.filter(tronix=3)
        elif(dept_id==5):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(civil=2) | club_post.objects.filter(civil=3)
        elif(dept_id==6):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(mst=2) | club_post.objects.filter(mst=3)
        elif(dept_id==7):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(cera=2) | club_post.objects.filter(cera=3)
        elif(dept_id==8):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(meta=2) | club_post.objects.filter(mining=3)
        elif(dept_id==9):
             post1 = club_post.objects.filter(allin=1) | club_post.objects.filter(allin=3)|club_post.objects.filter(mining=2) | club_post.objects.filter(mining=3)
 
    except post1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClubPostSerializer(post1,many=True)
        return Response(serializer.data)    