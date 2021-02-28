from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import RegisterSerializer
from rest_framework import status


# Register API
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import generics, permissions, status, views
from rest_framework.authentication import TokenAuthentication
from . import serializers

User = get_user_model()


class RegisterAPIView(generics.CreateAPIView):
    """
    Endpoint for user registration.
    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.RegisterSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "User": RegisterSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
            "Success": "Data posted successfully",



        })
