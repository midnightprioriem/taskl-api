from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api.models import Task
from api.serializers import TaskSerializer, UserSerializer
from api.permissions import IsOwner

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'tasks': reverse('task-list', request=request, format=format),
    })

class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = TaskSerializer

class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer