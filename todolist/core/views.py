from re import T
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated 
from rest_framework import generics , mixins
from .serializers import TodoSerializer
from todo.models import Todo
from django.shortcuts import get_object_or_404
from rest_framework.decorators import (
    api_view, renderer_classes , permission_classes
)

from store.models import Product

class TodoCreateView(generics.CreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def post(self, request,*args, **kwargs):
        return self.create(request,*args, **kwargs)


class TodoListView(generics.ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class TodoSingleView(generics.RetrieveAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    
    def get(self, request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)


class TodoUpdateView(generics.UpdateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    
    def put(self, request,*args, **kwargs):
        return self.update(request,*args, **kwargs)


class TodoDeleteView(generics.DestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def delete(self, request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)


class TodoListViewOne(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get(self, request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

    def get_single(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def post(self, request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self, request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)


class TodoListViewTwo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,*args, **kwargs):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos,many=True)
        return Response(serializer.data)

    def post(self, request,*args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors)

# function base view for list items
@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def todo_list_view(request, format=None):
    todos = TodoSerializer(Todo.objects.all(),many=True)
    return Response(todos.data)

# function base view for single item
@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def todo_detail_view(request, pk, format=None):
    todo = get_object_or_404(Todo, pk=pk)
    serializer = TodoSerializer(todo)
    return Response(serializer.data)
