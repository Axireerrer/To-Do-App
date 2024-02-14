from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView


from todo.models import Task
from todo.forms import UserListForm


class TaskItems(LoginRequiredMixin, CreateView, ListView):
    form_class = UserListForm
    model = Task
    template_name = 'todo/todo.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Задачи'
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('title'):
            Task.objects.create(title=self.request.POST.get('title'))

        if self.request.POST.get('delete'):
            Task.objects.filter(id=self.request.POST.get('delete')).delete()

        if self.request.POST.get('update'):
            item = Task.objects.get(id=self.request.POST.get('update'))
            if item.is_completed is False:
                Task.objects.filter(id=self.request.POST.get('update')).update(is_completed=True)
            else:
                Task.objects.filter(id=self.request.POST.get('update')).update(is_completed=False)

        if self.request.POST.get('user'):
            Task.objects.filter(id=self.request.POST.get('task_id')).update(user=self.request.POST.get('user'))

        return redirect('app:tasks')








