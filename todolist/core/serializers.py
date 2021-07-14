from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    model = Todo
    class Meta:
        model = Todo
        fields = ['title','done','user','id']