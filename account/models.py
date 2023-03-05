from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.

class MyUser(AbstractUser):
   PHONE_REGEX = RegexValidator(
      regex=r'(84|0[3|5|7|8|9])+([0-9]{8})\b',
      message='Phone number invalid'
   )

   birth = models.DateField(blank=True, null=True)
   phone = models.CharField(blank=True, null=True, 
                              validators=(PHONE_REGEX,),
                              max_length=15)
