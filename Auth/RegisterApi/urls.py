from .views import RegisterAPIView
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPIView.as_view(), name='register'),
]