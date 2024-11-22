from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task

class TaskListView(ListView, LoginRequiredMixin):
    model = Task
    context_object_name = 'tasks'
    template_name = 'home.html'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)