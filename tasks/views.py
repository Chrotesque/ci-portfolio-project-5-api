from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer
from cip5_api.permissions import IsCoOwnerOrReadOnly


class TaskList(generics.ListCreateAPIView):
    """ Lists tasks and allows creating them if authenticated (CR) """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TaskSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'title',
        'body',
        'owner__username'
    ]
    filterset_fields = [
        'owner__profile',
        'state',
        'priority',
        'due_date'
    ]
    ordering_fields = [
        'title',
        'body',
        'created_at',
        'updated_at',
        'due_date',
        'category',
        'state',
        'priority',
        'owner__username',
        'coowner__username'
    ]
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        """ Assigns owner upon task creation """
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Detail view of a task allowing owner to modify (RUD) """
    permission_classes = [IsCoOwnerOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
