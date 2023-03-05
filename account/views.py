from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ViewSet
from  rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView, 
    RetrieveAPIView
)

from .serializers import MyUserSerializer

MyUser = get_user_model()
# Create your views here.
class MyUserViewSet(ViewSet, ListAPIView, CreateAPIView, 
                    UpdateAPIView, RetrieveAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer