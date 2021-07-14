from django.urls import path
from .views import (
TodoListView, 
TodoList, 
todo_list_view,
todo_detail_view,
TodoDetail)

urlpatterns = [
    path('',todo_list_view),
    # path('<int:pk>',todo_detail_view),
    path('<int:pk>',TodoDetail.as_view()),
]