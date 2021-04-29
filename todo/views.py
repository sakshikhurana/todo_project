from django.shortcuts import render, redirect
from .models import TodoModel
from .forms import TodoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView, RedirectView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class TodoCreate(LoginRequiredMixin, CreateView):
    model = TodoModel
    form_class = TodoForm
    template_name = 'todo/create_update.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class TodoList(LoginRequiredMixin, ListView):
    model = TodoModel
    template_name = 'todo/list.html'
    context_object_name = 'todo_list'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(completed__isnull=True, user=self.request.user).order_by('created')


class TodoDetail(LoginRequiredMixin, DetailView):
    model = TodoModel
    template_name = 'todo/detail.html'
    context_object_name = 'todo'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

class TodoComplete(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        todo_obj = get_object_or_404(TodoModel, user=self.request.user, pk=kwargs['pk'])
        if todo_obj:
            todo_obj.completed=timezone.now()
            todo_obj.save()
        return reverse_lazy('todo:list')



class TodoEdit(LoginRequiredMixin, UpdateView):
    model = TodoModel
    template_name = 'todo/create_update.html'
    form_class = TodoForm

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class TodoDelete(LoginRequiredMixin, DeleteView):
    model = TodoModel
    template_name = 'todo/deleted.html'
    success_url = reverse_lazy('todo:list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
    


class TodoCompletedList(LoginRequiredMixin, ListView):
    model = TodoModel
    template_name = 'todo/complete_list.html'
    context_object_name = 'todo_complete_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(completed__isnull=False, user=self.request.user).order_by('completed')
