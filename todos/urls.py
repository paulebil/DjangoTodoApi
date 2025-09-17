from django.urls import path

from .views import ListTodo, DetailTodo

urlpattern = [
    path("<int:pk>/", DetailTodo.as_view(), name="todo-detail" ),
    path("", ListTodo.as_view(), name="todo_list"),
]