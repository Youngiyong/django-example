from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets


class UserViewSet(viewsets.GenericViewSet):

    def create(self):

        return ""