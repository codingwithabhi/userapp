from django.shortcuts import render
from rest_framework.decorators import api_view
from account.models import Profile
from api.serializers import ProfileSerializer
from django.http.response import JsonResponse
from rest_framework import status


@api_view(['GET'])
def profile_list(request):
    if request.method == 'GET':
        profile_list = Profile.objects.all()
        profile_list_serializer = ProfileSerializer(profile_list, many=True)
        return JsonResponse(profile_list_serializer.data, safe=False)
        

@api_view(['GET'])
def profile_detail(request, pk):
    try: 
        profile = Profile.objects.get(pk=pk) 
    except Profile.DoesNotExist: 
        return JsonResponse({'message': 'The Profile does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        profile_serializer = ProfileSerializer(profile) 
        return JsonResponse(profile_serializer.data) 