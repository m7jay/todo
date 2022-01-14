from django.contrib.auth.views import LogoutView
from django.urls import path
from api.views.auth import TodoLoginView, TodoRegisterView
from api.views.todo import TodoCreateView, TodoDeleteView, TodoDetailView, TodoListView, TodoUpdateView

urlpatterns = [
    path('register/', TodoRegisterView.as_view(), name='register'),
    path('login/', TodoLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TodoListView.as_view(), name='todo-list'),
    path('todo/<int:pk>', TodoDetailView.as_view(), name='todo-detail'),
    path('create', TodoCreateView.as_view(), name='todo-create'),
    path('update/<int:pk>', TodoUpdateView.as_view(), name='todo-edit'),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name='todo-delete')
]
