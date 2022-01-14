from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class TodoLoginView(LoginView):
    template_name = 'api/login.html'
    fields = '__all__'
    redirect_authenticated_users = True

    def get_success_url(self):
        return reverse_lazy('todo-list')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todo-list')
        return super(TodoLoginView, self).get(*args, **kwargs)


class TodoRegisterView(FormView):
    template_name = 'api/register.html'
    form_class = UserCreationForm
    redirect_authenticated_users = True
    success_url = reverse_lazy('todo-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(TodoRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todo-list')
        return super(TodoRegisterView, self).get(*args, **kwargs)
