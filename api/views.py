from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from api.models import Todo
from api.serializers import TodoSerializer


class TodoListView(ListView):
    model = Todo
    serializer_class = TodoSerializer
    context_object_name = 'todo_list'


class TodoDetailView(DetailView):
    model = Todo
    serializer_class = TodoSerializer
    context_object_name = 'todo'


class TodoCreateView(CreateView):
    model = Todo
    fields = ['user', 'title', 'description', 'status']
    success_url = reverse_lazy('todo-list')


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['user', 'title', 'description', 'status']
    success_url = reverse_lazy('todo-list')


class TodoDeleteView(DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('todo-list')
