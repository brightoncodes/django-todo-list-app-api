from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from .form import TodoCreateForm
from .models import Todo, User
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    View,
)


class TodoListView(ListView):
    template_name = 'index.html'
    context_object_name = 'todos'
    model = Todo

    def get_queryset(self):
        return self.model.objects.order_by('done')


class TodoCreateView(CreateView):
    form_class = TodoCreateForm
    model = Todo
    template_name = 'create.html'

    def post(self,request):
        req = request.POST
        user = get_object_or_404(User,id=req.get('user'))
        Todo.objects.create(user=user,title=req.get('title'))
        return redirect('todo:index')

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'detail.html'


class TodoEditView(UpdateView):
    form_class = TodoCreateForm
    model = Todo
    template_name='edit.html'

    def post(self,request,pk):
        req  = request.POST
        user = get_object_or_404(User,id=req.get('user'))
        todo = get_object_or_404(self.model,id=pk)
        todo.user  = user
        todo.title = req.get('title')
        todo.save()
        return redirect('todo:index')


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:index')


class CheckerView(View):
    model = Todo
    def post(self, request, *args, **kwargs):
        req = request.POST
        if request.method == 'POST':
            todo = get_object_or_404(self.model, id=req.get('id'))
            if todo.done == False:
                todo.done = True
                todo.save()
                return JsonResponse({'title' : todo.title, 'done' : todo.done},safe=True)
            else:
                todo.done = False
                todo.save()
                return JsonResponse({'title' : todo.title, 'done' : todo.done},safe=True)

        return JsonResponse({'check' : 'failed'},safe=True)
    
        