from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from cip5_api.permissions import IsCoOwnerOrReadOnly


class TaskList(generics.ListCreateAPIView):
    """ Lists tasks and allows creating them if authenticated (CR) """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        """ Assigns owner upon task creation """
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Detail view of a task allowing owner to modify (RUD) """
    permission_classes = [IsCoOwnerOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
