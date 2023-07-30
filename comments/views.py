from rest_framework import generics, permissions, filters
from cip5_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """ Lists comments and allows creating them if authenticated (CR) """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = [
        'task__title',
        'task__body',
        'owner__username',
        'body'
    ]
    ordering_fields = [
        'task__title',
        'task__body',
        'body',
        'owner__username',
    ]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        """ Assigns owner upon comment creation """
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Detail view of a comment allowing owner to modify (RUD) """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
