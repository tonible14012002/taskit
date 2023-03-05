
from django.urls import path, include
from rest_framework import routers
from account.views import MyUserViewSet
from account.token import  MyTokenObtainPairView

router = routers.DefaultRouter()
router.register('users', MyUserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view()),
]