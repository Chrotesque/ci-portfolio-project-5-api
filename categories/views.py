from django.http import Http404
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    """ Lists categaories and allowes creating them if authenticated (CR) """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        """ Assigns owner upon category creation """
        serializer.save(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Detail view of a category allowing authenticated users to modify (RUD) """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
