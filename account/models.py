from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager
from django.core.validators import RegexValidator
# Create your models here.

# Generate image  path for avatar
def get_avatar_path(instance, filename):
   return f'images/account/{instance.username}/avatar/{filename}'


class MyActiveUserManager(BaseUserManager):
   def get_queryset(self):
      return super().get_queryset().filter(is_active=True)

class MyUser(AbstractUser):
   PHONE_REGEX = RegexValidator(
      regex=r'(84|0[3|5|7|8|9])+([0-9]{8})\b',
      message='Phone number invalid'
   )

   REQUIRED_FIELDS = ['email', 'last_name', 'first_name']

   first_name = models.CharField(max_length=150, null=False, blank=False)
   last_name = models.CharField(max_length=150, null=False, blank=False)
   birth = models.DateField(blank=True, null=True)
   phone = models.CharField(blank=True, null=True, 
                              validators=(PHONE_REGEX,),
                              max_length=15)
   avatar = models.ImageField(upload_to=get_avatar_path, 
                              default='/static/images/default_avatar.jpg')
   objects = UserManager()
   active = MyActiveUserManager()