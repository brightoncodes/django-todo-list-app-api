from rest_framework import generics
from .serializers import TodoSerializer
from todo.models import Todo


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

