from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

MyUser = get_user_model()

class EmailAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        email=username
        try:
            assert email != None and password != None
            user = MyUser.objects.get(email=email)
        except (ObjectDoesNotExist,):
            return None
        if user.check_password(password):
            return user
        return None