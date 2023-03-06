from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ViewSet
from  rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView, 
    RetrieveAPIView
)

from .serializers import (
    MyUserDetailSerializer,
    MyUserSerializer
)

MyUser = get_user_model()
# Create your views here.
class MyUserViewSet(ViewSet, CreateAPIView, 
                    UpdateAPIView, RetrieveAPIView):
    queryset = MyUser.active.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MyUserSerializer
        return MyUserDetailSerializer