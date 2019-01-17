from django.urls import path
from todos.views import TodoList, DeleteItems

urlpatterns = [
    path('', TodoList.as_view(), name='todo-list'),
    path('delete/<itemId>', DeleteItems.as_view(), name='todo-delete'),
]