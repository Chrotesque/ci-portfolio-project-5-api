from django.http import Http404
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from cip5_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """ Lists profiles (R) """
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """ Detail view of a profile allowing owner to modify (RU) """
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Profile.objects.all()
