from django.urls import path
from api.views import TodoCreateView, TodoDeleteView, TodoDetailView, TodoListView, TodoUpdateView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-list'),
    path('todo/<int:pk>', TodoDetailView.as_view(), name='todo-detail'),
    path('create', TodoCreateView.as_view(), name='todo-create'),
    path('update/<int:pk>', TodoUpdateView.as_view(), name='todo-edit'),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name='todo-delete')
]
