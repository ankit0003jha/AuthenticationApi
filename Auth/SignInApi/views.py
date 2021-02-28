from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login

from rest_framework import permissions, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import status, views
from rest_framework.response import Response
from . import serializers


class LoginAPI(views.APIView):
    """
    Endpoint for user login. Returns authentication token on success.
    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # response_data =  {queryset = User.objects.all()}
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
