from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models import Q
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import BaseUserManager
User = get_user_model()


class LoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        required=False,
        allow_blank=True,
        write_only=True,
    )

    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta(object):
        model = User
        fields = ['username', 'password']

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def validate(self, data):

        username = data.get('username', None)
        password = data.get('password', None)

        if not username:
            raise serializers.ValidationError(
                "Please enter username to login.")

        user = User.objects.filter(
            Q(username=username)
        )

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("This username is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError("Invalid credentials.")

        return data
