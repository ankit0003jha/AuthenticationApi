from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(
        required=True
    )

    email = serializers.EmailField(
        required=True,
        label="Email Address"
    )

    # phone_number = serializers.IntegerField(
    # required=True)

    username = serializers.CharField(
        required=True

    )
    password = serializers.CharField(
        required=True,
        label="Password",
        style={'input_type': 'password'}
    )

    class Meta(object):
        model = User
        fields = ['first_name', 'email', 'username', 'password']

    # Validation           ####################################################3

    def validate_first_name(self, value):
        if len(value) < getattr(settings, 'FIRSTNAME_MIN_LENGTH', 3):
            raise serializers.ValidationError(
                "FIRST NAME should be atleast %s characters long." % getattr(
                    settings, 'FIRSTNAME_MIN_LENGTH', 3)
            )
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_password(self, value):
        if len(value) < getattr(settings, 'PASSWORD_MIN_LENGTH', 8):
            raise serializers.ValidationError(
                "Password should be atleast %s characters long." % getattr(
                    settings, 'PASSWORD_MIN_LENGTH', 8)
            )
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("username already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],
                                   email=validated_data['email'],
                                   first_name=validated_data['first_name'],
                                   password=validated_data['password'])

        return user
