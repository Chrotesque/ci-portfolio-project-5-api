from django.http import Http404
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from cip5_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Profile.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Profile.objects.all()
