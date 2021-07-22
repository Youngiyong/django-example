
from rest_framework import serializers

from lastorder.users.models import Users


class UserSerializer(serializers.ModelSerializer):
    """
        회원 정보
    """

    class Meta:
        model = Users
        fields = '__all__'