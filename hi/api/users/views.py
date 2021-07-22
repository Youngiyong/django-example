
from rest_framework import viewsets

from lastorder.users.models import Users
from lastorder.users.serializers import UserSerializer
from lastorder.lastorder.responses import Response, ErrorResponse, ExceptionResponse


class UserViewSet(viewsets.GenericViewSet):

    models = Users
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        return ""

class LoginViewSet(viewsets.GenericViewSet):

    def logincheck(self):
        return ""

class LogoutViewSet(viewsets.GenericViewSet):

    def logout(self):
        return ""