from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from cip5_api.permissions import IsCoOwnerOrReadOnly


class TaskList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCoOwnerOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
