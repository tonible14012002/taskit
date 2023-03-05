from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ViewSet
from  rest_framework.generics import (ListAPIView)

from .serializers import MyUserSerializer

MyUser = get_user_model()
# Create your views here.
class MyUserViewSet(ViewSet, ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

