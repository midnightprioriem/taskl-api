from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')

    class Meta:
        model = Task
        fields = ['url', 'id', 'owner', 'created', 'title', 'description', 'due_date', 'done']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(many = True, view_name = 'task-detail', read_only = True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'tasks']