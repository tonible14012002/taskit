from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth import get_user_model

MyUser = get_user_model()

class MyUserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'username', 'first_name', 'last_name', 
                  'birth', 'date_joined', 'email']