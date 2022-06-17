from pickle import TRUE
from typing import Text
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
   # author = models.ForeignKey(get_user_model())
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,)
    time = models.DateTimeField( 
        auto_now_add=True,
        auto_now=False,)
    #post = models.ForeignKey('Post', on_delete=models.CASCADE,)

    # Create your models here.

#from django.contrib.auth.models import AbstractUser

#class User(AbstractUser):
#    pass

