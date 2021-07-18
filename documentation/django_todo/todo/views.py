from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from serializers import TodoSerializer
from models import Todo


class ListTodoAPIView(ListAPIView):
    """Lists all todos from the database"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateTodoAPIView(CreateAPIView):
    """Creates a new todo"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UpdateTodoAPIView(UpdateAPIView):
    """Update the todo whose id has been passed through the request"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DeleteTodoAPIView(DestroyAPIView):
    """Deletes a todo whose id has been passed through the request"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
