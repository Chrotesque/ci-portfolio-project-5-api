from django.http import Http404
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category
from .serializers import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    """
    Lists categaories and allowes creating them if authenticated (CR)
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'name',
        'parent__name'
    ]
    ordering_fields = [
        'name',
        'parent',
        'owner__username',
    ]
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        """ Assigns owner upon category creation """
        serializer.save(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail view of a category allowing authenticated users to modify (RUD)
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
