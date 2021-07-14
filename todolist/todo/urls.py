from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path('', views.TodoListView.as_view(), name='index'),
    path('create', views.TodoCreateView.as_view(), name='create'),
    path('detail/<int:pk>', views.TodoDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', views.TodoEditView.as_view(), name='edit'),
    path('delete/<int:pk>', views.TodoDeleteView.as_view(), name='delete'),
    path('checker',views.CheckerView.as_view(), name='checker')
]
