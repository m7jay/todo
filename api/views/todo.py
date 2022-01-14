from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from api.models import Todo
from api.serializers import TodoSerializer

from django.contrib.auth.mixins import LoginRequiredMixin


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    serializer_class = TodoSerializer
    context_object_name = 'todo_list'

    def get_queryset(self):
        queryset = Todo.objects.filter(user=self.request.user)
        search_input = self.request.GET.get('search-area') or None
        if search_input:
            queryset = queryset.filter(title__istartswith=search_input)
        return queryset

    def get_context_data(self, **kwargs):
        search_input = self.request.GET.get('search-area') or None
        context = super().get_context_data(**kwargs)
        context['search_input'] = search_input
        return context


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    serializer_class = TodoSerializer
    context_object_name = 'todo'


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('todo-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('todo-list')


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('todo-list')
