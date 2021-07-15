from django.urls import path
from .views import (  
TodoCreateView,
TodoSingleView,
TodoListView,
TodoUpdateView,
TodoDeleteView)

urlpatterns = [
    path('',TodoListView.as_view(), name='todos'),
    path('create',TodoCreateView.as_view(), name='create'),
    path('<int:pk>',TodoSingleView.as_view(), name='single-todo'),
    path('edit/<int:pk>',TodoUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>',TodoDeleteView.as_view(), name='delete'),
]