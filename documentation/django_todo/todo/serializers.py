from rest_framework import serializers

from django_todo.todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Todo
        fields = "__all__"
