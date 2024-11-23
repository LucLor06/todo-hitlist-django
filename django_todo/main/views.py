from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'home.html'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['task']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)