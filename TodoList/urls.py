from django.urls import path
from . import views


urlpatterns = [
    path('todolist/', views.home, name='home'),
    path('details/<int:todo_id>/', views.details, name="details"),
    path('addTodo/', views.addTodo, name="addTodo"),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo, name="deleteTodo")
]