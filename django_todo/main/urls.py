from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='tasks'),
    path('create/', views.TaskCreateView.as_view(), name='tasks-create')
]