from django.http import Http404
from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from cip5_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """ Lists profiles (R) """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = [
        'name',
        'image',
    ]
    ordering_fields = [
        'owner__username',
    ]
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """ Detail view of a profile allowing owner to modify (RU) """
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Profile.objects.all()
