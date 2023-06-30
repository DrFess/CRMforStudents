from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Group, Profile
from Serializers.serializer import GroupSerializer, ProfileSerializer, GeolocationSerializer


@api_view(['GET'])
def get_all_groups(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_profiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_profiles_by_parameter(request):
    parameter = request.body.decode('utf-8')
    profiles = Profile.objects.filter(group_number=int(parameter))
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_field_values(request):
    queryset = Profile.objects.all().values_list(request.GET.get('data'), flat=True)
    telegram_ids = list(queryset)
    return Response(telegram_ids)


@api_view(['POST'])
def add_profile(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def geolocation_view(request):
    serializer = GeolocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
